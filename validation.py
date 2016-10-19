def validate_transfer(args, is_agent):
    """
    
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
    if not len(args) == 3:
        return 'Error: Invalid number of arguments'
    elif not validate_account_number(args[1]):
        return 'Error: Invalid account number'
    elif not validate_amount(args[2], is_agent):
        return 'Error: Invalid amount'
    else:
        return ''


def validate_deposit(args, is_agent):
    if not len(args) == 3:
        return 'Error: Invalid number of arguments'
    elif not validate_account_number(args[1]):
        return 'Error: Invalid account number'
    elif not validate_amount(args[2], is_agent):
        return 'Error: Invalid amount'
    else:
        return ''


def validate_creation(args):
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
    account_num = int(account_num)

    with open('accounts.txt') as account_file:
        for existing in account_file:
            if account_num == int(existing):
                return True

        return False


def validate_account_number(num, should_exist=True):
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
    name = name.strip()
    if len(name) > 30 or len(name) < 3:
        return False
    else:
        return True


def validate_amount(num, is_agent=False):
    num = int(num)
    if num < 0:
        return False
    elif (not is_agent) and num > 1000000:
        return False
    elif is_agent and num > 99999999:
        return False
    else:
        return True
