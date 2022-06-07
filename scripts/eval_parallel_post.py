"""
sign up 1 user and make him post ~500 tribs
check time taken for different gas prices

Usage: brownie run scripts/eval_serial_post
"""

from brownie import accounts, network
import time
from .deploy import TribblerMain
from .constants import (
    GAS_PRICE_FAST,
    GAS_PRICE_SAFE_LOW,
    GAS_PRICE_STANDARD,
    TRIBBLER_CONTRACT_HASH,
    UTILS_CONTRACT_HASH,
)
from os.path import join
from os import system, cpu_count
from multiprocessing import Process


def run(gas_price: int, num_tribs: int, user: str):
    network.gas_price(str(gas_price) + " gwei")
    account = accounts[6]

    tribbler = TribblerMain(
        account=account,
        utilsAddr=UTILS_CONTRACT_HASH,
        tribblerAddr=TRIBBLER_CONTRACT_HASH,
    )

    tribbler.signupTx(user)

    file_name = "parallel_post"
    now = int(time.time())

    final_file_name = "_".join([file_name, str(gas_price), str(now), user, ".csv"])

    f = open(join("..", "data", final_file_name), "w")
    for trib_num in range(1, num_tribs + 1):
        start = time.time()
        tribbler.postTx(user, "trib" + str(trib_num))
        end = time.time()

        time_taken = round(end - start, 2)
        f.write(str(trib_num) + "," + str(time_taken))

    f.close()


# gas_prices = [GAS_PRICE_SAFE_LOW, GAS_PRICE_STANDARD, GAS_PRICE_FAST]
num_tribs = 100
n_processes = 2
# for gas_price in gas_prices:

users = ["raghav", "rajdeep"]
processes = []

for i in range(n_processes):
    p = Process(target=run, args=(GAS_PRICE_STANDARD, num_tribs, users[i]))
    processes.append(p)
    # Pin created processes in a round-robin
    system("taskset -p -c %d %d" % ((i % cpu_count()), p.pid))
    p.start()

for process in processes:
    process.wait()
