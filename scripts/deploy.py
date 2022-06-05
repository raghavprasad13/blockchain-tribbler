from typing import List
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
from .constants import *


class TribblerMain:
    def __init__(self, account):
        self.account = account
        self.init_gas_used = 0

        contract = String.deploy({"from": self.account})
        self.init_gas_used += contract.tx.gas_used

        contract = Tribs.deploy({"from": self.account})
        self.init_gas_used += contract.tx.gas_used

        contract = Utils.deploy({"from": self.account})
        self.init_gas_used += contract.tx.gas_used

        self.contract = Tribbler.deploy({"from": self.account})
        self.init_gas_used += self.contract.tx.gas_used

    def followTx(self, who: str, whom: str) -> network.transaction.TransactionReceipt:
        tx, gas_used = self.followOrUnfollowTx(True, who, whom)

        return tx, gas_used

    def unfollowTx(self, who: str, whom: str) -> network.transaction.TransactionReceipt:
        tx, gas_used = self.followOrUnfollowTx(False, who, whom)

        return tx, gas_used

    def followOrUnfollowTx(
        self, isFollow: bool, who: str, whom: str
    ) -> network.transaction.TransactionReceipt:
        gas_used = 0
        tx = self.contract.followOrUnfollow(who, whom)
        tx.wait(1)
        success = tx.return_value

        if not success:
            return None

        tx_hash = tx.txid[2:]
        gas_used += tx.gas_used

        tx = self.contract.appendToFollowUnfollowLog(isFollow, who, whom, tx_hash)
        tx.wait(1)
        gas_used += tx.gas_used

        return tx, gas_used

    def postTx(self, who: str, message: str) -> network.transaction.TransactionReceipt:
        gas_used = 0
        tx = self.contract.post(who, message)
        tx.wait(1)
        success = tx.return_value

        if not success:
            return None

        tx_index = tx.txindex
        timestamp = int(time.time())
        block_num = tx.block_number

        gas_used += tx.gas_used

        tx = self.contract.addTrib(who, message, timestamp, block_num, tx_index)
        tx.wait(1)
        gas_used += tx.gas_used

        return tx, gas_used

    def signupTx(self, username: str) -> network.transaction.TransactionReceipt:
        tx = self.contract.signup(username)
        tx.wait(1)

        success = tx.return_value

        if not success:
            return None
        return tx, tx.gas_used

    def listUsersTx(self) -> List[str]:
        users = list(self.contract.listUsers())
        users.sort()

        return users

    def tribsTx(self, username: str):
        tribs = list(self.contract.tribs(username))
        tribs = [tuple(trib) for trib in tribs]

        tribs = sorted(
            tribs, key=lambda trib: (-trib[3], trib[4], trib[2], trib[1], trib[0])
        )

        return tribs

    def isFollowingTx(self, who: str, whom: str) -> bool:
        followingList = self.followingTx(who)
        return whom in followingList

    def followingTx(self, username: str) -> List[str]:
        followList = list(self.contract.following(username))
        followList = [tuple(follow)[2] for follow in followList]

        return followList

    def homeTx(self, username: str) -> network.transaction.TransactionReceipt:
        homeList = list(self.contract.home(username))
        homeList = [tuple(trib) for trib in homeList]

        sorted(
            homeList, key=lambda trib: (-trib[3], trib[4], trib[2], trib[1], trib[0])
        )

        homeList = homeList[:MAX_TRIB_FETCH]

        return homeList


def deploy_tribbler():
    tribbler = TribblerMain(accounts[0])
    tx_types_gas_used = {
        method_name: 0
        for method_name in dir(tribbler)
        if callable(getattr(tribbler, method_name))
        and not method_name.startswith("__")
        and method_name not in ["followOrUnfollowTx", "listUsersTx"]
    }

    tx_types = tx_types_gas_used.keys()

    total_gas_used = 0

    _, gas_used = tribbler.signupTx("raghav")
    tx_types_gas_used.update({"signupTx": gas_used})
    total_gas_used += gas_used

    tribbler.signupTx("harsh")

    _, gas_used = tribbler.postTx("raghav", "hello world, I am raghav")
    tx_types_gas_used.update({"postTx": gas_used})
    total_gas_used += gas_used

    tribbler.postTx("raghav", "this is my 2nd trib")

    _, gas_used = tribbler.followTx("raghav", "harsh")
    tx_types_gas_used.update({"followTx": gas_used})
    total_gas_used += gas_used

    home = tribbler.homeTx("raghav")
    print(f"Home: {home}")
    # tx_types_gas_used.update({"homeTx": gas_used})
    # total_gas_used += gas_used

    followingList = tribbler.followingTx("raghav")
    print(f"Raghav is following: {followingList}")
    # tx_types_gas_used.update({"followingTx": gas_used})
    # total_gas_used += gas_used

    isFollowing = tribbler.isFollowingTx("raghav", "harsh")
    print(f"Raghav is following Harsh: {isFollowing}")
    # tx_types_gas_used.update({"isFollowingTx": gas_used})
    # total_gas_used += gas_used

    users = tribbler.listUsersTx()
    print(f"All users: {users}")
    # tx_types_gas_used.update({"listUsersTx": gas_used})
    # total_gas_used += gas_used

    tribs = tribbler.tribsTx("raghav")
    print(f"Raghav's tribs: {tribs}")
    # tx_types_gas_used.update({"tribsTx": gas_used})
    # total_gas_used += gas_used

    _, gas_used = tribbler.unfollowTx("raghav", "harsh")
    tx_types_gas_used.update({"unfollowTx": gas_used})
    total_gas_used += gas_used

    print(tx_types_gas_used)
    print(f"init gas: {tribbler.init_gas_used}")


def main():
    deploy_tribbler()
