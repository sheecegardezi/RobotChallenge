from robotchallenge.Robot.robot import Robot
from robotchallenge.Robot.robot import RobotTypeError


def test_robot():
    x_coordinate, y_coordinate, direction_facing = 0, 0, 'NORTH'
    robot = Robot(x_coordinate, y_coordinate, direction_facing)

    assert robot.x_coordinate == x_coordinate
    assert robot.y_coordinate == y_coordinate
    assert robot.direction_facing == direction_facing

    robot.move()
    assert robot.x_coordinate == x_coordinate
    assert robot.y_coordinate == y_coordinate + 1
    assert robot.direction_facing == direction_facing

    robot.rotate('LEFT')
    assert robot.x_coordinate == x_coordinate
    assert robot.y_coordinate == y_coordinate + 1
    assert robot.direction_facing == 'WEST'

    robot.place(1, 2, 'SOUTH')
    assert robot.x_coordinate == 1
    assert robot.y_coordinate == 2
    assert robot.direction_facing == 'SOUTH'

    assert robot.future_position() == (1, 1)

    assert str(robot) == "Robot(x_coordinate=1, y_coordinate=2, direction_facing=SOUTH, is_placed=True)"

    try:
        robot.rotate('INVALID_DIRECTION')
        assert False, "Should not reach here"
    except RobotTypeError:

        assert True, "Should reach here"


if __name__ == "__main__":
    test_robot()
    print("All tests passed")
