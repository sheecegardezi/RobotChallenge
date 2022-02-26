from src.Compiler.compiler import Compiler
from src.Compiler.compiler import CompilerError
from src.Direction.direction import Direction


def test_compiler():

    try:
        compiler = Compiler("INVALID_CMD")
        compiler.compile()
        assert False, "Should not reach here"
    except CompilerError:
        assert True, "Should reach here"


if __name__ == "__main__":
    test_compiler()
    print("All tests passed")
