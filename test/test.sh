#!/bin/bash

# CLEAN UP AND PREPARE FOR TEST

rm -rf test/output
mkdir test/output
mkdir test/output/logs
mkdir test/output/transactions


# RUN TESTS

for i in $(ls test/input/commands)
do
    pwd
    echo "Running test $i"
    ./main.py test/input/accounts/$i test/output/transactions/$i < test/input/commands/$i > test/output/logs/$i.log
done


# CREATE SUMMARY FILE

DATE=$(date +%F_%T)
OUTFILE=test/results_${DATE}.txt
echo "" > ${OUTFILE}
for i in $(ls test/expected/transactions)
do
    echo "Checking outputs of test $i" >> ${OUTFILE}
    diff test/output/transactions/$i test/expected/transactions/$i >> ${OUTFILE}
    diff test/output/logs/$i test/expected/logs/$i.log >> ${OUTFILE}
done
