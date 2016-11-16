

def find_account(number, accounts):
    """
    This function takes in a account number and the master accounts list
    to check if the specified account number is in the master accounts list.
    """
    for i in range(len(accounts)):
        if accounts[i][0] == number:
            return i+1
    return 0


def withdraw(transaction, accounts):
    """
    This function takes in the merged transaction summary file and the master
    accounts list and updates the master accounts list with the specified transaction.
    If the transaction is not valid the program will terminate
    """
    num = find_account(transaction[2], accounts)
    if not num:
        return None
    elif int(accounts[num-1][1]) - int(transaction[3]) < 0:
        return None
    else:
        accounts[num-1][1] = str(int(accounts[num-1][1]) - int(transaction[3]))
        return accounts


def deposit(transaction, accounts):
    """
    This function takes in the merged transaction summary file and the master
    accounts list and updates the master accounts list with the specified transaction.
    """
    num = find_account(transaction[0], accounts)
    if not num:
        raise RuntimeError
    else:
        accounts[num-1][1] = str(int(accounts[num-1][1]) + int(transaction[3]))
        return accounts


def transfer(transaction, accounts):
    """
    This function takes in the merged transaction summary file and the master
    accounts list and updates the master accounts list with the specified transaction.
    """
    num1 = find_account(transaction[1], accounts)
    num2 = find_account(transaction[2], accounts)
    if not (num1 and num2):
        raise RuntimeError
    elif int(accounts[num2-1][1]) - int(transaction[3]) < 0:
        raise RuntimeError
    else:
        accounts[num1-1][1] = str(int(accounts[num1-1][1]) + int(transaction[3]))
        accounts[num2-1][1] = str(int(accounts[num2-1][1]) - int(transaction[3]))
        return accounts


def create(transaction, accounts):
    """
    This function takes in the merged transaction summary file and the master
    accounts list and updates the master accounts list with the specified transaction.
    """
    num = find_account(transaction[0], accounts)
    if num:
        raise RuntimeError
    else:
        transaction = [transaction[0], '000', transaction[3]]
        accounts.append(transaction)
        return accounts


def delete(transaction, accounts):
    """
    This function takes in the merged transaction summary file and the master
    accounts list and updates the master accounts list with the specified transaction.
    """
    num = find_account(transaction[1], accounts)
    if not num:
        return None
    elif int(accounts[num-1][1]) != 0:
        return None
    elif transaction[4] != accounts[num+1][2]:
        return None
    else:
        accounts.remove([accounts[num-1][0], accounts[num-1][1], accounts[num+1][2]])
        return accounts
