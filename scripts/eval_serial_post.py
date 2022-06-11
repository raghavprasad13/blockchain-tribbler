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
import os


def run(gas_price: int, num_tribs: int, account, timestamp):
    network.gas_price(str(gas_price) + " gwei")
    # account = accounts[6]

    tribbler = TribblerMain(
        account=account,
        utilsAddr=UTILS_CONTRACT_HASH,
        tribblerAddr=TRIBBLER_CONTRACT_HASH,
    )

    users = ["raghav", "rajdeep", "harsh"]

    # user = users[0]
    if gas_price == GAS_PRICE_STANDARD:
        user = "raghav"
    elif gas_price == GAS_PRICE_SAFE_LOW:
        user = "rajdeep"
    else:
        user = "harsh"

    # tribbler.signupTx(user)

    file_name = "serial_post"

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

    f.close()


def main():
    account = accounts.load("test-account1")

    timestamp_now = int(time.time())

    # gas_prices = [GAS_PRICE_SAFE_LOW, GAS_PRICE_STANDARD, GAS_PRICE_FAST]
    gas_prices = [GAS_PRICE_FAST, GAS_PRICE_STANDARD, GAS_PRICE_SAFE_LOW]
    num_tribs = 105
    for gas_price in gas_prices:
        run(
            gas_price=gas_price,
            num_tribs=num_tribs,
            account=account,
            timestamp=timestamp_now,
        )
