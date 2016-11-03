#!/bin/bash

# CLEAN UP AND PREPARE FOR TEST

rm -rf test/output
mkdir test/output
mkdir test/output/logs
mkdir test/output/transactions


# RUN TESTS

for i in $(ls test/input/commands)
do
    echo "Running test $i"
    ./main.py test/input/accounts/$i test/output/transactions/$i < test/input/commands/$i > test/output/logs/$i.log
done


# CREATE SUMMARY FILE

DATE=$(date +%F_%T)
OUTFILE=test/results_${DATE}.txt
echo "Creating summary file"
echo "" > ${OUTFILE}
for i in $(ls test/expected/logs)
do
    echo "Comparing output log for test $i"
    echo "Comparing output log for test $i" >> ${OUTFILE}
    diff test/output/logs/$i.log test/expected/logs/$i >> ${OUTFILE}
    if [ -f test/expected/transactions/$i ]; then
        echo "Comparing transaction summary file for test $i"
        echo "Comparing transaction summary file for test $i" >> ${OUTFILE}
        diff test/output/transactions/$i test/expected/transactions/$i >> ${OUTFILE}
    fi
done
