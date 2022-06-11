# Test tribbler functionality

from . import deploy
from brownie import accounts, Utils, Tribbler, reverts


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
    account = accounts[0]

    Utils.deploy({"from": account})
    tribbler = Tribbler.deploy({"from": account})

    test_username = "u1"
    tribbler.signup(test_username)

    with reverts("User already exists"):
        tribbler.signup(test_username)


def test_listUsers():
    account = accounts[0]

    Utils.deploy({"from": account})
    tribbler = Tribbler.deploy({"from": account})

    tribbler.signup("u3")
    tribbler.signup("u2")
    tribbler.signup("u1")

    list_users = list(tribbler.listUsers())
    list_users.sort()
    print(list_users)

    assert list_users == ["u1", "u2", "u3"]


def test_noUsers():
    account = accounts[0]

    Utils.deploy({"from": account})
    tribbler = Tribbler.deploy({"from": account})

    with reverts("No users exist"):
        tribbler.listUsers()


def test_minListUser():
    account = accounts[0]

    Utils.deploy({"from": account})
    tribbler = Tribbler.deploy({"from": account})

    for i in range(25, -1, -1):
        username = "u" + str(i)
        tribbler.signup(username)

    listUsers = list(tribbler.listUsers())
    listUsers.sort()
    print(listUsers)

    listOfUsers = ["u" + str(i) for i in range(6, 26)]
    listOfUsers = sorted(listOfUsers)

    assert len(listUsers) == 20

    assert listUsers == listOfUsers
