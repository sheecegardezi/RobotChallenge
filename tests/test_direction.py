from robotchallenge.Direction.direction import Direction
from robotchallenge.Direction.direction import DirectionError


def test_direction():
    direction = Direction('NORTH')
    assert direction == 'TOP'
    assert direction == 'NORTH'
    assert direction != 'INVALID_DIRECTION'

    try:
        Direction("INVALID_DIRECTION")
        assert False, "Should not reach here"
    except DirectionError:
        assert True, "Should reach here"


if __name__ == "__main__":
    test_direction()
    print("All tests passed")
