from . import deploy
from brownie import accounts, Tribbler, reverts
import time


def test_signup1():

    tribbler = deploy.TribblerMain(accounts[6])

    test_username = "u1"
    tx, _ = tribbler.signupTx(test_username)

    expected_output = True

    assert tx.return_value == expected_output


def test_signup2():
    tribbler = deploy.TribblerMain(accounts[6])

    test_username = "1u"
    ret, _ = tribbler.signupTx(test_username)

    assert ret == None


def test_signup3():
    tribbler = deploy.TribblerMain(accounts[6])

    test_username = "uV"
    ret, _ = tribbler.signupTx(test_username)

    assert ret == None


def test_signup4():
    tribbler = deploy.TribblerMain(accounts[6])

    test_username = "u1"

    tribbler.signupTx(test_username)

    ret, _ = tribbler.signupTx(test_username)

    assert ret == None


def test_listUsers():
    tribbler = deploy.TribblerMain(accounts[6])

    tribbler.signupTx("u3")
    tribbler.signupTx("u2")
    tribbler.signupTx("u1")

    list_users = tribbler.listUsersTx()

    assert list_users == ["u1", "u2", "u3"]


def test_noUsers():
    account = accounts[0]

    tribbler = Tribbler.deploy({"from": account})

    with reverts("No users exist"):
        tribbler.listUsers()


def test_minListUser():
    tribbler = deploy.TribblerMain(accounts[6])

    for i in range(25, -1, -1):
        username = "u" + str(i)
        tribbler.signupTx(username)

    listUsers = tribbler.listUsersTx()

    listOfUsers = ["u" + str(i) for i in range(6, 26)]
    listOfUsers = sorted(listOfUsers)

    assert len(listUsers) == 20

    assert listUsers == listOfUsers


def test_maxFollowing():
    tribbler = deploy.TribblerMain(accounts[6])

    for i in range(25, -1, -1):
        username = "u" + str(i)
        tribbler.signupTx(username)

    for j in range(1, 21):
        who = "u0"
        whom = "u" + str(j)

        tribbler.followOrUnfollowTx(True, who, whom)

    username = "u0"
    followingList = tribbler.followingTx(username)

    assert len(followingList) == 20


def test_post():
    tribbler = deploy.TribblerMain(accounts[6])

    tribbler.signupTx("u1")

    who = "u1"
    message = "testtrib1"

    tribbler.postTx(who, message)

    time.sleep(1)

    who = "u1"
    message = "testtrib2"

    tribbler.postTx(who, message)

    time.sleep(1)

    who = "u1"
    message = "testtrib0"

    tribbler.postTx(who, message)

    who = "u1"
    tribs = tribbler.tribsTx(who)

    listTribs = [trib_obj[1] for trib_obj in tribs]

    assert listTribs == [
        "testtrib0",
        "testtrib2",
        "testtrib1",
    ]  # posting order was 1,2,0 so listing should be in reverse sorted order i.e. 0,2,1


def test_home():
    tribbler = deploy.TribblerMain(accounts[6])

    tribbler.signupTx("u1")

    who = "u1"
    message = "testtrib1"

    tribbler.postTx(who, message)

    who = "u1"
    message = "testtrib2"

    tribbler.postTx(who, message)

    time.sleep(1)

    who = "u1"
    message = "testtrib0"

    tribbler.postTx(who, message)

    home = tribbler.homeTx(who)

    listTribs = [trib_obj[1] for trib_obj in home]

    assert listTribs == [
        "testtrib0",
        "testtrib2",
        "testtrib1",
    ]  # posting order was 1,2,0 so listing should be in reverse sorted order i.e. 0,2,1


def test_follow_following():
    tribbler = deploy.TribblerMain(accounts[6])

    tribbler.signupTx("u1")
    tribbler.signupTx("u2")
    tribbler.signupTx("u3")

    who = "u1"
    whom = "u2"
    tribbler.followOrUnfollowTx(True, who, whom)

    who = "u1"
    whom = "u3"
    tribbler.followOrUnfollowTx(True, who, whom)

    who = "u2"
    whom = "u3"
    tribbler.followOrUnfollowTx(True, who, whom)

    who = "u2"
    whom = "u1"
    tribbler.followOrUnfollowTx(True, who, whom)

    username = "u2"
    following_list = tribbler.followingTx(username)

    assert following_list == ["u1", "u3"]


