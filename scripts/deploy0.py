# import subprocess

from scripts.tribbler_main import TribblerMain
from brownie import accounts

# def main():
#     import os

#     pwd = os.getcwd()

#     print("In deploy0")

#     subprocess.Popen("python3 {}/deploy1.py".format(pwd), shell=True)
#     subprocess.Popen("python3 {}/deploy2.py".format(pwd), shell=True)

#     import time

#     time.sleep(1)
#     print("Ending...")


def deploy_tribbler():
    tribbler = TribblerMain(accounts[2])

    contractAddress_dict = tribbler.getContractAddresses()

    # save address to a file for future use
    # manually for now as it is a one time process

    print(contractAddress_dict)


def main():
    deploy_tribbler()


if __name__ == "__main__":
    main()
