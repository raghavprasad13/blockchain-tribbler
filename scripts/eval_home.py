"""
sign up 1 user and make him post ~500 tribs
check time taken for different gas prices

Usage: brownie run scripts/eval_serial_post
"""

from brownie import accounts, network
from random import randint
import time
from .deploy import TribblerMain
from .constants import (
    GAS_PRICE_FAST,
    GAS_PRICE_SAFE_LOW,
    GAS_PRICE_STANDARD,
    TRIBBLER_CONTRACT_HASH,
    UTILS_CONTRACT_HASH,
)
from os.path import join


def run(gas_price: int):
    network.gas_price(str(gas_price) + " gwei")
    account = accounts[6]

    tribbler = TribblerMain(
        account=account,
        utilsAddr=UTILS_CONTRACT_HASH,
        tribblerAddr=TRIBBLER_CONTRACT_HASH,
    )

    users = ["user" + str(i) for i in range(10)]  # 10 users

    # signup all 10 users
    for user in users:
        tribbler.signupTx(user)

    # Post 100 tribs for each user
    users_tribs = {user: 0 for user in users}
    choices = list(range(10))
    trib_num = 0
    while len(choices) > 0:
        choice = randint(0, len(choices) - 1)
        user_num = choices[choice]
        user = "user" + str(user_num)
        num_tribs = users_tribs[user]
        users_tribs.update({user: num_tribs + 1})

        tribbler.postTx(user, "trib" + str(trib_num))
        if num_tribs + 1 == 100:
            choices.remove(user_num)

        trib_num += 1

    file_name = "home"
    now = int(time.time())

    final_file_name = "_".join([file_name, str(gas_price), str(now), ".csv"])

    f = open(join("..", "data", final_file_name), "w")

    test_user = "user0"

    num_followers = 0
    # user0 follows 1 user then call home
    tribbler.followTx(test_user, "user1")
    num_followers += 1

    start = time.time()
    tribbler.homeTx(test_user)
    end = time.time()

    time_taken = round(end - start, 2)
    f.write(str(num_followers) + "," + str(time_taken))

    # user0 follows 2 more users then call home
    tribbler.followTx(test_user, "user2")
    tribbler.followTx(test_user, "user3")
    num_followers += 2

    start = time.time()
    tribbler.homeTx(test_user)
    end = time.time()

    time_taken = round(end - start, 2)
    f.write(str(num_followers) + "," + str(time_taken))

    # user0 follows 2 more users then call home
    tribbler.followTx(test_user, "user4")
    tribbler.followTx(test_user, "user5")
    num_followers += 2

    start = time.time()
    tribbler.homeTx(test_user)
    end = time.time()

    time_taken = round(end - start, 2)
    f.write(str(num_followers) + "," + str(time_taken))

    # user0 follows 2 more users then call home
    tribbler.followTx(test_user, "user6")
    tribbler.followTx(test_user, "user7")
    num_followers += 2

    start = time.time()
    tribbler.homeTx(test_user)
    end = time.time()

    time_taken = round(end - start, 2)
    f.write(str(num_followers) + "," + str(time_taken))

    # user0 follows 2 more users then call home
    tribbler.followTx(test_user, "user8")
    tribbler.followTx(test_user, "user9")
    num_followers += 2

    start = time.time()
    tribbler.homeTx(test_user)
    end = time.time()

    time_taken = round(end - start, 2)
    f.write(str(num_followers) + "," + str(time_taken))

    f.close()


gas_prices = [GAS_PRICE_SAFE_LOW, GAS_PRICE_STANDARD, GAS_PRICE_FAST]
num_tribs = 500
for gas_price in gas_prices:
    run(gas_price=gas_price)
