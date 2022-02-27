from typing import Optional
import argparse
import os
import sys
import logging
import pathlib
import time

from robotchallenge import __app_name__, __version__

from robotchallenge.Board.board import Board
from robotchallenge.Robot.robot import Robot
from robotchallenge.Compiler.compiler import Compiler
from robotchallenge.Simulator.simulator import Simulator


def validate_file(f):
    if not os.path.isfile(f):
        raise argparse.ArgumentTypeError("{0} does not exist".format(f))
    return f


def main():
    start_experiment_time = time.time()
    # Debugging
    # sys.argv.append("-h")
    # sys.argv.append("--log")
    # sys.argv.append("DEBUG")
    # sys.argv.append("--file")
    # sys.argv.append(str(pathlib.Path(__file__).parent.parent / 'tests' / 'test_data' / 'sample_problems.txt'))

    parser = argparse.ArgumentParser(prog=f"{__app_name__}",
                                     epilog='Raise issue at https://github.com/sheecegardezi/RobotChallenge/issues',
                                     description=f"{__app_name__} v{__version__}")
    parser.add_argument("-f", "--file", type=validate_file, help="input file", metavar="FILE", required=True)
    parser.add_argument("-l", "--log", type=str.upper, default="INFO", dest="logLevel",
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help="Set the logging level",
                        required=False)

    args = parser.parse_args()

    if args.logLevel:
        logging.basicConfig(level=getattr(logging, "DEBUG"))

    logging.debug(f"Running {__app_name__} v{__version__}")

    if args.file:
        logging.debug(f"args.file: {args.file}")

        # Create a new board
        board_size = 5
        board = Board(board_size)
        logging.debug(f"board: {board}")

        # Create a new robot
        x_coordinate, y_coordinate = 0, 0  # starting position
        direction_facing = 'NORTH'  # starting direction
        robot = Robot(x_coordinate, y_coordinate, direction_facing)
        logging.debug(f"robot: {robot}")

        # Create a new compiler
        compiler = Compiler(file_path=args.file)
        compiler.compile()
        commands = compiler.get_commands()
        logging.debug(f"commands: {commands}")

        # Create a new simulator
        simulator = Simulator(board, robot, commands)
        simulator.run()
        logging.debug(f"simulator: {simulator}")

    logging.debug("Time take to complete experiment: %s seconds" % (time.time() - start_experiment_time))
    logging.debug(f"Finished {__app_name__} v{__version__}")


if __name__ == "__main__":
    main()
