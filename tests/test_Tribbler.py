from brownie import Tribbler, Utils, Tribs, String, accounts, reverts
import time


# # def test_signup1():
# #     account = accounts[0]

# #     # arrange
# #     String.deploy({"from": account})
# #     Tribs.deploy({"from": account})
# #     Utils.deploy({"from": account})
# #     tribbler = Tribbler.deploy({"from": account})

# #     # act
# #     test_username = "u1"
# #     output = tribbler.signup(test_username)
# #     output.wait(1)
# #     # print(type(output))
# #     # expected_output = True

# #     # list_usernames = tribbler.usernames
# #     # print(list_usernames[0])

# #     # assert
# #     # assert type(output) == expected_output


# def test_signup2():
#     account = accounts[0]

#     # arrange
#     String.deploy({"from": account})
#     Tribs.deploy({"from": account})
#     Utils.deploy({"from": account})
#     tribbler = Tribbler.deploy({"from": account})

#     # act
#     test_username = "1u"

#     with reverts("Username is invalid"):
#         tribbler.signup(test_username)


# def test_signup3():
#     account = accounts[0]

#     # arrange
#     String.deploy({"from": account})
#     Tribs.deploy({"from": account})
#     Utils.deploy({"from": account})
#     tribbler = Tribbler.deploy({"from": account})

#     # act
#     test_username = "uV"
#     with reverts("Username is invalid"):
#         tribbler.signup(test_username)


# def test_signup4():
#     account = accounts[0]

#     # arrange
#     String.deploy({"from": account})
#     Tribs.deploy({"from": account})
#     Utils.deploy({"from": account})
#     tribbler = Tribbler.deploy({"from": account})

#     # act
#     test_username = "u1"
#     tribbler.signup(test_username)

#     with reverts("User already exists"):
#         tribbler.signup(test_username)


# def test_listUsers():
#     account = accounts[0]

#     # arrange
#     String.deploy({"from": account})
#     Tribs.deploy({"from": account})
#     Utils.deploy({"from": account})
#     tribbler = Tribbler.deploy({"from": account})

#     # act
#     tribbler.signup("u3")
#     # tx.wait(1)
#     # print(tx.return_value)

#     tribbler.signup("u2")
#     # tx.wait(1)
#     # print(tx.return_value)

#     tribbler.signup("u1")
#     # tx.wait(1)
#     # print(tx.return_value)

#     list_users = tribbler.listUsers()
#     # print(list_users.info())

#     assert list_users.return_value == ["u1", "u2", "u3"]


##### sort
# def test_sort():
#     account = accounts[0]

#     # arrange
#     String.deploy({"from": account})
#     Tribs.deploy({"from": account})
#     Utils.deploy({"from": account})
#     tribbler = Tribbler.deploy({"from": account})

#     # print(type(utils_obj), Utils, Utils[0].info())
#     # print(utils_obj.abi)

#     # act
#     test_arr = ["a", "p", "b", "q", "c", "r"]
#     output = tribbler.bubbleSort(test_arr)
#     # print(output)

#     expected_output = ["a", "b", "c", "p", "q", "r"]

#     # print(output.return_value)

#     # assert
#     assert output == expected_output


# def test_post():
#     account = accounts[0]

#     # arrange
#     String.deploy({"from": account})
#     Tribs.deploy({"from": account})
#     Utils.deploy({"from": account})
#     tribbler = Tribbler.deploy({"from": account})

#     # act
#     tribbler.signup("u1")
#     # tribbler.signup("u2")
#     # tribbler.signup("u3")

#     who = "u1"
#     message = "testtrib1"

#     tx = tribbler.post(who, message)
#     # tx.wait(1)

#     tx_index = tx.txindex
#     timestamp = int(time.time())
#     block_num = tx.block_number

#     tx = tribbler.addTrib(who, message, timestamp, block_num, tx_index)
#     # tx.wait(1)

#     time.sleep(1)

#     who = "u1"
#     message = "testtrib2"

#     tx = tribbler.post(who, message)
#     # tx.wait(1)

#     tx_index = tx.txindex
#     timestamp = int(time.time())
#     block_num = tx.block_number

#     tx = tribbler.addTrib(who, message, timestamp, block_num, tx_index)
#     # tx.wait(1)

#     time.sleep(1)

#     who = "u1"
#     message = "testtrib0"

#     tx = tribbler.post(who, message)
#     # tx.wait(1)

#     tx_index = tx.txindex
#     timestamp = int(time.time())
#     block_num = tx.block_number

#     tx = tribbler.addTrib(who, message, timestamp, block_num, tx_index)
#     # tx.wait(1)

