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
import argparse


def run(gas_price: int, num_tribs: int):
    network.gas_price(str(gas_price) + " gwei")
    account = accounts[6]

    tribbler = TribblerMain(
        account=account,
        utilsAddr=UTILS_CONTRACT_HASH,
        tribblerAddr=TRIBBLER_CONTRACT_HASH,
    )

    users = ["raghav", "rajdeep", "harsh"]

    user = users[0]

    tribbler.signupTx(user)

    file_name = "serial_post"
    now = int(time.time())

    final_file_name = "_".join([file_name, str(gas_price), str(now), ".csv"])

    f = open(join("..", "data", final_file_name), "w")
    for trib_num in range(1, num_tribs + 1):
        start = time.time()
        tribbler.postTx(user, "trib" + str(trib_num))
        end = time.time()

        time_taken = round(end - start, 2)
        f.write(str(trib_num) + "," + str(time_taken))

    f.close()


gas_prices = [GAS_PRICE_SAFE_LOW, GAS_PRICE_STANDARD, GAS_PRICE_FAST]
num_tribs = 500
for gas_price in gas_prices:
    run(gas_price=gas_price, num_tribs=num_tribs)
