import sys
import re


def account_number_exists(account_num):
    """
    Check whether an account number exists in the accounts list file.
    Returns True if the account number is found, and False otherwise.
    """
    try:
        account_num = int(account_num)
        with open(sys.argv[1]) as account_file:
            for existing in account_file:
                if account_num == int(existing):
                    return True

            return False
    except ValueError:
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
    m = re.search('^[a-zA-Z0-9 ]{3,30}$', name)
    if m is None:
        return False
    else:
        return True


def validate_amount(num, is_agent=False, session_withdrawals=0):
    """
    Validate an amount parameter.
    If is_agent is True, the range of valid amounts is < $1M.
    If is_agent is False, the range of valid amounts is < $10k.
    """
    try:
        num = int(num)
        if num < 0:
            return False
        elif (not is_agent) and num + session_withdrawals > 100000:
            return False
        elif is_agent and num > 99999999:
            return False
        else:
            return True
    except ValueError:
        return False


def validate_deleted(account_num, deleted_accounts):
    for i in range(0, len(deleted_accounts)):
        if account_num == deleted_accounts[i]:
            return False
    return True
