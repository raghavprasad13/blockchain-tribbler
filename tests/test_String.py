from brownie import String, accounts


def test_lexicographicOrder1():
    # same length first string should be first
    account = accounts[0]

    # arrange
    string_obj = String.deploy({"from": account})

    # act
    s1 = "hello"
    s2 = "world"
    cmp_output = string_obj.compare(s1, s2)
    expected_cmp_output = 1  # s1 comes first lexicographically

    # assert
    assert cmp_output == expected_cmp_output


def test_lexicographicOrder2():
    # same length second string should be first
    account = accounts[0]

    # arrange
    string_obj = String.deploy({"from": account})

    # act
    s1 = "world"
    s2 = "hello"
    cmp_output = string_obj.compare(s1, s2)
    expected_cmp_output = -1  # s2 comes first lexicographically

    # assert
    assert cmp_output == expected_cmp_output


def test_lexicographicOrder3():
    # same length equal strings
    account = accounts[0]

    # arrange
    string_obj = String.deploy({"from": account})

    # act
    s1 = "hello world!"
    s2 = "hello world!"
    cmp_output = string_obj.compare(s1, s2)
    expected_cmp_output = 0  # equal strings

    # assert
    assert cmp_output == expected_cmp_output


def test_lexicographicOrder4():
    # different length first string should be first
    account = accounts[0]

    # arrange
    string_obj = String.deploy({"from": account})

    # act
    s1 = "hello world"
    s2 = "world"
    cmp_output = string_obj.compare(s1, s2)
    expected_cmp_output = 1  # s1 comes first lexicographically

    # assert
    assert cmp_output == expected_cmp_output


def test_lexicographicOrder5():
    # different length first string should be first
    account = accounts[0]

    # arrange
    string_obj = String.deploy({"from": account})

    # act
    s1 = "abc"
    s2 = "world"
    cmp_output = string_obj.compare(s1, s2)
    expected_cmp_output = 1  # s1 comes first lexicographically

    # assert
    assert cmp_output == expected_cmp_output


def test_lexicographicOrder6():
    # different length second string should be first
    account = accounts[0]

    # arrange
    string_obj = String.deploy({"from": account})

    # act
    s1 = "world"
    s2 = "hello world"
    cmp_output = string_obj.compare(s1, s2)
    expected_cmp_output = -1  # s2 comes first lexicographically

    # assert
    assert cmp_output == expected_cmp_output


def test_lexicographicOrder7():
    # different length second string should be first
    account = accounts[0]

    # arrange
    string_obj = String.deploy({"from": account})

    # act
    s1 = "world"
    s2 = "abc"
    cmp_output = string_obj.compare(s1, s2)
    expected_cmp_output = -1  # s2 comes first lexicographically

    # assert
    assert cmp_output == expected_cmp_output


def test_lexicographicOrder_special1():
    # different length second string should be first
    account = accounts[0]

    # arrange
    string_obj = String.deploy({"from": account})

    # act
    s1 = "hello"
    s2 = " world"
    cmp_output = string_obj.compare(s1, s2)
    expected_cmp_output = -1  # s2 comes first lexicographically

    # assert
    assert cmp_output == expected_cmp_output


def test_lexicographicOrder_special2():
    # different length second string should be first
    account = accounts[0]

    # arrange
    string_obj = String.deploy({"from": account})

    # act
    s1 = ""
    s2 = ""
    cmp_output = string_obj.compare(s1, s2)
    expected_cmp_output = 0  # equal

    # assert
    assert cmp_output == expected_cmp_output


def test_lexicographicOrder_special3():
    # different length second string should be first
    account = accounts[0]

    # arrange
    string_obj = String.deploy({"from": account})

    # act
    s1 = ""
    s2 = "   "
    cmp_output = string_obj.compare(s1, s2)
    expected_cmp_output = 1  # s1 comes first lexicographically

    # assert
    assert cmp_output == expected_cmp_output


def test_lexicographicOrder_special4():
    # different length second string should be first
    account = accounts[0]

    # arrange
    string_obj = String.deploy({"from": account})

    # act
    s1 = "abcde"
    s2 = ""
    cmp_output = string_obj.compare(s1, s2)
    expected_cmp_output = -1  # s2 comes first lexicographically

    # assert
    assert cmp_output == expected_cmp_output