#     who = "u1"
#     tx = tribbler.tribs(who)
#     # tx.wait(1)

#     print(tx.return_value)

# listTribs = [trib_obj[1] for trib_obj in tx.return_value]

# assert listTribs == [
#     "testtrib0",
#     "testtrib2",
#     "testtrib1",
# ]  # posting order was 1,2,0 so listing should be in reverse sorted order i.e. 0,2,1


# def test_home():
#     account = accounts[0]

#     # arrange
#     String.deploy({"from": account})
#     Tribs.deploy({"from": account})
#     Utils.deploy({"from": account})
#     tribbler = Tribbler.deploy({"from": account})

#     # act
#     tribbler.signup("u1")
#     # tribbler.signup("u2")
#     # tribbler.signup("u3")

#     who = "u1"
#     message = "testtrib1"

#     tx = tribbler.post(who, message)
#     # tx.wait(1)

#     tx_index = tx.txindex
#     timestamp = int(time.time())
#     block_num = tx.block_number

#     tx = tribbler.addTrib(who, message, timestamp, block_num, tx_index)
#     # tx.wait(1)

#     time.sleep(1)

#     who = "u1"
#     message = "testtrib2"

#     tx = tribbler.post(who, message)
#     # tx.wait(1)

#     tx_index = tx.txindex
#     timestamp = int(time.time())
#     block_num = tx.block_number

#     tx = tribbler.addTrib(who, message, timestamp, block_num, tx_index)
#     # tx.wait(1)

#     time.sleep(1)

#     who = "u1"
#     message = "testtrib0"

#     tx = tribbler.post(who, message)
#     # tx.wait(1)

#     tx_index = tx.txindex
#     timestamp = int(time.time())
#     block_num = tx.block_number

#     tx = tribbler.addTrib(who, message, timestamp, block_num, tx_index)
#     # tx.wait(1)

#     tx = tribbler.home(who)
#     # tx.wait(1)

#     print(tx.return_value)

#     listTribs = [trib_obj[1] for trib_obj in tx.return_value]

#     assert listTribs == [
#         "testtrib0",
#         "testtrib2",
#         "testtrib1",
#     ]  # posting order was 1,2,0 so listing should be in reverse sorted order i.e. 0,2,1


# TODO: test post and tribs with multiple users


# def test_follow_following():
#     account = accounts[0]

#     # arrange
#     String.deploy({"from": account})
#     Tribs.deploy({"from": account})
#     Utils.deploy({"from": account})
#     tribbler = Tribbler.deploy({"from": account})

#     # act
#     tribbler.signup("u1")
#     tribbler.signup("u2")
#     tribbler.signup("u3")

#     who = "u1"
#     whom = "u2"
#     tx = tribbler.followOrUnfollow(who, whom)
#     # tx.wait(1)
#     # success = tx.return_value

#     # if not success:
#     #     return None

#     tx_hash = tx.txid
#     tx_hash = tx_hash[2:]
#     # print(type(tx_hash), tx_hash)

#     tx = tribbler.appendToFollowUnfollowLog(True, who, whom, tx_hash)
#     # tx.wait(1)

#     who = "u1"
#     whom = "u3"
#     tx = tribbler.followOrUnfollow(who, whom)
#     # tx.wait(1)
#     # success = tx.return_value

#     # if not success:
#     #     return None

#     tx_hash = tx.txid
#     tx_hash = tx_hash[2:]
#     # print(type(tx_hash), tx_hash)

#     tx = tribbler.appendToFollowUnfollowLog(True, who, whom, tx_hash)
#     # tx.wait(1)

#     who = "u2"
#     whom = "u3"
#     tx = tribbler.followOrUnfollow(who, whom)
#     # tx.wait(1)
#     # success = tx.return_value

#     # if not success:
#     #     return None

#     tx_hash = tx.txid
#     tx_hash = tx_hash[2:]
#     # print(type(tx_hash), tx_hash)

#     tx = tribbler.appendToFollowUnfollowLog(True, who, whom, tx_hash)
#     # tx.wait(1)

#     who = "u2"
#     whom = "u1"
#     tx = tribbler.followOrUnfollow(who, whom)
#     # tx.wait(1)
#     # success = tx.return_value

#     # if not success:
#     #     return None

#     tx_hash = tx.txid
#     tx_hash = tx_hash[2:]
#     # print(type(tx_hash), tx_hash)

#     tx = tribbler.appendToFollowUnfollowLog(True, who, whom, tx_hash)
#     # tx.wait(1)

