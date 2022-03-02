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
from robotchallenge.constants import SIZE_OF_BOARD, STARTING_POSITION, STARTING_DIRECTION


def validate_file(file_path: str) -> Optional[str]:
    """
    Validate that the file exists
    :param file_path: file path
    :return: raise error if file does not exist or return file path
    """
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError("{0} does not exist".format(file_path))
    return file_path


def main() -> None:
    """
    Main function
    :return: None
    """
    # Record start time
    start_experiment_time = time.time()
    # Debugging
    # sys.argv.append("-h")
    # sys.argv.append("--log")
    # sys.argv.append("DEBUG")
    # sys.argv.append("--file")
    # sys.argv.append(str(pathlib.Path(__file__).parent.parent / 'tests' / 'test_data' / 'sample_problems.txt'))
    # Setup argument parser and parse arguments
    parser = argparse.ArgumentParser(prog=f"{__app_name__}",
                                     epilog='Raise issue at https://github.com/sheecegardezi/RobotChallenge/issues',
                                     description=f"{__app_name__} v{__version__}")
    parser.add_argument("-f", "--file", type=validate_file, help="input file", metavar="FILE", required=True)
    parser.add_argument("-l", "--log", type=str.upper, default="INFO", dest="logLevel",
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help="Set the logging level",
                        required=False)

    args = parser.parse_args()
    # Setup logging
    if args.logLevel:
        logging.basicConfig(level=getattr(logging, args.logLevel))
        logging.debug(f"Logging level set to {args.logLevel}")

    logging.debug(f"Running {__app_name__} v{__version__}")

    # Run main program logic if file exists
    if args.file:
        logging.debug(f"args.file: {args.file}")

        # Create a new board
        board_size = SIZE_OF_BOARD
        board = Board(board_size)
        logging.debug(f"board: {board}")

        # Create a new robot
        x_coordinate, y_coordinate = STARTING_POSITION  # starting position
        direction_facing = STARTING_DIRECTION  # starting direction
        robot = Robot(x_coordinate, y_coordinate, direction_facing)
        logging.debug(f"robot: {robot}")

        # Create a new compiler
        compiler = Compiler(file_path=args.file)
        compiler.compile()
        commands = compiler.get_instructions()
        logging.debug(f"commands: {commands}")

        # Create a new simulator
        simulator = Simulator(board, robot, commands)
        simulator.run()
        logging.debug(f"simulator: {simulator}")

    # Record end time
    logging.debug("Time take to complete experiment: %s seconds" % (time.time() - start_experiment_time))
    logging.debug(f"Finished {__app_name__} v{__version__}")


if __name__ == "__main__":
    """
    Main Function
    """
    main()
