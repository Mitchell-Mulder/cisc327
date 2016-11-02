#!/bin/bash

chdir output/logs
for i in *.log
do
    echo "Checking outputs of test $i"
    diff ../transactions/$i.txt ../../expected/transactions/$i.txt
    diff ./$i.log ../../expected/logs/$i.log
done
