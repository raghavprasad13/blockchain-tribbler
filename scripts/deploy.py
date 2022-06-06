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
from .utils import *


class TribblerMain:
    def __init__(self, account, utilsAddr=None, tribblerAddr=None):
        self.account = account
        self.init_gas_used = 0

        # contract = String.deploy({"from": self.account})
        # self.init_gas_used += contract.tx.gas_used

        # contract = Tribs.deploy({"from": self.account})
        # self.init_gas_used += contract.tx.gas_used

        if utilsAddr is None:
            self.utils_contract = Utils.deploy({"from": self.account})
            self.init_gas_used += self.utils_contract.tx.gas_used
        else:
            self.utils_contract = Utils.at(utilsAddr)

        if tribblerAddr is None:
            self.contract = Tribbler.deploy({"from": self.account})
            self.init_gas_used += self.contract.tx.gas_used
        else:
            self.contract = Tribbler.at(tribblerAddr)

    def getContractAddress(self):
        return {
            "utils_contract": self.utils_contract.address,
            "tribbler_contract": self.contract.address,
        }

    def followTx(self, who: str, whom: str) -> network.transaction.TransactionReceipt:
        tx, gas_used, isConcurrentSuccessful = self.followOrUnfollowTx(True, who, whom)

        return tx, gas_used, isConcurrentSuccessful

    def unfollowTx(self, who: str, whom: str) -> network.transaction.TransactionReceipt:
        tx, gas_used, isConcurrentSuccessful = self.followOrUnfollowTx(False, who, whom)

        return tx, gas_used, isConcurrentSuccessful

    def followOrUnfollowTx(
        self, isFollow: bool, who: str, whom: str
    ) -> network.transaction.TransactionReceipt:
        if not isValidUsername(who) or not isValidUsername(whom):
            return None, None

        if whoWhomSame(who, whom):
            return None, None

        followingList = self.followingTx(who)

        if len(followingList) >= MAX_FOLLOWING:
            # following too many people. equal to check makes sure that if max following then this also won't get appended to the log
            return None, None

        if isFollow and whom in followingList:
            # already following
            return None, None

        if not isFollow and whom not in followingList:
            # already not following
            return None, None

        gas_used = 0
        tx = self.contract.followOrUnfollow(who, whom, {"from": self.account})
        tx.wait(1)
        success = tx.return_value

        if not success:
            return None

        tx_hash = tx.txid[2:]
        gas_used += tx.gas_used

        tx = self.contract.appendToFollowUnfollowLog(
            isFollow, who, whom, tx_hash, {"from": self.account}
        )
        tx.wait(1)
        gas_used += tx.gas_used

        # again go through the log and check if this succeeded
        followUnfollowLog = list(self.contract.following(who))

        # iterate from start and look for hash.
        for log_i in followUnfollowLog:
            if log_i[2] == tx_hash:  # 2nd index is tx_hash
                return tx, gas_used, True
            else:
                return tx, gas_used, True

        # return tx, gas_used

    def postTx(self, who: str, message: str) -> network.transaction.TransactionReceipt:
        if isLongTrib(message):
            return None, None

        if not isValidUsername(who):
            return None, None

        gas_used = 0
        tx = self.contract.post(who, message, {"from": self.account})
        tx.wait(1)
        success = tx.return_value

        if not success:
            return None

        tx_index = tx.txindex
        timestamp = int(time.time())
        block_num = tx.block_number

        gas_used += tx.gas_used

        tx = self.contract.addTrib(
            who, message, timestamp, block_num, tx_index, {"from": self.account}
        )
        tx.wait(1)
        gas_used += tx.gas_used

        return tx, gas_used

    def signupTx(self, username: str) -> network.transaction.TransactionReceipt:
        # check isValidUsername
        if not isValidUsername(username):
            return None, None

        tx = self.contract.signup(username, {"from": self.account})
        tx.wait(1)

        success = tx.return_value

        if not success:
            return None, None
        return tx, tx.gas_used

    def listUsersTx(self) -> List[str]:
        users = list(self.contract.listUsers())
        users.sort()

        return users

    def tribsTx(self, username: str):
        if not isValidUsername(username):
            return None

        tribs = list(self.contract.tribs(username))
        tribs = [tuple(trib) for trib in tribs]

        tribs = sorted(
            tribs, key=lambda trib: (-trib[3], trib[4], trib[2], trib[1], trib[0])
        )

        # check length of tribs
        if len(tribs) > MAX_TRIB_FETCH:
            tribs = tribs[:MAX_TRIB_FETCH]

        return tribs

    def isFollowingTx(self, who: str, whom: str) -> bool:
        if not isValidUsername(who) or not isValidUsername(whom):
            return None

        followingList = self.followingTx(who)
        return whom in followingList

    def followingTx(self, username: str) -> List[str]:
        if not isValidUsername(username):
            return None

        followUnfollowLog = list(self.contract.following(username))
        # print(followUnfollowLog)

        followListSet = set()

        for log_i in followUnfollowLog:
            if log_i[0] == True:  # follow op
                followListSet.add(log_i[1])
            elif log_i[0] == False:  # unfollow op
                followListSet.remove(log_i[1])

        # followList = [tuple(follow)[2] for follow in followList]

        return list(followListSet)

    def homeTx(self, username: str) -> network.transaction.TransactionReceipt:
        if not isValidUsername(username):
            return None

        # bring in the entire home functionality

        # get own tribs
        homeList = list(self.tribsTx(username))

        # get following list
        followingList = self.followingTx(username)

        for followedUser in followingList:
            userTribs = self.contract.tribs(followedUser)

            if len(userTribs) != 0:
                homeList.extend(userTribs)

        # homeList = list(self.contract.home(username))
        # homeList = [tuple(trib) for trib in homeList]

        # print(homeList)

        homeList = sorted(
            homeList, key=lambda trib: (-trib[3], trib[4], trib[2], trib[1], trib[0])
        )

        # check length of homeList
        if len(homeList) > MAX_TRIB_FETCH:
            homeList = homeList[:MAX_TRIB_FETCH]

        return homeList


def deploy_tribbler():

    network.gas_price("50 gwei")

    tribbler = TribblerMain(accounts[5])
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

    tribbler.postTx("harsh", "first test trib")

    tribbler.postTx("raghav", "this is my 2nd trib")

    _, gas_used, isConcurrentSuccessful = tribbler.followTx("raghav", "harsh")
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

    followingList = tribbler.followingTx("harsh")
    print(f"Harsh is following: {followingList}")

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

    _, gas_used, isConcurrentSuccessful = tribbler.unfollowTx("raghav", "harsh")
    tx_types_gas_used.update({"unfollowTx": gas_used})
    total_gas_used += gas_used

    followingList = tribbler.followingTx("raghav")
    print(f"Raghav is following: {followingList}")

    _, gas_used, isConcurrentSuccessful = tribbler.followTx("raghav", "harsh")

    isFollowing = tribbler.isFollowingTx("raghav", "harsh")
    print(f"Raghav is following Harsh: {isFollowing}")

    print(tx_types_gas_used)
    print(f"init gas: {tribbler.init_gas_used}")


def main():
    # deploy_tribbler()
    tribbler = TribblerMain(accounts[6])

    print(tribbler.getContractAddress())