#     username = "u2"
#     tx = tribbler.following(username)
#     # tx.wait(1)

#     print(tx.return_value)

#     assert tx.return_value == ["u3", "u1"]


# def test_follow():
#     account = accounts[0]

#     # arrange
#     String.deploy({"from": account})
#     Tribs.deploy({"from": account})
#     Utils.deploy({"from": account})
#     tribbler = Tribbler.deploy({"from": account})

#     # act
#     tribbler.signup("u1")

# with reverts("User does not exist"):
#     who = "u1"
#     whom = "u2"
#     tribbler.followOrUnfollow(who, whom)

# with reverts("Username is invalid"):
#     who = "u1"
#     whom = "2u"
#     tribbler.followOrUnfollow(who, whom)

#     with reverts("Both the usernames are the same"):
#         who = "u1"
#         whom = "u1"
#         tribbler.followOrUnfollow(who, whom)


# def test_follow_unfollow_allOps():
#     account = accounts[0]

#     # arrange
#     String.deploy({"from": account})
#     Tribs.deploy({"from": account})
#     Utils.deploy({"from": account})
#     tribbler = Tribbler.deploy({"from": account})

#     # act
#     tribbler.signup("u1")
#     tribbler.signup("u2")
#     tribbler.signup("u3")
#     tribbler.signup("u4")

#     who = "u1"
#     whom = "u2"
#     tx = tribbler.followOrUnfollow(who, whom)
#     # tx.wait(1)
#     # success = tx.return_value

#     # if not success:
#     #     return None

#     tx_hash = tx.txid
#     tx_hash = tx_hash[2:]
#     # print(type(tx_hash), tx_hash)

#     tx = tribbler.appendToFollowUnfollowLog(True, who, whom, tx_hash)
#     # tx.wait(1)

#     who = "u1"
#     whom = "u3"
#     tx = tribbler.followOrUnfollow(who, whom)
#     # tx.wait(1)
#     # success = tx.return_value

#     # if not success:
#     #     return None

#     tx_hash = tx.txid
#     tx_hash = tx_hash[2:]
#     # print(type(tx_hash), tx_hash)

#     tx = tribbler.appendToFollowUnfollowLog(True, who, whom, tx_hash)
#     # tx.wait(1)

#     who = "u2"
#     whom = "u3"
#     tx = tribbler.followOrUnfollow(who, whom)
#     # tx.wait(1)
#     # success = tx.return_value

#     # if not success:
#     #     return None

#     tx_hash = tx.txid
#     tx_hash = tx_hash[2:]
#     # print(type(tx_hash), tx_hash)

#     tx = tribbler.appendToFollowUnfollowLog(True, who, whom, tx_hash)
#     # tx.wait(1)

#     who = "u2"
#     whom = "u1"
#     tx = tribbler.followOrUnfollow(who, whom)
#     # tx.wait(1)
#     # success = tx.return_value

#     # if not success:
#     #     return None

#     tx_hash = tx.txid
#     tx_hash = tx_hash[2:]
#     # print(type(tx_hash), tx_hash)

#     tx = tribbler.appendToFollowUnfollowLog(True, who, whom, tx_hash)
#     # tx.wait(1)

#     who = "u2"
#     whom = "u4"
#     tx = tribbler.followOrUnfollow(who, whom)
#     # tx.wait(1)
#     # success = tx.return_value

#     # if not success:
#     #     return None

#     tx_hash = tx.txid
#     tx_hash = tx_hash[2:]
#     # print(type(tx_hash), tx_hash)

#     tx = tribbler.appendToFollowUnfollowLog(True, who, whom, tx_hash)
#     # tx.wait(1)

#     who = "u2"
#     whom = "u1"
#     tx = tribbler.followOrUnfollow(who, whom)
#     # tx.wait(1)
#     # success = tx.return_value

#     # if not success:
#     #     return None

#     tx_hash = tx.txid
#     tx_hash = tx_hash[2:]
#     # print(type(tx_hash), tx_hash)

#     tx = tribbler.appendToFollowUnfollowLog(True, who, whom, tx_hash)
#     # tx.wait(1)

#     assert tx.return_value == False  # already following

#     who = "u2"
#     whom = "u3"
#     tx = tribbler.followOrUnfollow(who, whom)
#     # tx.wait(1)
#     # success = tx.return_value

#     # if not success:
#     #     return None

#     tx_hash = tx.txid
#     tx_hash = tx_hash[2:]
#     # print(type(tx_hash), tx_hash)

#     tx = tribbler.appendToFollowUnfollowLog(False, who, whom, tx_hash)
#     # tx.wait(1)

