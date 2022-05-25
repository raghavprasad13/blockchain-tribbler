from asyncio import constants
from brownie import (
    accounts,
    config,
    Tribbler,
    Utils,
    Tribs,
    Constants,
    String,
    network,
)


def deploy_tribbler():
    account = accounts[0]
    Utils.deploy({"from": account})
    Tribs.deploy({"from": account})
    String.deploy({"from": account})
    # Constants.deploy({"from": account})
    # StringHeap.deploy({"from": account})
    tribbler = Tribbler.deploy({"from": account})
    tx = tribbler.signUp("raghav")
    tx.wait(1)
    print(f"tx: {tx}, user signup: {tx.return_value}, tx id: {type(tx.return_value)}")
    print(f"tx hash: {tx.txid}, type: {type(tx.txid)}")


def main():
    deploy_tribbler()
