import bInputOutput
import bCommands


def main():
    transactions = bInputOutput.merge_transactions()
    accounts = bInputOutput.read_master_accounts()
    print transactions
    print accounts
    for i in range(len(transactions)):
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
    bInputOutput.write_master_accounts(accounts)
    bInputOutput.write_accounts(accounts)


if __name__ == "__main__":
    main()
