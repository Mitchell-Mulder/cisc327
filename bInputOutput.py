import os


def merge_transactions():
    """
    This function reads in all the transaction summary files
    and merges them into one list to easily be read.
    """
    transactions = []
    path = os.getcwd() + '/test/output/transactions/'
    for filename in os.listdir(path):
        with open('test/output/transactions/' + filename) as f:
                content = f.readlines()
        if len(content) >= 1:
            for i in range(0, len(content)-1):
                transactions.append(content[i])
    for i in range(len(transactions)):
        transactions[i] = transactions[i].split(' ', 4)
    return transactions


def read_master_accounts():
    """
    This function opens the master accounts file to be written into a list.
    """
    accounts = []
    with open('master_accounts.txt') as f:
        content = f.readlines()
    if len(content) >= 1:
        for i in range(0, len(content)):
            accounts.append(content[i])
    for i in range(len(accounts)):
        accounts[i] = accounts[i].split(' ', 2)
    return accounts


def write_accounts(accounts):
    """
    This function takes in the master account list and returns a valid
    account file in the test/input/accounts/ folder.
    """
    account = open('test/input/accounts/accounts.txt', 'w')
    for i in range(0, len(accounts)):
        account.write(accounts[i][0] + '\n')
    account.close()


def write_master_accounts(accounts):
    """
    This function takes in the master accounts list and returns a updated
    master accounts file in increasing order.
    """
    master_account = open('master_accounts.txt', 'w')
    accounts = sorted(accounts, key=lambda account: accounts[0])
    for i in range(0, len(accounts)):
        master_account.write('{} {} {}'.format(accounts[i][0], accounts[i][1], accounts[i][2]))
    master_account.close()
    return
