from robotchallenge.Board.board import Board
from robotchallenge.Robot.robot import Robot
from robotchallenge.Compiler.compiler import Compiler
from robotchallenge.Simulator.simulator import Simulator


def test_simulator():
    # Create a new board
    board_size = 5
    board = Board(board_size)

    # Create a new robot
    x_coordinate, y_coordinate = 0, 0  # starting position
    direction_facing = 'NORTH'  # starting direction
    robot = Robot(x_coordinate, y_coordinate, direction_facing)

    # Create a new compiler
    commands_string = """PLACE 1,2,EAST
    MOVE
    MOVE
    LEFT
    MOVE
    REPORT"""

    compiler = Compiler(commands_string)
    compiler.compile()
    commands = compiler.get_instructions()

    # Create a new simulator
    simulator = Simulator(board, robot, commands)
    simulator.run()

    assert "Output: 3,3,NORTH" == simulator.get_result()


if __name__ == "__main__":
    test_simulator()
    print("All tests passed")
