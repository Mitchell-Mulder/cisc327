

def find_account(number, accounts):
    for i in range(len(accounts)):
        if accounts[i][0] == number:
            return i
    return False


def withdraw(transaction, accounts):
    num = find_account(transaction[2], accounts)
    if not num:
        return accounts
    elif int(accounts[num][1]) - int(transaction[3]) < 0:
        return accounts
    else:
        accounts[num][1] = str(int(accounts[num][1]) - int(transaction[3]))
        return accounts


def deposit(transaction, accounts):
    num = find_account(transaction[1], accounts)
    if not num:
        return accounts
    else:
        accounts[num][1] = str(int(accounts[num][1]) + int(transaction[3]))
        return accounts


def transfer(transaction, accounts):
    num1 = find_account(transaction[1], accounts)
    num2 = find_account(transaction[2], accounts)
    if not (num1 or num2):
        return accounts
    elif int(accounts[num2][1]) - int(transaction[3]) < 0:
        return accounts
    else:
        accounts[num1][1] = str(int(accounts[num1][1]) + int(transaction[3]))
        accounts[num2][1] = str(int(accounts[num2][1]) - int(transaction[3]))
        return accounts


def create(transaction, accounts):
    num = find_account(transaction[1], accounts)
    if num:
        return accounts
    else:
        transaction = [transaction[1], '000', transaction[4]]
        accounts.append(transaction)
        return accounts


def delete(transaction, accounts):
    num = find_account(transaction[1], accounts)
    if not num:
        return accounts
    elif int(accounts[num][1]) != 0:
        return accounts
    else:
        accounts.remove([accounts[num][0], accounts[num][1], accounts[num][2]])
        return accounts
