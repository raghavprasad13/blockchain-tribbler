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
We have a few tests in the `tests` directory as well as a couple in the `scripts` directory. The command to run a test file is: `brownie test <path to test file>`. For instance, `brownie test scripts/test_python_tribbler.py`

## Tribbler Contract
## User Contract