def test_follow():
    tribbler = deploy.TribblerMain(accounts[6])

    tribbler.signupTx("u1")

    who = "u1"
    whom = "u2"
    _, _, success = tribbler.followOrUnfollowTx(True, who, whom)

    assert success == False

    who = "u1"
    whom = "2u"
    _, _, success = tribbler.followOrUnfollowTx(True, who, whom)

    assert success == False

    who = "u1"
    whom = "u1"
    _, _, success = tribbler.followOrUnfollowTx(True, who, whom)

    assert success == False


def test_follow_unfollow_allOps():
    tribbler = deploy.TribblerMain(accounts[6])

    tribbler.signupTx("u1")
    tribbler.signupTx("u2")
    tribbler.signupTx("u3")
    tribbler.signupTx("u4")

    who = "u1"
    whom = "u2"
    tribbler.followOrUnfollowTx(True, who, whom)

    who = "u1"
    whom = "u3"
    tribbler.followOrUnfollowTx(True, who, whom)

    who = "u2"
    whom = "u3"
    tribbler.followOrUnfollowTx(True, who, whom)

    who = "u2"
    whom = "u1"
    tribbler.followOrUnfollowTx(True, who, whom)

    who = "u2"
    whom = "u4"
    tribbler.followOrUnfollowTx(True, who, whom)

    who = "u2"
    whom = "u1"
    _, _, success = tribbler.followOrUnfollowTx(True, who, whom)

    assert success == False  # already following

    who = "u2"
    whom = "u3"
    tribbler.followOrUnfollowTx(False, who, whom)

    who = "u2"
    whom = "u3"
    _, _, success = tribbler.followOrUnfollowTx(False, who, whom)

    assert success == False  # already unfollowed

    username = "u2"
    following_list = tribbler.followingTx(username)

    assert following_list == ["u1", "u4"]

    who = "u1"
    whom = "u2"
    tribbler.followOrUnfollowTx(False, who, whom)

    who = "u1"
    whom = "u2"
    is_following = tribbler.isFollowingTx(who, whom)

    assert is_following == False

    who = "u1"
    whom = "u3"
    following_list = tribbler.followingTx(who)

    assert following_list == ["u3"]

    who = "u1"
    whom = "u3"
    is_following = tribbler.isFollowingTx(who, whom)

    assert is_following == True


def test_post_multiple_users():
    tribbler = deploy.TribblerMain(accounts[6])

    users = ["u1", "u2", "u3"]

    for user in users:
        tribbler.signupTx(user)

    for i in range(2 * len(users)):
        who = users[i % len(users)]
        message = "trib" + str(i)
        tribbler.postTx(who, message)

    home_list = tribbler.homeTx("u1")
    listTribs = [trib_obj[1] for trib_obj in home_list]
    assert (len(listTribs) == 2) and (listTribs[0] > listTribs[1])

    who = "u1"
    whom = "u3"
    tribbler.followOrUnfollowTx(True, who, whom)

    who = "u2"
    whom = "u1"
    tribbler.followOrUnfollowTx(True, who, whom)

    home_list = tribbler.homeTx("u2")
    listTribs = [trib_obj[1] for trib_obj in home_list]
    assert (len(listTribs) == 4) and (
        listTribs[0] > listTribs[1] > listTribs[2] > listTribs[3]
    )

    home_list = tribbler.homeTx("u3")
    listTribs = [trib_obj[1] for trib_obj in home_list]
    assert (len(listTribs) == 2) and (listTribs[0] > listTribs[1])

    who = "u1"
    whom = "u3"
    tribbler.followOrUnfollowTx(False, who, whom)

    home_list = tribbler.homeTx("u1")
    listTribs = [trib_obj[1] for trib_obj in home_list]
    assert (len(listTribs) == 2) and (listTribs[0] > listTribs[1])


def test_multiple_follow_multiple_post():
    tribbler = deploy.TribblerMain(accounts[6])

    users = ["u1", "u2"]

    for user in users:
        tribbler.signupTx(user)

    for i in range(2 * len(users)):
        who = users[i % len(users)]
        message = "trib" + str(i)
        tribbler.postTx(who, message)

    who_whom = [("u1", "u2"), ("u2", "u3"), ("u1", "u3")]

    for who, whom in who_whom:
        tribbler.followOrUnfollowTx(True, who, whom)

    home_list = tribbler.homeTx("u1")
    listTribs = [trib_obj[1] for trib_obj in home_list]

    assert (len(listTribs) == 4) and (
        listTribs == ["trib" + str(i) for i in range(3, -1, -1)]
    )

    home_list = tribbler.homeTx("u2")
    listTribs = [trib_obj[1] for trib_obj in home_list]

    assert (len(listTribs) == 2) and (listTribs == ["trib3", "trib1"])
