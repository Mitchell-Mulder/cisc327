def validate_transfer(args, is_agent):
    """
    Validate the arguments for a "transfer" command.
    """
    if not len(args) == 4:
        return 'Error: Invalid number of arguments'
    elif not validate_account_number(args[1]):
        return 'Error: Invalid first account number'
    elif not validate_account_number(args[2]):
        return 'Error: Invalid second account number'
    elif not validate_amount(args[3], is_agent):
        return 'Error: Invalid amount'
    else:
        return ''


def validate_withdrawal(args, is_agent):
    """
    Validate the arguments for a "withdraw" command.
    """
    if not len(args) == 3:
        return 'Error: Invalid number of arguments'
    elif not validate_account_number(args[1]):
        return 'Error: Invalid account number'
    elif not validate_amount(args[2], is_agent):
        return 'Error: Invalid amount'
    else:
        return ''


def validate_deposit(args, is_agent):
    """
    Validate the arguments for a "deposit" command.
    """
    if not len(args) == 3:
        return 'Error: Invalid number of arguments'
    elif not validate_account_number(args[1]):
        return 'Error: Invalid account number'
    elif not validate_amount(args[2], is_agent):
        return 'Error: Invalid amount'
    else:
        return ''


def validate_creation(args):
    """
    Validate the arguments for a "create" command.
    """
    if len(args) < 3:
        return 'Error: Invalid number of arguments'
    elif not validate_account_number(args[1], False):
        return 'Error: Invalid account number'
    elif account_number_exists(args[1]):
        return 'Error: Account number already in use'
    elif not validate_name(args[2]):
        return 'Error: Invalid account name'
    else:
        return ''


def validate_deletion(args):
    """
    Validate the arguments for a "delete" command.
    """
    if len(args) < 3:
        return 'Error: Invalid number of arguments'
    elif not validate_account_number(args[1]):
        return 'Error: Invalid account number'
    elif not account_number_exists(args[1]):
        return 'Error: Account with that number does not exist'
    elif not validate_name(args[2]):
        return 'Error: Invalid account name'
    else:
        return ''


def account_number_exists(account_num):
    """
    Check whether an account number exists in the accounts list file.
    Returns True if the account number is found, and False otherwise.
    """
    account_num = int(account_num)

    with open('accounts.txt') as account_file:
        for existing in account_file:
            if account_num == int(existing):
                return True

        return False


def validate_account_number(num, should_exist=True):
    """
    Validate an account number parameter.
    If should_exist is True, the account number is expected to be in
        the accounts list and will only be considered valid if so.
    If should_exist is False, the account number is expected not to be
        in the accounts list, and will be considered invalid if so.
    """
    if len(num) != 8:
        return False
    elif num[0] == '0':
        return False
    else:
        if should_exist:
            return account_number_exists(num)
        else:
            return not account_number_exists(num)


def validate_name(name):
    """
    Validate an account name parameter.
    """
    name = name.strip()
    if len(name) > 30 or len(name) < 3:
        return False
    else:
        return True


def validate_amount(num, is_agent=False):
    """
    Validate an amount parameter.
    If is_agent is True, the range of valid amounts is < $1M.
    If is_agent is False, the range of valid amounts is < $10k.
    """
    num = int(num)
    if num < 0:
        return False
    elif (not is_agent) and num > 1000000:
        return False
    elif is_agent and num > 99999999:
        return False
    else:
        return True
