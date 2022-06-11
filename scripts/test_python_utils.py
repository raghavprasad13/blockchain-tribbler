# Test utils.py functionality

from . import utils


def test_isValidUsername1():

    # arrange

    # act
    test_username = "u1"
    isValid_output = utils.isValidUsername(test_username)
    expected_isValid_output = True

    # assert
    assert isValid_output == expected_isValid_output


def test_isValidUsername2():
    # arrange

    # act
    test_username = "1fefklrgwfcklrgm"
    isValid_output = utils.isValidUsername(test_username)
    expected_isValid_output = False

    # assert
    assert isValid_output == expected_isValid_output


def test_isValidUsername3():
    # arrange

    # act
    test_username = "u1Tfdnrejknfg"
    isValid_output = utils.isValidUsername(test_username)
    expected_isValid_output = False

    # assert
    assert isValid_output == expected_isValid_output


def test_isValidUsername4():
    # arrange

    # act
    test_username = ""
    isValid_output = utils.isValidUsername(test_username)
    expected_isValid_output = False

    # assert
    assert isValid_output == expected_isValid_output


def test_isValidUsername5():
    # arrange

    # act
    test_username = "a" * 16
    isValid_output = utils.isValidUsername(test_username)
    expected_isValid_output = False

    # assert
    assert isValid_output == expected_isValid_output


def test_whoWhomSame1():
    # arrange

    # act
    who = "abc"
    whom = "abc"
    output = utils.whoWhomSame(who, whom)
    expected_output = True

    # assert
    assert output == expected_output


def test_whoWhomSame2():
    # arrange

    # act
    who = "abc"
    whom = "ab9"
    output = utils.whoWhomSame(who, whom)
    expected_output = False

    # assert
    assert output == expected_output


def test_longTrib():
    # arrange

    # act
    message = "a" * 141
    output = utils.isLongTrib(message)
    expected_output = True

    # assert
    assert output == expected_output
