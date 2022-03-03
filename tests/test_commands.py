from robotchallenge.Commands.command import Command
from robotchallenge.Commands.utlities import create_command


def test_commands():
    command = Command("SOME_CMD", **{"SOME_ARG_1": "SOME_VALUE_1", "SOME_ARG_2": "SOME_VALUE_2"})

    assert str(
        command) == "Command(command=SOME_CMD, kwargs=({'SOME_ARG_1': 'SOME_VALUE_1', 'SOME_ARG_2': 'SOME_VALUE_2'}))"
    assert command.get_command() == "SOME_CMD"
    assert command.get_argument("SOME_ARG_1") == "SOME_VALUE_1"
    assert command == "SOME_CMD"
    command.set_argument("SOME_ARG_1", "SOME_NEW_VALUE_1")
    assert command.get_argument("SOME_ARG_1") == "SOME_NEW_VALUE_1"

    command = create_command("PLACE", *[1, 2, "EAST"])

    assert str(
        command) == "Command(command=PLACE, kwargs=({'x_coordinate': 1, 'y_coordinate': 2, 'direction': 'EAST'}))"
    assert command.get_command() == "PLACE"
    assert command.get_argument("x_coordinate") == 1
    assert command == "PLACE"
    command.set_argument("x_coordinate", 2)
    assert command.get_argument("x_coordinate") == 2


if __name__ == "__main__":
    test_commands()
    print("All tests passed")
