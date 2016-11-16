"""

CISC 327 Assignment 4

Brandon Bloch (10052759),
Bryce Marshall (10113902),
Mitchell Mulder (10137002)

This program merges the transaction summary files and
reads in the master accounts file. It then loops through
the whole merged transaction summary file updating the
master accounts file to produce a updated master accounts
file and a valid accounts file.

"""

import bInputOutput
import bCommands


def main():
    transactions = bInputOutput.merge_transactions()
    accounts = bInputOutput.read_master_accounts()
    """
    This loops through the transactions updating the master accounts
    file depending what transaction is requested.
    """
    for i in range(len(transactions)):
        try:
            if transactions[i][0] == 'WD':
                accounts = bCommands.withdraw(transactions[i], accounts)
            elif transactions[i][0] == 'DE':
                accounts = bCommands.deposit(transactions[i], accounts)
            elif transactions[i][0] == 'TR':
                accounts = bCommands.transfer(transactions[i], accounts)
            elif transactions[i][0] == 'DL':
                accounts = bCommands.delete(transactions[i], accounts)
            else:
                accounts = bCommands.create(transactions[i], accounts)
        except RuntimeError:
            print 'Fatal Error: Process Aborted.'
    bInputOutput.write_master_accounts(accounts)
    bInputOutput.write_accounts(accounts)
    return


if __name__ == "__main__":
    main()
