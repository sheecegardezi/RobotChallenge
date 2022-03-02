from robotchallenge.Commands.command import Command
from robotchallenge.constants import COMMANDS
from typing import List


def create_command(command: str, *args: List[str]) -> Command:
    """
    Creates a command object from a command string and arguments.
    :param command: string
    :param args: list of strings
    :return: Command object
    """

    if len(args) != len(COMMANDS[command]):
        raise ValueError(f'Missing arguments for: {command} provided: {args}')

    # traverse over all possible arguments using the command dictionary
    # and type cast the string tokens to appropriate data types
    # and add arguments to a dictionary
    arguments = {
        argument: COMMANDS[command][argument](args[i])
        for i, argument in enumerate(COMMANDS[command])
    }

    return Command(command, **arguments)
