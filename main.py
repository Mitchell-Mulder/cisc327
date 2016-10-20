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


def run_agent_mode():
    """
    Prompt the user for commands and listen for the response.
    Commands are run with agent parameters and limitations.
    When the "logout" command is given, this function returns.
    """
    print 'Logged in as agent'
    records = []
    while True:
        line = io.prompt_for_input().lower()
        if line == 'logout':
            io.write_summary_file(records)
            print 'Logged out'
            return
        elif line == 'transfer':
            records.append(commands.transfer(True))
        elif line == 'withdraw':
            records.append(commands.withdraw(True))
        elif line == 'deposit':
            records.append(commands.deposit(True))
        elif line == 'create':
            records.append(commands.create())
        elif line == 'delete':
            records.append(commands.delete())
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
            io.write_summary_file(records)
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


run_main_loop()
