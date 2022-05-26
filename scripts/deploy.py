import time
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


def followTx(
    tribbler: network.contract.ContractContainer, who: str, whom: str
) -> network.transaction.TransactionReceipt:
    return followOrUnfollowTx(tribbler, True, who, whom)


def unfollowTx(
    tribbler: network.contract.ContractContainer, who: str, whom: str
) -> network.transaction.TransactionReceipt:
    return followOrUnfollowTx(tribbler, False, who, whom)


def followOrUnfollowTx(
    tribbler: network.contract.ContractContainer, isFollow: bool, who: str, whom: str
) -> network.transaction.TransactionReceipt:
    tx = tribbler.followOrUnfollow(who, whom)
    tx.wait(1)
    success = tx.return_value

    if not success:
        return None

    tx_hash = tx.txid
    tx = tribbler.appendToFollowUnfollowLog(isFollow, whom, tx_hash)
    tx.wait(1)
    return tx


def postTx(
    tribbler: network.contract.ContractContainer, who: str, message: str
) -> network.transaction.TransactionReceipt:
    tx = tribbler.post(who, message)
    tx.wait(1)
    success = tx.return_value

    if not success:
        return None

    tx_index = tx.txindex
    timestamp = int(time.time())
    block_num = tx.block_number

    tx = tribbler.addTrib(who, message, timestamp, block_num, tx_index)
    tx.wait(1)
    return tx


def deploy_tribbler():
    account = accounts[0]

    # the order of deployments of contracts matters because some contracts are dependent on others
    String.deploy({"from": account})
    Tribs.deploy({"from": account})
    Utils.deploy({"from": account})
    String.deploy({"from": account})
    # Constants.deploy({"from": account})
    # StringHeap.deploy({"from": account})
    tribbler = Tribbler.deploy({"from": account})
    print(type(Tribbler))
    tx = tribbler.signUp("raghav")
    tx.wait(1)
    tx = tribbler.signUp("harsh")
    tx.wait(1)
    # tx = tribbler.follow("raghav", "harsh")
    # tx.wait(1)
    print(f"tx: {tx}, tx return: {type(tx)}")
    # print(f"tx: {tx}, user signup: {tx.return_value}, tx id: {type(tx.return_value)}")
    # print(f"tx hash: {tx.txid}, type: {type(tx.txid)}")


def main():
    deploy_tribbler()
