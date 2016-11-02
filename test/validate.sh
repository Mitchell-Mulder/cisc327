#!/bin/bash

for i in $(ls test/expected/transactions)
do
    echo "Checking outputs of test $i"
    diff test/output/transactions/$i test/expected/transactions/test$i
    diff test/output/logs/$i.log test/expected/logs/$i.log
done
