from typing import List, Tuple
import time
from brownie import (
    accounts,
    Tribbler,
    Utils,
    Tribs,
    String,
    network,
)


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

    def followTx(
        self, who: str, whom: str
    ) -> Tuple[network.transaction.TransactionReceipt, int]:
        tx, gas_used = self.followOrUnfollowTx(True, who, whom)

        return tx, gas_used

    def unfollowTx(
        self, who: str, whom: str
    ) -> Tuple[network.transaction.TransactionReceipt, int]:
        tx, gas_used = self.followOrUnfollowTx(False, who, whom)

        return tx, gas_used

    def followOrUnfollowTx(
        self, isFollow: bool, who: str, whom: str
    ) -> Tuple[network.transaction.TransactionReceipt, int]:
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

    def postTx(
        self, who: str, message: str
    ) -> Tuple[network.transaction.TransactionReceipt, int]:
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

    def signupTx(
        self, username: str
    ) -> Tuple[network.transaction.TransactionReceipt, int]:
        tx = self.contract.signup(username)
        tx.wait(1)

        success = tx.return_value

        if not success:
            return None
        return tx, tx.gas_used

    def listUsersTx(self) -> Tuple[List[str], int]:
        tx = self.contract.listUsers()

        return tx.return_value, tx.gas_used

    def tribsTx(
        self, username: str
    ) -> Tuple[network.transaction.TransactionReceipt, int]:
        tx = self.contract.tribs(username)
        tx.wait(1)

        return tx, tx.gas_used

    def isFollowingTx(self, who: str, whom: str) -> Tuple[bool, int]:
        tx = self.contract.isFollowing(who, whom)
        tx.wait(1)

        return tx.return_value, tx.gas_used

    def followingTx(self, username: str) -> List[str]:
        tx = self.contract.following(username)
        tx.wait(1)

        return tx.return_value, tx.gas_used

    def homeTx(
        self, username: str
    ) -> Tuple[network.transaction.TransactionReceipt, int]:
        tx = self.contract.home(username)
        tx.wait(1)

        return tx, tx.gas_used


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

    _, gas_used = tribbler.followTx("raghav", "harsh")
    tx_types_gas_used.update({"followTx": gas_used})
    total_gas_used += gas_used

    _, gas_used = tribbler.homeTx("raghav")
    tx_types_gas_used.update({"homeTx": gas_used})
    total_gas_used += gas_used

    _, gas_used = tribbler.followingTx("raghav")
    tx_types_gas_used.update({"followingTx": gas_used})
    total_gas_used += gas_used

    _, gas_used = tribbler.isFollowingTx("raghav", "harsh")
    tx_types_gas_used.update({"isFollowingTx": gas_used})
    total_gas_used += gas_used

    _, gas_used = tribbler.tribsTx("raghav")
    tx_types_gas_used.update({"tribsTx": gas_used})
    total_gas_used += gas_used

    _, gas_used = tribbler.unfollowTx("raghav", "harsh")
    tx_types_gas_used.update({"unfollowTx": gas_used})
    total_gas_used += gas_used

    print(tx_types_gas_used)
    print(f"init_gas: {tribbler.init_gas_used}")


def main():
    deploy_tribbler()


if __name__ == "__main__":
    main()
