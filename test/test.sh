#!/bin/bash

for i in input/*.txt
do
    echo "Running test $i"
    ../main input/accounts/$i.txt output/transactions/$i.txt < input/commands/$i.txt > output/logs/$i.txt
done
