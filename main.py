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

import io
import validation


def parse_line(line):
    """
    Split a line of input by spaces, normalizing the command parameter.
    """
    line_parts = line.strip().split()
    if len(line_parts) > 0:
        line_parts[0] = line_parts[0].lower()
    else:
        line_parts = ['']
    return line_parts


def prompt_for_input():
    """
    Prompt the user for input and return their response (with whitespace trimmed).
    """
    return raw_input('> ').strip()


def run_agent_mode():
    """
    Prompt the user for commands and listen for the response.
    Commands are run with agent parameters and limitations.
    When the "logout" command is given, this function returns.
    """
    print 'Logged in as agent'
    records = []
    while True:
        args = parse_line(prompt_for_input())
        if args[0] == 'logout':
            io.write_summary_file(records)
            print 'Logged out'
            return
        elif args[0] == 'transfer':
            problem = validation.validate_transfer(args, True)
            if problem:
                print problem
            else:
                records.append(args)
        elif args[0] == 'withdraw':
            problem = validation.validate_withdrawal(args, True)
            if problem:
                print problem
            else:
                records.append(args)
        elif args[0] == 'deposit':
            problem = validation.validate_deposit(args, True)
            if problem:
                print problem
            else:
                records.append(args)
        elif args[0] == 'create':
            # Flatten elements 2..end into element 2 (for spaces in names)
            args = args[:2] + [" ".join(args[2:])]
            problem = validation.validate_creation(args)
            if problem:
                print problem
            else:
                records.append(args)
        elif args[0] == 'delete':
            # Flatten elements 2..end into element 2 (for spaces in names)
            args = args[:2] + [" ".join(args[2:])]
            problem = validation.validate_deletion(args)
            if problem:
                print problem
            else:
                records.append(args)
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
    while True:
        args = parse_line(prompt_for_input())
        if args[0] == 'logout':
            io.write_summary_file(records)
            print 'Logged out'
            return
        elif args[0] == 'transfer':
            problem = validation.validate_transfer(args, False)
            if problem:
                print problem
            else:
                records.append(args)
        elif args[0] == 'withdraw':
            problem = validation.validate_withdrawal(args, False)
            if problem:
                print problem
            else:
                records.append(args)
        elif args[0] == 'deposit':
            problem = validation.validate_deposit(args, False)
            if problem:
                print problem
            else:
                records.append(args)
        elif args[0] == 'create':
            print 'Error: privileged command'
        elif args[0] == 'delete':
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
        prompt = prompt_for_input().lower()
        if prompt == 'login':
            while True:
                print 'Log in as ATM or agent?'
                mode_prompt = prompt_for_input().lower()
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
