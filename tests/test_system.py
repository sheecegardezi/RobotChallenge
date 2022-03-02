import sys
import pytest
from pathlib import Path
from .tests_constants import PROJECT_ROOT_FOLDER, PATH_TO_SAMPLE_PROBLEM_FILE
from robotchallenge.constants import ROTATE_DIRECTIONS, DIRECTIONS, DIRECTION_STEP_MAPPING, DIRECTION_ROTATION_MAPPING
import logging

LOG_FILE = "test.log"
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename=LOG_FILE,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@pytest.mark.incremental
class TestSystemSanity:

    def test_complete_system_run(self):

        assert True
