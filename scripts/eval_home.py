"""
sign up 1 user and make him post ~500 tribs
check time taken for different gas prices

Usage: brownie run scripts/eval_serial_post
"""

from brownie import accounts, network, config
from random import randint
import time
from .deploy import TribblerMain
from .constants import (
    GAS_PRICE_FAST,
    GAS_PRICE_SAFE_LOW,
    GAS_PRICE_STANDARD,
    TRIBBLER_CONTRACT_HASH,
    # UTILS_CONTRACT_HASH,
)
from os.path import join
import os


def run(gas_price: int, account, timestamp):
    network.gas_price(str(gas_price) + " gwei")
    # account = accounts[6]

    # account = accounts.add(config["wallets"]["from_key"])

    tribbler = TribblerMain(
        account=account,
        # utilsAddr=UTILS_CONTRACT_HASH,
        tribblerAddr=TRIBBLER_CONTRACT_HASH,
    )

    # users = ["user" + str(i) for i in range(10)]  # 10 users

    # signup all 10 users
    # for user in users:
    #     tribbler.signupTx(user)

    test_user = "rajdeep"
    tribbler.signupTx(test_user)

    # Post 100 tribs for each user
    # users_tribs = {user: 0 for user in users}
    # choices = list(range(10))
    # trib_num = 0
    # while len(choices) > 0:
    #     choice = randint(0, len(choices) - 1)
    #     user_num = choices[choice]
    #     user = "user" + str(user_num)
    #     num_tribs = users_tribs[user]
    #     users_tribs.update({user: num_tribs + 1})

    #     tribbler.postTx(user, "trib" + str(trib_num))
    #     if num_tribs + 1 == 100:
    #         choices.remove(user_num)

    #     trib_num += 1

    file_name = "home"
    # now = int(time.time())

    final_file_name = "_".join([file_name, str(gas_price), str(timestamp), ".csv"])

    pwd = os.getcwd()

    f = open(join(pwd, "data", final_file_name), "w")

    # test_user = "user0"

    num_followers = 0
    # user0 follows 1 user then call home
    tribbler.followTx(test_user, "harsh")
    num_followers = len(tribbler.followingTx(test_user))

    start = time.time()
    tribbler.homeTx(test_user)
    # print(homeList)
    end = time.time()

    tribs_processed = 1
    time_taken = round(end - start, 3)
    f.write(
        str(num_followers) + "," + str(tribs_processed) + "," + str(time_taken) + "\n"
    )

    # user0 follows 1 more users then call home
    tribbler.followTx(test_user, "raghav")
    # tribbler.followTx(test_user, "user3")
    num_followers = len(tribbler.followingTx(test_user))

    start = time.time()
    tribbler.homeTx(test_user)
    # print(homeList)
    end = time.time()

    tribs_processed = 4
    time_taken = round(end - start, 3)
    f.write(
        str(num_followers) + "," + str(tribs_processed) + "," + str(time_taken) + "\n"
    )

    # user0 follows 2 more users then call home
    tribbler.followTx(test_user, "serialuser1")
    # tribbler.followTx(test_user, "user5")
    num_followers = len(tribbler.followingTx(test_user))

    start = time.time()
    tribbler.homeTx(test_user)
    end = time.time()

    tribs_processed = 100
    time_taken = round(end - start, 3)
    f.write(
        str(num_followers) + "," + str(tribs_processed) + "," + str(time_taken) + "\n"
    )

    tribbler.followTx(test_user, "serialuser2")
    # tribbler.followTx(test_user, "user5")
    num_followers = len(tribbler.followingTx(test_user))

    start = time.time()
    tribbler.homeTx(test_user)
    end = time.time()

    tribs_processed = 200
    time_taken = round(end - start, 3)
    f.write(
        str(num_followers) + "," + str(tribs_processed) + "," + str(time_taken) + "\n"
    )

    tribbler.followTx(test_user, "serialuser3")
    # tribbler.followTx(test_user, "user5")
    num_followers = len(tribbler.followingTx(test_user))

    start = time.time()
    tribbler.homeTx(test_user)
    end = time.time()

    tribs_processed = 300
    time_taken = round(end - start, 3)
    f.write(
        str(num_followers) + "," + str(tribs_processed) + "," + str(time_taken) + "\n"
    )

    tribbler.followTx(test_user, "serialuser4")
    # tribbler.followTx(test_user, "user5")
    num_followers = len(tribbler.followingTx(test_user))

    start = time.time()
    tribbler.homeTx(test_user)
    end = time.time()

    tribs_processed = 400
    time_taken = round(end - start, 3)
    f.write(
        str(num_followers) + "," + str(tribs_processed) + "," + str(time_taken) + "\n"
    )

    tribbler.followTx(test_user, "serialuser5")
    # tribbler.followTx(test_user, "user5")
    num_followers = len(tribbler.followingTx(test_user))

    start = time.time()
    tribbler.homeTx(test_user)
    end = time.time()

    tribs_processed = 500
    time_taken = round(end - start, 3)
    f.write(
        str(num_followers) + "," + str(tribs_processed) + "," + str(time_taken) + "\n"
    )

    tribbler.followTx(test_user, "paralleluser1")
    tribbler.followTx(test_user, "paralleluser2")
    num_followers = len(tribbler.followingTx(test_user))

    start = time.time()
    tribbler.homeTx(test_user)
    end = time.time()

    tribs_processed = 600
    time_taken = round(end - start, 3)
    f.write(
        str(num_followers) + "," + str(tribs_processed) + "," + str(time_taken) + "\n"
    )

    # # user0 follows 2 more users then call home
    # tribbler.followTx(test_user, "user6")
    # tribbler.followTx(test_user, "user7")
    # num_followers += 2

    # start = time.time()
    # tribbler.homeTx(test_user)
    # end = time.time()

    # time_taken = round(end - start, 2)
    # f.write(str(num_followers) + "," + str(time_taken))

    # # user0 follows 2 more users then call home
    # tribbler.followTx(test_user, "user8")
    # tribbler.followTx(test_user, "user9")
    # num_followers += 2

    # start = time.time()
    # tribbler.homeTx(test_user)
    # end = time.time()

    # time_taken = round(end - start, 2)
    # f.write(str(num_followers) + "," + str(time_taken))

    f.close()


def main():
    account = accounts.add(config["wallets"]["from_key"])
    timestamp = int(time.time())

    # gas_prices = [GAS_PRICE_SAFE_LOW, GAS_PRICE_STANDARD, GAS_PRICE_FAST]
    gas_prices = [50]
    # num_tribs = 500
    for gas_price in gas_prices:
        run(gas_price=gas_price, account=account, timestamp=timestamp)
