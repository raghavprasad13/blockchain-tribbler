from ctypes import util
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
import subprocess


class TribblerMain:
    def __init__(
        self,
        account,
        stringContractAddr=None,
        tribsContractAddr=None,
        utilsContractAddr=None,
        tribblerContractAddr=None,
    ):
        self.account = account

        if tribblerContractAddr is not None:
            self.stringContract = String.at(stringContractAddr, {"from": self.account})
            self.tribsContract = Tribs.at(tribsContractAddr, {"from": self.account})
            self.utilsContract = Utils.at(utilsContractAddr, {"from": self.account})
            self.contract = Tribbler.at(tribblerContractAddr, {"from": self.account})
        else:
            self.stringContract = String.deploy({"from": self.account})
            self.tribsContract = Tribs.deploy({"from": self.account})
            self.utilsContract = Utils.deploy({"from": self.account})
            self.contract = Tribbler.deploy({"from": self.account})

    def getContractAddresses(self):
        return {
            "String_contract": self.stringContract.address,
            "Tribs_contract": self.tribsContract.address,
            "Utils_contract": self.utilsContract.address,
            "Tribbler_contract": self.contract.address,
        }

    def followTx(self, who: str, whom: str) -> network.transaction.TransactionReceipt:
        return self.followOrUnfollowTx(True, who, whom)

    def unfollowTx(self, who: str, whom: str) -> network.transaction.TransactionReceipt:
        return self.followOrUnfollowTx(False, who, whom)

    def followOrUnfollowTx(
        self, isFollow: bool, who: str, whom: str
    ) -> network.transaction.TransactionReceipt:
        tx = self.contract.followOrUnfollow(who, whom)
        tx.wait(1)
        success = tx.return_value

        if not success:
            return None

        tx_hash = tx.txid
        tx = self.contract.appendToFollowUnfollowLog(isFollow, who, whom, tx_hash)
        tx.wait(1)
        return tx

    def postTx(self, who: str, message: str) -> network.transaction.TransactionReceipt:
        tx = self.contract.post(who, message)
        tx.wait(1)
        success = tx.return_value

        if not success:
            return None

        tx_index = tx.txindex
        timestamp = int(time.time())
        block_num = tx.block_number

        tx = self.contract.addTrib(who, message, timestamp, block_num, tx_index)
        tx.wait(1)
        return tx

    def signupTx(self, username: str) -> network.transaction.TransactionReceipt:
        tx = self.contract.signup(username)
        tx.wait(1)

        success = tx.return_value

        if not success:
            return None
        return tx

    def listUsersTx(self) -> List[str]:
        tx = self.contract.listUsers()

        return sorted(tx.return_value)

    def tribsTx(self, username: str) -> network.transaction.TransactionReceipt:
        tx = self.contract.tribs(username)
        tx.wait(1)

        return tx

    def isFollowingTx(self, who: str, whom: str) -> bool:
        tx = self.contract.isFollowing(who, whom)
        tx.wait(1)

        return tx.return_value

    def followingTx(self, username: str) -> List[str]:
        tx = self.contract.following(username)
        tx.wait(1)

        return tx.return_value

    def homeTx(self, username: str) -> network.transaction.TransactionReceipt:
        tx = self.contract.home(username)
        tx.wait(1)

        return tx


# def deploy_tribbler():
#     tribbler = TribblerMain(accounts[0])

#     # import os

#     # pwd = os.getcwd()
#     # print(pwd)

#     # p1 = subprocess.Popen(
#     #     "{}/blockchain-tribbler-venv/bin/python {}/scripts/deploy1.py {}".format(
#     #         pwd, pwd, tribbler.getContractAddress()
#     #     ),
#     #     shell=True,
#     # )
#     # subprocess.Popen("python3 deploy2.py", shell=True)

#     import time

#     time.sleep(120)

#     # p1.wait()

#     print(tribbler.listUsersTx())

#     print("Ending...")


# def main():
#     deploy_tribbler()


# if __name__ == "__main__":
#     main()
