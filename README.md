# Tribbler: A Blockchain-based Decentralized Application

This repository contains code to implement Tribbler, a twitter-like service on blockchain.

[Link to demo video](https://drive.google.com/file/d/1JHfVsBFs2os6VWpHJRd4HcolGiIxK-JE/view?usp=sharing)


<p align="center">
  <img src="https://github.com/raghavprasad13/blockchain-tribbler/blob/main/tribbler-blockchain-diagram.png">
</p>

## Structure of the Repository
There are 3 branches in the repo
1. `main` - Contains the optimized implementation with user-specific contracts. This implementation has the least gas utilization because most of the compute operations are performed on the frontend.
2. `efficient-code` - Contains the optimized implementation that performs most of the compute operations in frontend, but has a single central tribbler contract to handle data and storage for all users. 
3. `inefficient` - This is also a correct and working implementation code. However it contains many data processing and manipulation operations in the Solidity code i.e. on blockchain. Thus, this implementation incurs very high gas utilization.


### Structure of `main` branch
- `contracts` - Contains backend Solidity code for Tribbler and User smart contracts containing all the backend tribbler functionality that will be deployed on blockchain.
    - `Tribbler.sol` - Tribbler contract functionality. The only task here is to sign up users and store a mapping of username and the corresponding address (hash) of the user contract deployed on blockchain.
        - Many functions like listUsers(), tribs(), following(), isFollowing() and home() have been implemented as view functions which only read from blockchain. They do not perform any transactions or modify the state of blockchain and hence don't incur any cost.
    - `User.sol` - User contract functionality. Performs all the user specific operations on blockchain.
- `data` - Data/observations used for analysis.
- `data_extra` - All the collected data.
- `scripts` - Python scripts for frontend functionality along with required test scripts.
    - `deploy.py` - Script containing `TribblerMain` class which acts as frontend and contains wrapper functions to call above contracts and perform operations on blockchain.
    - `utils.py` - Utility functions used by frontend.
    - `constants.py` - Contains constant values. Stores hash of Tribber contract deployed on ropsten testnes
    - `test_python_utils.py` - contains 8 tests to test utility functions.
    - `test_python_tribbler.py` - Implements 15 tests to test Tribbler functionality.
    - `eval_home.py` - To perform home() operation (and other required signup and follow-unfollow operations)
    - `eval_serial_post.py` - To post tribs for multiple users for multiple gas prices.
- `brownie-config.yaml` - brownie configurations required to run this dapp
- `requirements.txt` - To setup python virtualenv to run this code

### Structure of `efficient-code` branch
- `contracts` - Contains Solidity code for Tribbler and User contracts and supporting Utility functions containing all the backend tribbler functionality that will be deployed on blockchain. 
    - Many functions like listUsers(), tribs(), following(), isFollowing() and home() have been implemented as view functions which only read from blockchain. They do not perform any transactions or modify the state of blockchain and hence don't incur any cost.
- `data` - Data/observations used for analysis
- `data_extra` - All the collected data
- `scripts` - Python scripts for frontend functionality along with required test scripts

### Structure of `inefficient` branch
- `contracts` - Contains Solidity code for Tribbler and User contracts and supporting Utility functions containing all the backend tribbler functionality that will be deployed on blockchain. This manages significant Tribbler code logic and hence performs transactions for most of the functions which is costly as each transaction required ether.
- `scripts` - Python scripts for basic frontend functionality


## Environment setup

- Ensure basic packages along with python3 including pip and virtualenv are installed
- Setup a virtualenv and install packages using `pip install -r requirements.txt`

### Installing ganache-cli
- Install NodeJS at [https://nodejs.dev/download/](https://nodejs.dev/download/) or install from nodesource https://github.com/nodesource/distributions/blob/master/README.md
    - Code tested on version 16.15
- Installation success sanity check: `node --version`
- Install yarn: `sudo npm install --global yarn`
- Installation success sanity check: `yarn --version`
- Install ganache-cli: `sudo yarn global add ganache-cli`
- Installation success sanity check: `ganache-cli --version`

### Setting up Brownie
- Install pipx: `python3 -m pip install pipx`
- Install ensurepath: `python3 -m pipx ensurepath`
- Install brownie: `pipx install eth-brownie`
- Create `.env` file 
    - Add `Infura` project id or a key of API service which will be used to connect to public blockchain networks
    - Add `PRIVATE_KEY` of `MetaMask` or your blockchain account

- Create (or verify) network with `brownie networks list`
- Add your blockchain account that is used for deployment to brownie: `brownie accounts new`



## Running the main program
- Our main frontend code is housed in `scripts/deploy.py`. 
- The command to run that program is: `brownie run scripts/deploy.py`

## Running tests
- We have a couple of tests in the `scripts` directory. 
- The command to run a test file is: `brownie test <path to test file>`.
    - For example, `brownie test scripts/test_python_tribbler.py`

## Backend code
- We are using the blockchain to serve as our backend. And the code we are using to communicate/perform operations on the backend is housed in the `contracts` directory. `contracts` contains Solidity smart contracts that define a main `Tribbler` contract and user-specific `User` contracts.
