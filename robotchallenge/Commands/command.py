from typing import Any


class Command:
    """
    This class is used to represent a command.
    """

    def __init__(self, command: str, **kwargs) -> None:
        """
        Initializes a command.
        """
        self.command = command
        self.kwargs = kwargs

    def get_command(self) -> str:
        """
        Returns the command.
        :return: The name of the command
        """
        return self.command

    def set_argument(self, argument, value) -> None:
        """
        Sets the argument to the given value.
        :param argument: name of the argument
        :param value: value of the argument
        :return: None
        """
        self.kwargs[argument] = value

    def get_argument(self, argument) -> Any[str, int]:
        """
        Returns the value of the argument
        :param argument: name of the argument
        :return: value of the argument
        """
        return self.kwargs[argument]

    def __str__(self):
        """
        Returns a string representation of the command.
        :return: string representation of the command
        """
        return f'Command(command={self.command}, kwargs=({self.kwargs}))'

    def __repr__(self):
        return f'Command(command={self.command}, kwargs=({self.kwargs}))'

    def __eq__(self, command: str) -> bool:
        """
        Returns true if the command is equal to the given command name
        :param command: name of the command
        :return: true if the command is equal to the given command name
        """
        return self.command == command

    def __hash__(self):
        """
        Returns the hash of the command.
        :return: the hash of the command
        """
        return self.command.__hash__()
