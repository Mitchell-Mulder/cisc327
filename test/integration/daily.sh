#!/bin/bash

# RUN TESTS
# ---
# Start the program, using a folder of input accounts files and a folder of
# files containing standard input to be used, writing the transaction
# summary file and standard output to a pair of folders
for i in $(ls $1/input)
do
    echo "Running test $i"
    ./main.py $1/accounts.txt $1/transactions/$i < $1/input/$i
done

./backend.py $1/master_accounts.txt $1/accounts.txt $1/transactions
