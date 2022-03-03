from robotchallenge.Board.board import Board
from robotchallenge.Robot.robot import Robot
from robotchallenge.Compiler.compiler import Compiler
from robotchallenge.Simulator.simulator import Simulator
from robotchallenge.Simulator.utilities import get_output_string
from math import floor
# import multiprocessing
# from multiprocessing import Process, Pipe


def run_simulation(board_size):
    if floor(board_size / 2) == 0:
        return 0

    # Create a new board
    board = Board(board_size)

    # Create a new robot
    x_coordinate, y_coordinate = 0, 0  # starting position
    direction_facing = 'EAST'  # starting direction
    robot = Robot(x_coordinate, y_coordinate, direction_facing)

    commands_string = (
            f"PLACE {x_coordinate},{y_coordinate},{direction_facing}" + "\n"
    )

    for _ in range(floor(board_size / 2)):
        commands_string += "MOVE" + "\n"
    commands_string += "LEFT" + "\n"

    for _ in range(floor(board_size / 2)):
        commands_string += "MOVE" + "\n"

    # Compile the commands
    compiler = Compiler(commands_string)
    compiler.compile()

    # Execute the commands
    simulator = Simulator(board, robot, compiler.get_instructions())
    simulator.run()

    assert get_output_string(floor(board_size / 2), floor(board_size / 2), "NORTH") == simulator.get_result()
    return 1


def test_simulation():
    # pool = multiprocessing.Pool()
    # pool.map(run_simulation, range(2, 100))
    # pool.close()
    for board_size in range(2, 100):
        run_simulation(board_size)


if __name__ == "__main__":
    test_simulation()
    print("All tests passed")
