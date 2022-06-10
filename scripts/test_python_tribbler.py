from . import deploy
from brownie import accounts, Tribbler, reverts


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
