from . import deploy
from brownie import accounts


def test_signup1():

    # arrange
    tribbler = deploy.TribblerMain(accounts[6])

    # act
    test_username = "u1"
    tx = tribbler.signupTx(test_username)
    tx.wait(1)

    expected_output = True

    # list_usernames = tribbler.usernames
    # print(list_usernames[0])

    # assert
    assert tx.return_value == expected_output


def test_signup2():
    account = accounts[0]

    # arrange
    Utils.deploy({"from": account})
    tribbler = Tribbler.deploy({"from": account})

    # act
    test_username = "1u"

    with reverts("Username is invalid"):
        tribbler.signup(test_username)


def test_signup3():
    account = accounts[0]

    # arrange
    Utils.deploy({"from": account})
    tribbler = Tribbler.deploy({"from": account})

    # act
    test_username = "uV"
    with reverts("Username is invalid"):
        tribbler.signup(test_username)


def test_signup4():
    account = accounts[0]

    # arrange
    Utils.deploy({"from": account})
    tribbler = Tribbler.deploy({"from": account})

    # act
    test_username = "u1"
    tribbler.signup(test_username)

    with reverts("User already exists"):
        tribbler.signup(test_username)


def test_listUsers():
    account = accounts[0]

    # network.gas_price("50 gwei")

    # arrange
    Utils.deploy({"from": account})
    tribbler = Tribbler.deploy({"from": account})

    # act
    tribbler.signup("u3")
    # tx.wait(1)
    # print(tx.return_value)

    tribbler.signup("u2")
    # tx.wait(1)
    # print(tx.return_value)

    tribbler.signup("u1")
    # tx.wait(1)
    # print(tx.return_value)

    list_users = list(tribbler.listUsers())
    list_users.sort()
    print(list_users)

    assert list_users == ["u1", "u2", "u3"]


def test_noUsers():
    account = accounts[0]

    # arrange
    Utils.deploy({"from": account})
    tribbler = Tribbler.deploy({"from": account})

    # act

    # assert
    with reverts("No users exist"):
        tribbler.listUsers()


def test_minListUser():
    account = accounts[0]

    # arrange
    Utils.deploy({"from": account})
    tribbler = Tribbler.deploy({"from": account})

    # act
    for i in range(25, -1, -1):
        username = "u" + str(i)
        # print(username)
        tribbler.signup(username)

    listUsers = list(tribbler.listUsers())
    listUsers.sort()
    print(listUsers)

    listOfUsers = ["u" + str(i) for i in range(6, 26)]
    listOfUsers = sorted(listOfUsers)

    assert len(listUsers) == 20

    assert listUsers == listOfUsers
