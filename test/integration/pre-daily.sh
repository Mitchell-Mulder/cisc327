#!/bin/bash

# CLEAN UP AND PREPARE FOR TEST
# ---
# Delete any output folders remaining from previous tests

cp test/integration/accounts.txt $1/accounts.txt
cp test/integration/master_accounts.txt $1/master_accounts.txt
rm -rf $1/transactions
mkdir $1/transactions
