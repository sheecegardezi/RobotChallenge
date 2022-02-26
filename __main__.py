from src.Board.board import Board
from src.Robot.robot import Robot
from src.Compiler.compiler import Compiler
from src.Simulator.simulator import Simulator


if __name__ == "__main__":
    # Create a new board
    board_size = 5
    board = Board(board_size)
    print("board: ", board)

    # Create a new robot
    x_coordinate, y_coordinate = 0, 0  # starting position
    direction_facing = 'NORTH'  # starting direction
    robot = Robot(x_coordinate, y_coordinate, direction_facing)
    print("robot: ", robot)

    # Create a new compiler
    commands_string = """PLACE 0,0,NORTH
    MOVE
    REPORT"""

    compiler = Compiler(commands_string)
    compiler.compile()
    commands = compiler.get_commands()
    print("compiler: ", compiler)

    # Create a new simulator
    simulator = Simulator(board, robot, commands)
    print("simulator: ", simulator)
    simulator.run()
