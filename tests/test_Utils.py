from brownie import Utils, String, Tribs, accounts


def test_whoWhomSame1():
    account = accounts[0]

    # arrange
    String.deploy({"from": account})
    Tribs.deploy({"from": account})
    utils_obj = Utils.deploy({"from": account})

    # act
    who = "abc"
    whom = "abc"
    output = utils_obj.whoWhomSame(who, whom)
    expected_output = True

    # assert
    assert output == expected_output


def test_whoWhomSame2():
    account = accounts[0]

    # arrange
    String.deploy({"from": account})
    Tribs.deploy({"from": account})
    utils_obj = Utils.deploy({"from": account})

    # act
    who = "abc"
    whom = "def"
    output = utils_obj.whoWhomSame(who, whom)
    expected_output = False

    # assert
    assert output == expected_output


def test_isValidUsername1():
    account = accounts[0]

    # arrange
    String.deploy({"from": account})
    Tribs.deploy({"from": account})
    utils_obj = Utils.deploy({"from": account})

    # act
    test_username = "u1"
    isValid_output = utils_obj.isValidUsername(test_username)
    expected_isValid_output = True

    # assert
    assert isValid_output == expected_isValid_output


def test_isValidUsername2():
    account = accounts[0]

    # arrange
    String.deploy({"from": account})
    Tribs.deploy({"from": account})
    utils_obj = Utils.deploy({"from": account})

    # act
    test_username = "1fefklrgwfcklrgm"
    isValid_output = utils_obj.isValidUsername(test_username)
    expected_isValid_output = False

    # assert
    assert isValid_output == expected_isValid_output


def test_isValidUsername3():
    account = accounts[0]

    # arrange
    String.deploy({"from": account})
    Tribs.deploy({"from": account})
    utils_obj = Utils.deploy({"from": account})

    # act
    test_username = "u1Tfdnrejknfg"
    isValid_output = utils_obj.isValidUsername(test_username)
    expected_isValid_output = False

    # assert
    assert isValid_output == expected_isValid_output


def test_exists1():
    account = accounts[0]

    # arrange
    String.deploy({"from": account})
    Tribs.deploy({"from": account})
    utils_obj = Utils.deploy({"from": account})

    # act
    test_arr = ["a", "p", "b", "q", "c", "r"]
    output = utils_obj.exists(test_arr, "q")
    expected_output = True

    # assert
    assert output == expected_output


def test_exists2():
    account = accounts[0]

    # arrange
    String.deploy({"from": account})
    Tribs.deploy({"from": account})
    utils_obj = Utils.deploy({"from": account})

    # act
    test_arr = []
    output = utils_obj.exists(test_arr, "a")
    expected_output = False

    # assert
    assert output == expected_output


def test_getIndex1():
    account = accounts[0]

    # arrange
    String.deploy({"from": account})
    Tribs.deploy({"from": account})
    utils_obj = Utils.deploy({"from": account})

    # act
    test_arr = ["a", "p", "b", "q", "c", "r"]
    output = utils_obj.getIndex(test_arr, "r")
    expected_output = 5

    # assert
    assert output == expected_output


def test_getIndex2():
    account = accounts[0]

    # arrange
    String.deploy({"from": account})
    Tribs.deploy({"from": account})
    utils_obj = Utils.deploy({"from": account})

    # act
    test_arr = ["a", "p", "b", "q", "c", "r"]
    output = utils_obj.getIndex(test_arr, "z")
    expected_output = -1

    # assert
    assert output == expected_output


##### deleteAtIndexUnordered
# def test_deleteAtIndexUnordered1():
#     account = accounts[0]

#     # arrange
#     String.deploy({"from": account})
#     Tribs.deploy({"from": account})
#     utils_obj = Utils.deploy({"from": account})

#     print(type(utils_obj))

#     # act
#     test_arr = ["a", "p", "b", "q", "c", "r"]
#     output = utils_obj.deleteAtIndexUnordered(test_arr, 2, {"from": account})
#     expected_output = ["a", "p", "r", "q", "c"]

#     # assert
#     assert output == expected_output


# def test_deleteAtIndexUnordered2():
#     account = accounts[0]

#     # arrange
#     String.deploy({"from": account})
#     Tribs.deploy({"from": account})
#     utils_obj = Utils.deploy({"from": account})

#     # act
#     test_arr = ["a", "p", "b", "q", "c", "r"]
#     output = utils_obj.deleteAtIndexUnordered(test_arr, len(test_arr) - 1)
#     expected_output = ["a", "p", "b", "q", "c"]

#     # assert
#     assert output == expected_output


##### deleteAtIndex


##### deepCopy

# # FAILED tests/test_Utils.py::test_deepCopy_memory1 - ValueError: Contract has more than one function 'Utils.deepCopy' requiring 1 arguments. You must explicitly declare which function you are calling...
# def test_deepCopy_memory1():
#     account = accounts[0]

#     # arrange
#     String.deploy({"from": account})
#     Tribs.deploy({"from": account})
#     utils_obj = Utils.deploy({"from": account})

#     # act
#     test_arr = ["a", "p", "b", "q", "c", "r"]
#     output = utils_obj.deepCopy(test_arr)
#     expected_output = test_arr

#     # assert
#     assert output == expected_output


##### sort


##### merge


##### appendArray
