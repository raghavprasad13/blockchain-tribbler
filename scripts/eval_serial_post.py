"""
sign up 1 user and make him post ~500 tribs
check time taken for different gas prices
"""
from brownie import accounts
import time
from .deploy import TribblerMain
from .constants import TRIBBLER_CONTRACT_HASH, UTILS_CONTRACT_HASH
from os.path import join

account = accounts[6]

tribbler = TribblerMain(
    account=account, utilsAddr=UTILS_CONTRACT_HASH, tribblerAddr=TRIBBLER_CONTRACT_HASH
)

users = ["raghav", "rajdeep", "harsh"]

user = users[0]

tribbler.signupTx(user)

num_tribs = 500

file_name = "serial_post_"
now = int(time.time())

final_file_name = file_name + str(now) + ".csv"

f = open(join("..", "data", final_file_name), "w")
for trib_num in range(1, 501):
    start = time.time()
    tribbler.postTx(user, "trib" + str(trib_num))
    end = time.time()

    time_taken = round(end - start, 2)
    f.write(str(trib_num) + "," + str(time_taken))

f.close()
