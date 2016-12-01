#!/bin/bash

WEEKLY_DIR=test/integration/weekly

cp test/integration/weekly_accounts.txt ${WEEKLY_DIR}/accounts.txt
cp test/integration/weekly_master_accounts.txt ${WEEKLY_DIR}/master_accounts.txt

for i in `seq 5`
do
    rm -rf ${WEEKLY_DIR}/input
    cp -r ${WEEKLY_DIR}/day${i}input ${WEEKLY_DIR}/input
    rm -rf ${WEEKLY_DIR}/transactions
    mkdir ${WEEKLY_DIR}/transactions
    test/integration/daily.sh ${WEEKLY_DIR}
done
