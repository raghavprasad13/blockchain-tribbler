# Tribbler on Blockchain


build-essential
python3
pip
venv
python3 -m venv blockchain-tribbler-venv
source blockchain-tribbler-venv
pip install -r requirements.txt

## Installing ganache-cli
- Install NodeJS at [https://nodejs.dev/download/](https://nodejs.dev/download/) - install from nodesource https://github.com/nodesource/distributions/blob/master/README.md - working on version 16.15

- Installation success sanity check: `node --version`
- `sudo npm install --global yarn`
- Installation success sanity check: `yarn --version`
- `sudo yarn global add ganache-cli`
- Installation success sanity check: `ganache-cli --version`
## Setting up Brownie
- `python3 -m pip install --user pipx` - no --user here for now
- `python3 -m pipx ensurepath`
- `pipx install eth-brownie`


- add .env and brownie-config.yaml - add infura key

- check network with brownie networks list - ensure infura

- add account - `brownie accounts new`


## Tribbler Contract
## User Contract

Some of the error checking and validation of data can be deferred to the Python deployment script