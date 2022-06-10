from typing import List
import time
from brownie import (
    accounts,
    config,
    Tribbler,
    # Utils,
    User,
    network,
)
from .constants import *
from .utils import *


class TribblerMain:
    def __init__(self, account, tribblerAddr=None):
        self.account = account
        self.init_gas_used = 0

        # contract = String.deploy({"from": self.account})
        # self.init_gas_used += contract.tx.gas_used

        # contract = Tribs.deploy({"from": self.account})
        # self.init_gas_used += contract.tx.gas_used

        # if utilsAddr is None:
        #     self.utils_contract = Utils.deploy({"from": self.account})
        #     self.init_gas_used += self.utils_contract.tx.gas_used
        # else:
        #     self.utils_contract = Utils.at(utilsAddr)

        if tribblerAddr is None:
            self.contract = Tribbler.deploy({"from": self.account})
            self.init_gas_used += self.contract.tx.gas_used
        else:
            self.contract = Tribbler.at(tribblerAddr)

    def getContractAddress(self):
        return {
            # "utils_contract": self.utils_contract.address,
            "tribbler_contract": self.contract.address,
        }

    # def isUserExists(self, username: str) -> bool:
    #     print(self.contract.isUserExists(username))

    def getUserContract(self, username: str):
        # check username is valid before calling this
        # check isValidUsername
        if not isValidUsername(username):
            return None

        # check if user exists
        if not self.contract.isUserExists(username):
            # print(self.contract.isUserExists(username))
            return None

        userContractAddr = self.contract.getUserContractAddr(username)

        userContractAddr = (
            "0x" + userContractAddr
        )  # prepend 0x which is not stored in tribbler contract string
        # print(userContractAddr)

        userContract = User.at(userContractAddr)

        return userContract

    def signupTx(self, username: str) -> network.transaction.TransactionReceipt:
        # check isValidUsername
        if not isValidUsername(username):
            return None, None

        # check if user exists
        if self.contract.isUserExists(username):
            return None

        # create user contract
        userContract = User.deploy(username, {"from": self.account})
        print(type(userContract))
        # print(userContract.address)

        userContractAddr = userContract.address

        # update address of user contract in tribbler contract
        tx = self.contract.signup(
            username, userContractAddr[2:], {"from": self.account}
        )
        tx.wait(1)

        # success = tx.return_value

        # if not success:
        #     return None, None
        return tx, tx.gas_used + userContract.tx.gas_used

    def listUsersTx(self) -> List[str]:
        users = list(self.contract.listUsers())
        users.sort()

        return users

    def postTx(self, who: str, message: str) -> network.transaction.TransactionReceipt:
        if isLongTrib(message):
            return None, None

        if not isValidUsername(who):
            return None, None

        # get user contract
        userContract = self.getUserContract(who)
        # error check
        if userContract is None:
            return None

        gas_used = 0
        # tx = self.contract.post(who, message, {"from": self.account})
        tx = userContract.post(message, {"from": self.account})
        tx.wait(1)
        # success = tx.return_value

        # if not success:
        #     return None

        tx_index = tx.txindex
        timestamp = int(time.time())
        block_num = tx.block_number

        gas_used += tx.gas_used

        # tx = self.contract.addTrib(
        #     who, message, timestamp, block_num, tx_index, {"from": self.account}
        # )
        tx = userContract.addTrib(
            message, timestamp, block_num, tx_index, {"from": self.account}
        )
        tx.wait(1)
        gas_used += tx.gas_used

        return tx, gas_used

    def tribsTx(self, username: str):
        if not isValidUsername(username):
            return None

        # get user contract
        userContract = self.getUserContract(username)
        # error check
        if userContract is None:
            return None

        # tribs = list(self.contract.tribs(username))
        tribs = list(userContract.tribs())
        tribs = [tuple(trib) for trib in tribs]

        tribs = sorted(
            tribs, key=lambda trib: (-trib[3], trib[4], trib[2], trib[1], trib[0])
        )

        # check length of tribs
        if len(tribs) > MAX_TRIB_FETCH:
            tribs = tribs[:MAX_TRIB_FETCH]

        return tribs

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
            return None, None, None

        if whoWhomSame(who, whom):
            return None, None, None

        if not self.contract.isUserExists(who) or not self.contract.isUserExists(whom):
            return None, None, None

        followingList = self.followingTx(who)

        if len(followingList) >= MAX_FOLLOWING:
            # following too many people. equal to check makes sure that if max following then this also won't get appended to the log
            return None, None, None

        if isFollow and whom in followingList:
            # already following
            return None, None, None

        if not isFollow and whom not in followingList:
            # already not following
            return None, None, None

        # get user contract
        userContract = self.getUserContract(who)
        # error check
        if userContract is None:
            return None

        gas_used = 0
        # tx = self.contract.followOrUnfollow(who, whom, {"from": self.account})
        tx = userContract.followOrUnfollow(who, whom, {"from": self.account})
        tx.wait(1)
        # success = tx.return_value

        # if not success:
        #     return None

        tx_hash = tx.txid[2:]
        gas_used += tx.gas_used

        # tx = self.contract.appendToFollowUnfollowLog(
        #     isFollow, who, whom, tx_hash, {"from": self.account}
        # )
        tx = userContract.appendToFollowUnfollowLog(
            isFollow, whom, tx_hash, {"from": self.account}
        )
        tx.wait(1)
        gas_used += tx.gas_used

        # again go through the log and check if this succeeded
        # followUnfollowLog = list(self.contract.following(who))
        followUnfollowLog = list(userContract.following())

        # iterate from start and look for hash.
        for log_i in followUnfollowLog:
            if log_i[2] == tx_hash:  # 2nd index is tx_hash
                return tx, gas_used, True
            else:
                return tx, gas_used, True

        # return tx, gas_used

    def isFollowingTx(self, who: str, whom: str) -> bool:
        if not isValidUsername(who) or not isValidUsername(whom):
            return None

        followingList = self.followingTx(who)
        return whom in followingList

    def followingTx(self, username: str) -> List[str]:
        if not isValidUsername(username):
            return None

        # get user contract
        userContract = self.getUserContract(username)
        # error check
        if userContract is None:
            return None

        # followUnfollowLog = list(self.contract.following(username))
        followUnfollowLog = list(userContract.following())
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
            # userTribs = self.contract.tribs(followedUser)
            userTribs = list(self.tribsTx(followedUser))

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

    account = accounts[0]

    tribbler = TribblerMain(account)
    # account = accounts.load("test-account1")

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

    # tribbler.signupTx("rajdeep")

    _, gas_used = tribbler.postTx("raghav", "hello world, I am raghav")
    tx_types_gas_used.update({"postTx": gas_used})
    total_gas_used += gas_used

    tribbler.postTx("harsh", "first test trib")

    # tribbler.postTx("raghav", "this is my 2nd trib")

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


def test_tribbler():
    network.gas_price("50 gwei")

    tribbler = TribblerMain(accounts[5])

    usernames = ["raghav", "harsh", "rajdeep"]

    for username in usernames:
        # tribbler.isUserExists(username)
        tribbler.signupTx(username)
        # tribbler.isUserExists(username)
        # tribbler.getUserContract(username)

        # userContract = tribbler.getUserContract(username)
        # if userContract is not None:
        #     print(userContract.getUsername())

    print(tribbler.listUsersTx())

    # test post and tribs
    for username in usernames:
        for i in range(5):  # post 5 tribs per user
            tribbler.postTx(username, "trib" + str(i))

        print(tribbler.tribsTx(username))


def main():
    deploy_tribbler()
    # test_tribbler()

    # tribbler = TribblerMain(accounts[6])
    # print(tribbler.getContractAddress())

    # deploy to ropsten
    # network.gas_price("50 gwei")
    # account = accounts.load("test-account1")
    # tribbler = TribblerMain(account)
    # print(tribbler.getContractAddress())
