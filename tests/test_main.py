import pathlib
import subprocess


def test_main():

    # Test that the main function with correct arguments
    input_problem_file = str(pathlib.Path(__file__).parent.parent / 'tests' / 'test_data' / 'sample_problems.txt')
    result = subprocess.run(
        f"python3 -m robotchallenge --file {input_problem_file} --log CRITICAL",
        shell=True, check=True, capture_output=True, text=True
    )

    assert result.stdout.strip() == "Output: 3,3,NORTH"

    # Test that the main function with invalid arguments
    invalid_input_problem_file = str(pathlib.Path(__file__).parent.parent / 'tests' / 'test_data' / 'invalid_file.txt')

    try:
        subprocess.run(
            f"python3 -m robotchallenge --file {invalid_input_problem_file} --log CRITICAL",
            shell=True, check=True, capture_output=True, text=True
        )
        assert False, "Should not reach here"
    except subprocess.CalledProcessError as err:
        assert "invalid_file.txt does not exist" in err.stderr


if __name__ == "__main__":
    test_main()
    print("All tests passed")
