class Command:
    def __init__(self, command, **kwargs):
        self.command = command
        self.kwargs = kwargs

    def get_command(self):
        return self.command

    def set_argument(self, argument, value):
        self.kwargs[argument] = value

    def get_argument(self, argument):
        return self.kwargs[argument]

    def __str__(self):
        return f'Command(command={self.command}, kwargs=({self.kwargs}))'

    def __repr__(self):
        return f'Command(command={self.command}, kwargs=({self.kwargs}))'

    def __eq__(self, other):
        return self.command == other.command

    def __hash__(self):
        return self.command.__hash__()
