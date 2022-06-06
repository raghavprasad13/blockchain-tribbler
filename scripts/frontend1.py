from collections import UserList
from . import deploy

from brownie import accounts


def main():

    contractAddresses = {
        "utils_contract": "0xF94f44597ABebc72CDB0980079fc483fCD49745A",
        "tribbler_contract": "0x25836965Fb1f7993de6F19929666B2e257492fe3",
    }

    account = accounts[6]

    tribbler = deploy.TribblerMain(
        account,
        utilsAddr=contractAddresses["utils_contract"],
        tribblerAddr=contractAddresses["tribbler_contract"],
    )

    # signup 10 users and print gas price
    # signup_gas_used = []
    # for i in range(14, 25):
    #     username = "u" + str(i)
    #     tx, gas_used = tribbler.signupTx(username)
    #     signup_gas_used.append(gas_used)

    # print(signup_gas_used)

    # post 1000 tribs and print gas price

    userList = ["u1", "u2"]

    # post_gas_used = []

    # for i in range(120):
    #     username = userList[i % 2]

    #     message = "test trib " + str(i)

    #     tx, gas_used = tribbler.postTx(username, message)

    #     post_gas_used.append(gas_used)

    # print(post_gas_used)

    print(tribbler.listUsersTx())

    print(len(tribbler.tribsTx("u1")))

    tx, gas_used, isConcurrentSuccessful = tribbler.followTx("u2", "u1")

    homeList = tribbler.homeTx("u2")

    print(homeList)
    print(len(homeList))
