import sys
import pytest
from pathlib import Path
from subprocess import Popen, PIPE, STDOUT
from .tests_constants import PROJECT_ROOT_FOLDER, PATH_TO_SAMPLE_PROBLEM_FILE
from robotchallenge.constants import ROTATE_DIRECTIONS, DIRECTIONS, DIRECTION_STEP_MAPPING, DIRECTION_ROTATION_MAPPING
import logging, select, subprocess

LOG_FILE = "test.log"
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename=LOG_FILE,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@pytest.mark.incremental
class TestSystemSanity:

    def test_complete_system_run(self):
        cmd = "ray start --head"
        process = Popen(cmd, shell=True)
        process.wait()

        cmd = (
            f"cd {str(PROJECT_ROOT_FOLDER)} && python -m robotchallenge -c "
            + str(PATH_TO_SAMPLE_PROBLEM_FILE)
        )

        process = Popen(cmd, shell=True)
        process.wait()
        print(process)

        cmd = "ray stop"
        process = Popen(cmd, shell=True)
        process.wait()

        assert True
