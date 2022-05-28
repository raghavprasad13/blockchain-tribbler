from brownie import Tribbler, Utils, Tribs, String, accounts, reverts


# def test_signup1():
#     account = accounts[0]

#     # arrange
#     String.deploy({"from": account})
#     Tribs.deploy({"from": account})
#     Utils.deploy({"from": account})
#     tribbler = Tribbler.deploy({"from": account})

#     # act
#     test_username = "u1"
#     output = tribbler.signup(test_username)
#     output.wait(1)
#     # print(type(output))
#     # expected_output = True

#     # list_usernames = tribbler.usernames
#     # print(list_usernames[0])

#     # assert
#     # assert type(output) == expected_output


def test_signup2():
    account = accounts[0]

    # arrange
    String.deploy({"from": account})
    Tribs.deploy({"from": account})
    Utils.deploy({"from": account})
    tribbler = Tribbler.deploy({"from": account})

    # act
    test_username = "1u"

    with reverts("Username is invalid"):
        tribbler.signup(test_username)


def test_signup3():
    account = accounts[0]

    # arrange
    String.deploy({"from": account})
    Tribs.deploy({"from": account})
    Utils.deploy({"from": account})
    tribbler = Tribbler.deploy({"from": account})

    # act
    test_username = "uV"
    with reverts("Username is invalid"):
        tribbler.signup(test_username)


def test_signup4():
    account = accounts[0]

    # arrange
    String.deploy({"from": account})
    Tribs.deploy({"from": account})
    Utils.deploy({"from": account})
    tribbler = Tribbler.deploy({"from": account})

    # act
    test_username = "u1"
    tribbler.signup(test_username)

    with reverts("User already exists"):
        tribbler.signup(test_username)


def test_listUsers():
    account = accounts[0]

    # arrange
    String.deploy({"from": account})
    Tribs.deploy({"from": account})
    Utils.deploy({"from": account})
    tribbler = Tribbler.deploy({"from": account})

    # act
    tribbler.signup("u1")
    # tx.wait(1)
    # print(tx.return_value)

    tribbler.signup("u2")
    # tx.wait(1)
    # print(tx.return_value)

    tribbler.signup("u3")
    # tx.wait(1)
    # print(tx.return_value)

    list_users = tribbler.listUsers()
    # print(list_users.info())

    assert sorted(list_users) == ["u1", "u2", "u3"]


# def post():
#     pass

# def test_tribs():
#     pass


# def test_follow():
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

#     tribbler.follow("u1", "u2")
#     tribbler.follow("u3", "u2")
#     tribbler.follow("u1", "u3")

#     with reverts("User already exists"):
#         tribbler.signup(test_username)


# def test_unfollow():
#     pass


# def test_isFollowing():
#     pass


# def test_followingList():
#     pass

# def home():
#     pass
