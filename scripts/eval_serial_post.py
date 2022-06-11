"""
Sign up users and make 100 tribs
check time taken for different gas prices

Usage: brownie run scripts/eval_serial_post
"""

from brownie import accounts, network, config
import time
from .deploy import TribblerMain
from .constants import (
    GAS_PRICE_FAST,
    GAS_PRICE_SAFE_LOW,
    GAS_PRICE_STANDARD,
    TRIBBLER_CONTRACT_HASH,
    GAS_PRICE_COMMON,
)
from os.path import join
import os


def run(gas_price: int, num_tribs: int, account, timestamp):
    network.gas_price(str(gas_price) + " gwei")
    # account = accounts[6]

    tribbler = TribblerMain(
        account=account,
        tribblerAddr=TRIBBLER_CONTRACT_HASH,
    )

    users = ["serialuser1", "serialuser2", "serialuser3", "serialuser4", "serialuser5"]

    user = users[0]

    if gas_price == 10:
        user = users[0]
    elif gas_price == 20:
        user = users[1]
    elif gas_price == 30:
        user = users[2]
    elif gas_price == 40:
        user = users[3]
    else:
        user = users[4]

    # print(user)

    # tribbler.signupTx(user)

    file_name = "new_parallel_post"

    final_file_name = "_".join([file_name, str(gas_price), str(timestamp), ".csv"])
    # print(final_file_name)

    pwd = os.getcwd()

    f = open(join(pwd, "data", final_file_name), "a")
    for trib_num in range(1, num_tribs + 1):
        start = time.time()
        tribbler.postTx(user, "trib" + str(trib_num))
        end = time.time()

        time_taken = round(end - start, 3)
        f.write(str(trib_num) + "," + str(time_taken) + "\n")

        time.sleep(1)

    f.close()


def main():
    # account = accounts.load("test-account1")

    account = accounts.add(config["wallets"]["from_key"])
    # account = accounts[0]

    timestamp_now = int(time.time())

    # gas_prices = [GAS_PRICE_SAFE_LOW, GAS_PRICE_STANDARD, GAS_PRICE_FAST]
    # gas_prices = [GAS_PRICE_FAST, GAS_PRICE_STANDARD, GAS_PRICE_SAFE_LOW]
    # gas_prices = [GAS_PRICE_COMMON]
    gas_prices = [50, 40, 30, 20, 10]  # gas price in gwei
    num_tribs = 105
    for gas_price in gas_prices:
        run(
            gas_price=gas_price,
            num_tribs=num_tribs,
            account=account,
            timestamp=timestamp_now,
        )
