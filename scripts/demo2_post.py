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


def demo_post(account, username):

    tribbler = TribblerMain(
        account=account,
        tribblerAddr=TRIBBLER_CONTRACT_HASH,
    )

    message1 = "trib A from user {}".format(username)
    tribbler.postTx(username, message1)

    print("trib A post complete")

    message2 = "trib B from user {}".format(username)
    tribbler.postTx(username, message1)

    print("trib B post complete")


def main():
    network.gas_price("50 gwei")

    # account = accounts.load("test-account1")
    account = accounts.add(config["wallets"]["from_key"])
    # account = accounts[0]

    username = "demouser2"
    demo_post(account, username)
