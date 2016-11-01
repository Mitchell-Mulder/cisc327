import io
import validation


def prompt_for_account_number(prompt_message, error_message, should_exist=True):
    """
    Repeatedly prompt the user for a valid account number.
    Return the number once it is successfully provided.
    """
    number = io.prompt_for_input(prompt_message)
    if should_exist:
        while not (validation.validate_account_number(number) and validation.account_number_exists(number)):
            print 'Error: ' + error_message
            number = io.prompt_for_input(prompt_message)
    else:
        while (not validation.validate_account_number(number, False)) or validation.account_number_exists(number):
            print 'Error: ' + error_message
            number = io.prompt_for_input(prompt_message)
    return int(number)


def prompt_for_amount(prompt_message, error_message, is_agent, session_withdrawals=0):
    """
    Repeatedly prompt the user for a valid amount in cents.
    Return the amount once it is successfully provided.
    """
    number = io.prompt_for_input(prompt_message)
    while not validation.validate_amount(number, is_agent, session_withdrawals):
        print 'Error: ' + error_message
        number = io.prompt_for_input(prompt_message)
    return int(number)


def prompt_for_account_name(prompt_message, error_message):
    """
    Repeatedly prompt the user for a valid account name.
    Return the name once it is successfully provided.
    """
    name = io.prompt_for_input(prompt_message)
    while not validation.validate_name(name):
        print 'Error: ' + error_message
        name = io.prompt_for_input(prompt_message)
    return name


def transfer(is_agent):
    """
    Collect the arguments for a "transfer" command.
    """
    from_account = prompt_for_account_number('From account', 'Invalid first account number')
    to_account = prompt_for_account_number('To account', 'Invalid second account number')
    amount = prompt_for_amount('Amount', 'Invalid amount', is_agent)
    print 'Transfer successful'
    return ['transfer', from_account, to_account, amount]


def withdraw(is_agent, existing_withdrawals):
    """
    Collect the arguments for a "withdraw" command.
    """
    account_number = prompt_for_account_number('Account number', 'Invalid account number')
    if account_number in existing_withdrawals:
        session_withdrawals = existing_withdrawals[account_number]
    else:
        session_withdrawals = 0
    amount = prompt_for_amount('Amount', 'Invalid amount', is_agent, session_withdrawals)
    print 'Withdrawal successful'
    return ['withdraw', account_number, amount]


def deposit(is_agent):
    """
    Collect the arguments for a "deposit" command.
    """
    account_number = prompt_for_account_number('Account number', 'Invalid account number')
    amount = prompt_for_amount('Amount', 'Invalid amount', is_agent)
    print 'Deposit successful'
    return ['deposit', account_number, amount]


def create():
    """
    Collect the arguments for a "create" command.
    """
    account_number = prompt_for_account_number('Account number', 'Invalid account number', False)
    account_name = prompt_for_account_name('Account name', 'Invalid account name')
    print 'Account creation successful'
    return ['create', account_number, account_name]


def delete():
    """
    Collect the arguments for a "delete" command.
    """
    account_number = prompt_for_account_number('Account number', 'Invalid account number')
    account_name = prompt_for_account_name('Account name', 'Invalid account name')
    print 'Account deletion successful'
    return ['delete', account_number, account_name]
