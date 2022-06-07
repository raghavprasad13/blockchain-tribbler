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
import os
from multiprocessing import Process


def run(gas_price: int, num_tribs: int, user: str, account, timestamp):
    network.gas_price(str(gas_price) + " gwei")
    # account = accounts[6]

    tribbler = TribblerMain(
        account=account,
        utilsAddr=None,
        tribblerAddr=None,
    )

    tribbler.signupTx(user)

    file_name = "parallel_post_local"
    # now = int(time.time())

    final_file_name = "_".join(
        [file_name, str(gas_price), str(timestamp), user, ".csv"]
    )

    pwd = os.getcwd()

    f = open(join(pwd, "data", final_file_name), "w")
    for trib_num in range(1, num_tribs + 1):
        start = time.time()
        tribbler.postTx(user, "trib" + str(trib_num))
        end = time.time()

        time_taken = round(end - start, 2)
        f.write(str(trib_num) + "," + str(time_taken))

    f.close()


def main():
    # account = accounts.load("test-account1")
    account = accounts[7]

    timestamp = int(time.time())

    # gas_prices = [GAS_PRICE_SAFE_LOW, GAS_PRICE_STANDARD, GAS_PRICE_FAST]
    num_tribs = 2
    n_processes = 3
    # for gas_price in gas_prices:

    users = ["raghav", "rajdeep", "harsh"]
    processes = []

    for i in range(n_processes):
        p = Process(
            target=run,
            args=(GAS_PRICE_STANDARD, num_tribs, users[i], account, timestamp),
        )
        processes.append(p)
        # Pin created processes in a round-robin
        p.start()
        print(i, cpu_count(), i % cpu_count(), p.pid)
        system("taskset -p -c %d %d" % ((i % cpu_count()), p.pid))

    for process in processes:
        process.wait()
