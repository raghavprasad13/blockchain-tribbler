from . import utils


def test_isValidUsername1():
    test_username = "u1"
    isValid_output = utils.isValidUsername(test_username)
    expected_isValid_output = True

    assert isValid_output == expected_isValid_output


def test_isValidUsername2():
    test_username = "1fefklrgwfcklrgm"
    isValid_output = utils.isValidUsername(test_username)
    expected_isValid_output = False

    assert isValid_output == expected_isValid_output


def test_isValidUsername3():
    test_username = "u1Tfdnrejknfg"
    isValid_output = utils.isValidUsername(test_username)
    expected_isValid_output = False

    assert isValid_output == expected_isValid_output


def test_isValidUsername4():
    test_username = ""
    isValid_output = utils.isValidUsername(test_username)
    expected_isValid_output = False

    assert isValid_output == expected_isValid_output


def test_isValidUsername5():
    test_username = "a" * 16
    isValid_output = utils.isValidUsername(test_username)
    expected_isValid_output = False

    assert isValid_output == expected_isValid_output


def test_whoWhomSame1():
    who = "abc"
    whom = "abc"
    output = utils.whoWhomSame(who, whom)
    expected_output = True

    assert output == expected_output


def test_whoWhomSame2():
    who = "abc"
    whom = "ab9"
    output = utils.whoWhomSame(who, whom)
    expected_output = False

    assert output == expected_output


def test_longTrib():
    message = "a" * 141
    output = utils.isLongTrib(message)
    expected_output = True

    assert output == expected_output
