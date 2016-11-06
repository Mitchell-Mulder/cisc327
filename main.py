#!/usr/bin/env python

"""

CISC 327 Assignment 2

Brandon Bloch (10052759),
Bryce Marshall (10113902),
Mitchell Mulder (10137002)


This program loops indefinitely on start,
waiting for the "login" command. When the
user logs in (either to ATM or agent mode),
the respective mode then loops indefinitely
waiting for further transaction commands
until the "logout" command is given. At
this point, the transaction summary log
is written.

"""

import commands
import io
import sys
import validation


def run_agent_mode():
    """
    Prompt the user for commands and listen for the response.
    Commands are run with agent parameters and limitations.
    When the "logout" command is given, this function returns.
    """
    print 'Logged in as agent'
    records = []
    deleted_accounts = []
    while True:
        line = io.prompt_for_input().lower()
        if line == 'logout':
            io.write_summary_file(records, sys.argv[2])
            print 'Logged out'
            return
        elif line == 'transfer':
            tmp_transfer = commands.transfer(True)
            if (validation.validate_deleted(tmp_transfer[1], deleted_accounts) or
                    validation.validate_deleted(tmp_transfer[2], deleted_accounts)):
                records.append(tmp_transfer)
                print 'Transfer successful'
            else:
                print 'Error: Account does not exist'
        elif line == 'withdraw':
            tmp_withdraw = commands.withdraw(True, {})
            if validation.validate_deleted(tmp_withdraw[1], deleted_accounts):
                records.append(tmp_withdraw)
                print 'Withdraw successful'
            else:
                print 'Error: Account does not exist'
        elif line == 'deposit':
            tmp_deposit = commands.deposit(True)
            if validation.validate_deleted(tmp_deposit[1], deleted_accounts):
                records.append(tmp_deposit)
                print 'Deposit successful'
            else:
                print 'Error: Account does not exist'
        elif line == 'create':
            records.append(commands.create())
        elif line == 'delete':
            tmp_delete = commands.delete()
            records.append(tmp_delete)
            deleted_accounts.append(tmp_delete[1])
        else:
            print 'Error: command not recognized'


def run_atm_mode():
    """
    Prompt the user for commands and listen for the response.
    Commands are run with ATM parameters and limitations.
    When the "logout" command is given, this function returns.
    """
    print 'Logged in as ATM'
    records = []
    withdrawals = {}
    while True:
        line = io.prompt_for_input().lower()
        if line == 'logout':
            io.write_summary_file(records, sys.argv[2])
            print 'Logged out'
            return
        elif line == 'transfer':
            records.append(commands.transfer(False))
        elif line == 'withdraw':
            result = commands.withdraw(False, withdrawals)
            records.append(result)
            if result[1] in withdrawals:
                withdrawals[result[1]] += result[2]
            else:
                withdrawals[result[1]] = result[2]
        elif line == 'deposit':
            records.append(commands.deposit(False))
        elif line == 'create':
            print 'Error: privileged command'
        elif line == 'delete':
            print 'Error: privileged command'
        else:
            print 'Error: command not recognized'


def run_main_loop():
    """
    Prompt the user for input.
    This loop waits for the "login" and "atm" or "agent"
    commands, and begins the respective mode.
    """
    while True:
        try:
            prompt = io.prompt_for_input().lower()
            if prompt == 'login':
                while True:
                    print 'Log in as ATM or agent?'
                    mode_prompt = io.prompt_for_input().lower()
                    if mode_prompt == 'atm':
                        run_atm_mode()
                        break
                    elif mode_prompt == 'agent':
                        run_agent_mode()
                        break
                    else:
                        print 'Error: invalid mode'
            else:
                print 'Error: command not recognized'
        except EOFError:
            return


if __name__ == "__main__":
    run_main_loop()
