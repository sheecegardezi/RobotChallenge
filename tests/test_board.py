from robotchallenge.Board.board import Board


def test_board():
    size = 3
    board = Board(size)

    assert board.position_on_board(0, 0) == True, "Should be True"
    assert board.position_on_board(0, size) == False, "Should be False"
    assert board.position_on_board(size, 0) == False, "Should be False"
    assert board.position_on_board(size, size) == False, "Should be False"
    assert board.position_on_board(size + 1, size) == False, "Should be False"
    assert board.position_on_board(size, size + 1) == False, "Should be False"
    assert board.position_on_board(size + 1, size + 1) == False, "Should be False"

    for i in range(size):
        for j in range(size):
            assert board.position_on_board(i, j) == True, "Should be True"


if __name__ == "__main__":
    test_board()
    print("All tests passed")
