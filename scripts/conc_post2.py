from brownie import (
    accounts,
    config,
    Tribbler,
    Utils,
    Tribs,
    Constants,
    String,
    network,
    Contract,
    # reverts,
)

# import brownie

import time


def test_tribbler(contractAddresses):
    # time.sleep(5)

    account = accounts[4]
    # tribbler = TribblerMain(
    #     account,
    #     stringContractAddr=contractAddresses["String_contract"],
    #     tribsContractAddr=contractAddresses["Tribs_contract"],
    #     utilsContractAddr=contractAddresses["Utils_contract"],
    #     tribblerContractAddr=contractAddresses["Tribbler_contract"],
    # )

    tribbler = Tribbler.at(contractAddresses["Tribbler_contract"])
    # print(type(tribbler))

    # # tribbler = TribblerMain(accounts[0])

    for i in range(104, 106):
        # with brownie.reverts("User already exists"):
        # tribbler.signup("ru" + str(i), {"from": account})
        time.sleep(1)

        who = "u2"
        message = "testtrib" + str(i)
        tx = tribbler.post(who, message, {"from": account})
        tx.wait(1)
        success = tx.return_value

        if not success:
            return None

        tx_index = tx.txindex
        timestamp = int(time.time())
        block_num = tx.block_number

        tx = tribbler.addTrib(
            who, message, timestamp, block_num, tx_index, {"from": account}
        )
        tx.wait(1)

    # tribbler.signup("harsh", {"from": account})
    # tribbler.signupTx("harsh")
    # print(tribbler.listUsers())

    # tribbler.signup("raghav", {"from": account})
    # tribbler.signupTx("raghav")
    # print(tribbler.listUsers())

    # tribbler.postTx("raghav", "testtrib1")
    # print(tribbler.tribsTx("raghav").return_value)
    # tribbler.followTx("raghav", "harsh")


def main():
    # print("hello deploy1")

    contractAddresses = {
        "String_contract": "0x817BCE88b6194141D8F72ffB4293D8ee0528A605",
        "Tribs_contract": "0x02908cD48c286825045918FFE07C23b238B761F8",
        "Utils_contract": "0x03f5Cf047849849C753d28898642dAe60AB7eaCD",
        "Tribbler_contract": "0x18edFc507a5ccB62c740d7bF52aA4DAEb811e7de",
    }
    print(contractAddresses["Tribbler_contract"])

    test_tribbler(contractAddresses)


if __name__ == "__main__":
    main()
