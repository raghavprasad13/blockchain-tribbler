# Tribbler on Blockchain

## Installing ganache-cli
- Install NodeJS at [https://nodejs.dev/download/](https://nodejs.dev/download/)
- Installation success sanity check: `node --version`
- `npm install --global yarn`
- Installation success sanity check: `yarn --version`
- `yarn global add ganache-cli`
- Installation success sanity check: `ganache-cli --version`
## Setting up Brownie
- `python3 -m pip install --user pipx`
- `python3 -m pipx ensurepath`
- `pipx install eth-brownie`

## Running the main program
Our main frontend code is housed in `scripts/deploy.py`. The command to run that program is: `brownie run scripts/deploy.py`

## Running tests
We have a couple of tests in the `scripts` directory. The command to run a test file is: `brownie test <path to test file>`. For instance, `brownie test scripts/test_python_tribbler.py`

## Backend code
We are using the blockchain to serve as our backend. And the code we are using to communicate/perform operations on the backend is housed in the `contracts` directory. `contracts` contains Solidity smart contracts that define a main `Tribbler` contract and user-specific `User` contracts.

## Other branches
We have three main variations of our Tribbler on Blockchain implementation, housed in three different branches of this repository:
- This branch: contain our most optimized design wherein we chose to deploy a `User` contract for each different user in our system
- `inefficient`: TODO
- `efficient-code`: TODO

## Tribbler Contract
## User Contract