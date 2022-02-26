ROTATE_DIRECTIONS = [
    "LEFT",
    "RIGHT"
]

DIRECTIONS = [
    "NORTH",
    "EAST",
    "SOUTH",
    "WEST"
]

DIRECTION_STEP_MAPPING = {
    "NORTH": (0, 1),
    "EAST": (1, 0),
    "SOUTH": (0, -1),
    "WEST": (-1, 0),
}

DIRECTION_ROTATION_MAPPING = {
    "NORTH": {
        "LEFT": "WEST",
        "RIGHT": "EAST"
    },
    "EAST": {
        "LEFT": "NORTH",
        "RIGHT": "SOUTH"

    },
    "WEST": {
        "LEFT": "SOUTH",
        "RIGHT": "NORTH"
    },
    "SOUTH": {
        "LEFT": "EAST",
        "RIGHT": "WEST"
    }
}
