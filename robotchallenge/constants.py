"""
This file contains the rules on which this abstraction of Robot Challenge is based on.
"""

SIZE_OF_BOARD = 5
STARTING_POSITION = (0, 0)
STARTING_DIRECTION = "NORTH"

ROTATE_DIRECTIONS = [
    "LEFT",
    "RIGHT",
]

DIRECTIONS = [
    "NORTH",
    "EAST",
    "SOUTH",
    "WEST",
]

DIRECTION_STEP_MAPPING = {
    "NORTH": (0, 1),
    "EAST": (1, 0),
    "WEST": (-1, 0),
    "SOUTH": (0, -1),
}

DIRECTION_ROTATION_MAPPING = {
    "NORTH": {
        "LEFT": "WEST",
        "RIGHT": "EAST",
    },
    "EAST": {
        "LEFT": "NORTH",
        "RIGHT": "SOUTH",
    },
    "WEST": {
        "LEFT": "SOUTH",
        "RIGHT": "NORTH",
    },
    "SOUTH": {
        "LEFT": "EAST",
        "RIGHT": "WEST",
    },
}

COMMANDS = {
        "PLACE": {
            "x_coordinate": int,
            "y_coordinate": int,
            "direction": str,
        },
        "MOVE": {
        },
        "LEFT": {
        },
        "RIGHT": {
        },
        "REPORT": {
        },
        "OUTPUT": {
        }
}
