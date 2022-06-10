from typing import List, Tuple
import time
from brownie import (
    accounts,
    Tribbler,
    User,
    network,
)
from .constants import *
from .utils import *


class TribblerMain:
    def __init__(
        self, account: network.account.Account, tribblerAddr: str = None
    ) -> None:
        self.account = account
        self.init_gas_used = 0

        if tribblerAddr is None:
            self.contract = Tribbler.deploy({"from": self.account})
            self.init_gas_used += self.contract.tx.gas_used
        else:
            self.contract = Tribbler.at(tribblerAddr)

    def getContractAddress(self) -> str:
        return self.contract.address

    def getUserContract(self, username: str) -> network.contract.ProjectContract:
        # check username is valid before calling this
        # check isValidUsername
        if not isValidUsername(username):
            return None

        # check if user exists
        if not self.contract.isUserExists(username):
            return None

        userContractAddr = self.contract.getUserContractAddr(username)

        userContractAddr = (
            "0x" + userContractAddr
        )  # prepend 0x which is not stored in tribbler contract string
        # print(userContractAddr)

        userContract = User.at(userContractAddr)

        return userContract

    def signupTx(
        self, username: str
    ) -> Tuple[network.transaction.TransactionReceipt, int]:
        # check isValidUsername
        if not isValidUsername(username):
            return None, None

        # check if user exists
        if self.contract.isUserExists(username):
            return None, None

        # create user contract
        userContract = User.deploy(username, {"from": self.account})

        userContractAddr = userContract.address

        # update address of user contract in tribbler contract
        tx = self.contract.signup(
            username, userContractAddr[2:], {"from": self.account}
        )
        tx.wait(1)

        return tx, tx.gas_used + userContract.tx.gas_used

    def listUsersTx(self) -> List[str]:
        users = list(self.contract.listUsers())
        users.sort()

        return users

    def postTx(
        self, who: str, message: str
    ) -> Tuple[network.transaction.TransactionReceipt, int]:
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
        tx = userContract.post(message, {"from": self.account})
        tx.wait(1)

        tx_index = tx.txindex
        timestamp = int(time.time())
        block_num = tx.block_number

        gas_used += tx.gas_used

        tx = userContract.addTrib(
            message, timestamp, block_num, tx_index, {"from": self.account}
        )
        tx.wait(1)
        gas_used += tx.gas_used

        return tx, gas_used

    def tribsTx(self, username: str) -> Tuple[str, str, int, int, int]:
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

    def followTx(
        self, who: str, whom: str
    ) -> Tuple[network.transaction.TransactionReceipt, int, bool]:
        tx, gas_used, isConcurrentSuccessful = self.followOrUnfollowTx(True, who, whom)

        return tx, gas_used, isConcurrentSuccessful

    def unfollowTx(
        self, who: str, whom: str
    ) -> Tuple[network.transaction.TransactionReceipt, int, bool]:
        tx, gas_used, isConcurrentSuccessful = self.followOrUnfollowTx(False, who, whom)

        return tx, gas_used, isConcurrentSuccessful

    def followOrUnfollowTx(
        self, isFollow: bool, who: str, whom: str
    ) -> Tuple[network.transaction.TransactionReceipt, int, bool]:
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
        tx = userContract.followOrUnfollow(who, whom, {"from": self.account})
        tx.wait(1)

        tx_hash = tx.txid[2:]
        gas_used += tx.gas_used

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

        followUnfollowLog = list(userContract.following())

        followListSet = set()

        for log_i in followUnfollowLog:
            if log_i[0] == True:  # follow op
                followListSet.add(log_i[1])
            elif log_i[0] == False:  # unfollow op
                followListSet.remove(log_i[1])

        return list(followListSet)

    def homeTx(self, username: str) -> Tuple[str, str, int, int, int]:
        if not isValidUsername(username):
            return None

        # get own tribs
        homeList = list(self.tribsTx(username))

        # get following list
        followingList = self.followingTx(username)

        for followedUser in followingList:
            userTribs = list(self.tribsTx(followedUser))

            if len(userTribs) != 0:
                homeList.extend(userTribs)

        homeList = sorted(
            homeList, key=lambda trib: (-trib[3], trib[4], trib[2], trib[1], trib[0])
        )

        # check length of homeList
        if len(homeList) > MAX_TRIB_FETCH:
            homeList = homeList[:MAX_TRIB_FETCH]

        return homeList


def deploy_tribbler() -> None:
    network.gas_price("50 gwei")

    account = accounts[0]

    tribbler = TribblerMain(account)

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

    tribbler.signupTx("rajdeep")

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

    followingList = tribbler.followingTx("raghav")
    print(f"Raghav is following: {followingList}")

    followingList = tribbler.followingTx("harsh")
    print(f"Harsh is following: {followingList}")

    isFollowing = tribbler.isFollowingTx("raghav", "harsh")
    print(f"Raghav is following Harsh: {isFollowing}")

    users = tribbler.listUsersTx()
    print(f"All users: {users}")

    tribs = tribbler.tribsTx("raghav")
    print(f"Raghav's tribs: {tribs}")

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


def test_tribbler() -> None:
    network.gas_price("50 gwei")

    tribbler = TribblerMain(accounts[5])

    usernames = ["raghav", "harsh", "rajdeep"]

    for username in usernames:
        tribbler.signupTx(username)

    print(tribbler.listUsersTx())

    # test post and tribs
    for username in usernames:
        for i in range(5):  # post 5 tribs per user
            tribbler.postTx(username, "trib" + str(i))

        print(tribbler.tribsTx(username))


def main():
    deploy_tribbler()


if __name__ == "__main__":
    main()
