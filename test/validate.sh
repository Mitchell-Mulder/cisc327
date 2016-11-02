#!/bin/bash

for i in input/*.txt
do
    echo "Checking outputs of test $i"
    diff output/transactions/$i.txt expected/transactions/$i.txt
    diff output/logs/$i.log expected/logs/$i.log
done
