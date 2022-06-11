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


def demo_signup(account, username):

    tribbler = TribblerMain(
        account=account,
        tribblerAddr=TRIBBLER_CONTRACT_HASH,
    )

    tribbler.signupTx(username)

    print("Signup successful")


def main():
    network.gas_price("50 gwei")

    # account = accounts.load("test-account1")
    account = accounts.add(config["wallets"]["from_key"])
    # account = accounts[0]

    username = "demouser2"
    demo_signup(account, username)
