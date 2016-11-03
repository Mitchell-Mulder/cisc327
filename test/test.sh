#!/bin/bash

# CLEAN UP AND PREPARE FOR TEST
# ---
# Delete any output folders remaining from previous tests

rm -rf test/output
mkdir test/output
mkdir test/output/logs
mkdir test/output/transactions


# RUN TESTS
# ---
# Start the program, using a folder of input accounts files and a folder of
# files containing standard input to be used, writing the transaction
# summary file and standard output to a pair of folders

for i in $(ls test/input/commands)
do
    echo "Running test $i"
    ./main.py test/input/accounts/$i test/output/transactions/$i < test/input/commands/$i > test/output/logs/$i.log
done


# CREATE SUMMARY FILE
# ---
# For each test, compare the two sets of files and store the diff in a file.
# Compare the transaction summary file, as well as the output log, with
# what was expected for the test.

DATE=$(date +%F_%T)
OUTFILE=test/results_${DATE}.txt
echo "Creating summary file"
echo "" > ${OUTFILE}
for i in $(ls test/expected/logs)
do
    echo "Comparing output log for test $i"
    echo "Comparing output log for test $i" >> ${OUTFILE}
    diff -b test/output/logs/$i.log test/expected/logs/$i >> ${OUTFILE}
    if [ -f test/expected/transactions/$i ]; then
        echo "Comparing transaction summary file for test $i"
        echo "Comparing transaction summary file for test $i" >> ${OUTFILE}
        diff -b test/output/transactions/$i test/expected/transactions/$i >> ${OUTFILE}
    fi
done