#     who = "u2"
#     whom = "u3"
#     tx = tribbler.followOrUnfollow(who, whom)
#     # tx.wait(1)
#     # success = tx.return_value

#     # if not success:
#     #     return None

#     tx_hash = tx.txid
#     tx_hash = tx_hash[2:]
#     # print(type(tx_hash), tx_hash)

#     tx = tribbler.appendToFollowUnfollowLog(False, who, whom, tx_hash)
#     # tx.wait(1)

#     assert tx.return_value == False  # already unfollowed

#     username = "u2"
#     tx = tribbler.following(username)
#     # tx.wait(1)

#     # print(tx.return_value)

#     assert tx.return_value == ["u4", "u1"]

#     who = "u1"
#     whom = "u2"
#     tx = tribbler.followOrUnfollow(who, whom)
#     # tx.wait(1)
#     # success = tx.return_value

# if not success:
#     return None

# tx_hash = tx.txid
# tx_hash = tx_hash[2:]
# # print(type(tx_hash), tx_hash)

# tx = tribbler.appendToFollowUnfollowLog(False, who, whom, tx_hash)

#     who = "u1"
#     whom = "u2"
#     tx = tribbler.isFollowing(who, whom)
#     # tx.wait(1)

#     # print(tx.return_value)

#     assert tx.return_value == False

#     who = "u1"
#     whom = "u3"
#     tx = tribbler.following(who)
#     # tx.wait(1)

#     print(tx.return_value)

#     assert tx.return_value == ["u3"]

#     who = "u1"
#     whom = "u3"
#     tx = tribbler.isFollowing(who, whom)
#     # tx.wait(1)

#     # print(tx.return_value)

#     assert tx.return_value == True


# def test_isFollowing():
#     pass


# def test_followingList():
#     pass


def test_post_multiple_users():
    account = accounts[0]

    # arrange
    String.deploy({"from": account})
    Tribs.deploy({"from": account})
    Utils.deploy({"from": account})
    tribbler = Tribbler.deploy({"from": account})

    users = ["u1", "u2", "u3"]
    # "u4"]

    # act
    for user in users:
        tribbler.signup(user)

    for i in range(2 * len(users)):
        who = users[i % len(users)]
        message = "trib" + str(i)
        tx = tribbler.post(who, message)
        # tx.wait(1)

        tx_index = tx.txindex
        timestamp = int(time.time())
        block_num = tx.block_number

        tx = tribbler.addTrib(who, message, timestamp, block_num, tx_index)
        # tx.wait(1)

    # tx = tribbler.home("u1")
    # # tx.wait(1)
    # print(tx.return_value)
    # assert False

    for user in users:
        tx = tribbler.home(user)
        tx.wait(1)
        print(tx.return_value)
        listTribs = [trib_obj[1] for trib_obj in tx.return_value]

        assert len(listTribs) == 2
        assert listTribs[0] > listTribs[1]


def test_multiple_follow_multiple_post():
    account = accounts[0]

    # arrange
    String.deploy({"from": account})
    Tribs.deploy({"from": account})
    Utils.deploy({"from": account})
    tribbler = Tribbler.deploy({"from": account})

    users = ["u1", "u2"]

    # act
    for user in users:
        tribbler.signup(user)

    for i in range(2 * len(users)):
        who = users[i % len(users)]
        message = "trib" + str(i)
        tx = tribbler.post(who, message)
        # tx.wait(1)

        tx_index = tx.txindex
        timestamp = int(time.time())
        block_num = tx.block_number

        tx = tribbler.addTrib(who, message, timestamp, block_num, tx_index)

    who_whom = [("u1", "u2")]
    # , ("u2", "u3"), ("u1", "u3")]

    for who, whom in who_whom:
        tx = tribbler.followOrUnfollow(who, whom)
        tx_hash = tx.txid
        tx_hash = tx_hash[2:]
        # print(type(tx_hash), tx_hash)

        tx = tribbler.appendToFollowUnfollowLog(True, who, whom, tx_hash)

    # u1 -> trib0, trib2
    # u2 -> trib1, trib3

    tx = tribbler.home("u1")
    tx.wait(1)
    listTribs = [trib_obj[1] for trib_obj in tx.return_value]

    assert len(listTribs) == 4
    assert listTribs == ["trib" + str(i) for i in range(3, -1, -1)]

    tx = tribbler.home("u2")
    tx.wait(1)
    listTribs = [trib_obj[1] for trib_obj in tx.return_value]

    assert len(listTribs) == 2
    assert listTribs == ["trib3", "trib1"]
