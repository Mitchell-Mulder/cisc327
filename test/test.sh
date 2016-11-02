#!/bin/bash

for i in $(ls test/input/commands)
do
    pwd
    echo "Running test $i"
    ./main.py test/input/accounts/$i test/output/transactions/$i < test/input/commands/$i > test/output/logs/$i.log
done
