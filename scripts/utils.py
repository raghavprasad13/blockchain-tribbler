from . import constants


def isValidUsername(username) -> bool:
    if len(username) <= 0 or len(username) > constants.MAX_USERNAME_LEN:
        return False

    # check if the first character is a lowercase alphabet
    if not username[0].islower():
        return False

    # check the rest of the characters - should be a digit or a lowercase letter
    for i in range(len(username)):
        if not username[i].islower() and not username[i].isdigit():
            return False

    return True


def whoWhomSame(who, whom) -> bool:
    return (
        who == whom
    )  # validity of username already checked - No need to check case sensitivity


def isLongTrib(message) -> bool:
    return len(message) > constants.MAX_TRIB_LEN
