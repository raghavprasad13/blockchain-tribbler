from typing import List, Tuple
import time
from brownie import (
    accounts,
    Tribbler,
    User,
    network,
)
from .constants import *
from .utils import *
from .deploy import *


def deploy():
    account = accounts.load("demo_acc")
    tribbler = TribblerMain(account)
    users = ["_demo_user1", "_demo_user2"]

    for user in users:
        tribbler.signupTx(user)

    tribbler.postTx("_demo_user1", "testtrib1")
    tribbler.postTx("_demo_user2", "testtrib2")

    tribbler.followOrUnfollowTx(True, "_demo_user1", "_demo_user2")

    home_list = tribbler.homeTx("_demo_user1")
    home_list = [elem[1] for elem in home_list]

    print(home_list)


def main():
    deploy()
