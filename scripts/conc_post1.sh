#!/usr/bin/env bash

cd /home/rajdeep/MS/Q3_Spring2022/CSE223B/project/blockchain-tribbler
source activate blockchain-tribbler-venv/bin/activate
brownie run scripts/conc_post1.py
deactivate
