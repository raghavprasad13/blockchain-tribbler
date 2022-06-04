from scripts.tribbler_main import TribblerMain

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
)


def test_tribbler(contractAddresses):
    account = accounts[5]
    # tribbler = TribblerMain(
    #     account,
    #     stringContractAddr=contractAddresses["String_contract"],
    #     tribsContractAddr=contractAddresses["Tribs_contract"],
    #     utilsContractAddr=contractAddresses["Utils_contract"],
    #     tribblerContractAddr=contractAddresses["Tribbler_contract"],
    # )

    tribbler = Tribbler.at(contractAddresses["Tribbler_contract"])

    # tribbler = Contract(tribblerContractAddr)
    # print(type(tribbler))

    # # tribbler = TribblerMain(accounts[0])

    # tribbler.signup("harsh", {"from": account})
    # tribbler.signupTx("harsh")
    # print(tribbler.listUsers())

    # tribbler.signup("raghav", {"from": account})
    # tribbler.signupTx("raghav")
    # print(tribbler.listUsers())

    # tribbler.signup("rajdeep", {"from": account})
    # tribbler.signupTx("raghav")
    # print(tribbler.listUsers())

    print(tribbler.tribs("u2", {"from": account}).return_value)

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
