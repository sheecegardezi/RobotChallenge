from robotchallenge.Robot.robot import Robot
from robotchallenge.Robot.robot import RobotTypeError
from robotchallenge.Direction.direction import Direction


def test_robot():
    x_coordinate, y_coordinate, direction_facing = 0, 0, Direction('NORTH').direction
    robot = Robot(x_coordinate, y_coordinate, direction_facing)

    assert robot.x_coordinate == x_coordinate
    assert robot.y_coordinate == y_coordinate
    assert robot.direction_facing == direction_facing

    robot.move()
    assert robot.x_coordinate == x_coordinate
    assert robot.y_coordinate == y_coordinate + 1
    assert robot.direction_facing == direction_facing



if __name__ == "__main__":
    test_robot()
    print("All tests passed")
