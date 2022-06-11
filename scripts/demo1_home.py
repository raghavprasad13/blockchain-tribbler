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


def demo_home(account, username):

    tribbler = TribblerMain(
        account=account,
        tribblerAddr=TRIBBLER_CONTRACT_HASH,
    )

    homeTribList = tribbler.homeTx(username)

    print(homeTribList)


def main():
    network.gas_price("50 gwei")

    # account = accounts.load("test-account1")
    account = accounts.add(config["wallets"]["from_key"])
    # account = accounts[0]

    username = "demouser1"

    demo_home(account, username)
