# RobotChallenge
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![codecov](https://codecov.io/gh/sheecegardezi/RobotChallenge/branch/main/graph/badge.svg?token=YR125ZTT27)](https://codecov.io/gh/sheecegardezi/RobotChallenge)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub release](https://img.shields.io/github/release/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/releases/)


Robot Challenge

--------------------------------------------------------------------------------
## Summary


An attempt at Robot Challenge.

--------------------------------------------------------------------------------
## How to Install


    git clone https://github.com/sheecegardezi/RobotChallenge.git
    cd RobotChallenge
    pip install -r requirements.txt
    pip install -e .

--------------------------------------------------------------------------------
## Running Software Locally


    robotchallenge --help
    robotchallenge -f "`pwd`/tests/test_data/sample_problems.txt"


--------------------------------------------------------------------------------
## Running Software in Docker 

    # clone repo
    git clone https://github.com/sheecegardezi/RobotChallenge.git
    cd RobotChallenge
    
    # building image locally
    docker build -t robotchallenge .

    # printing help
    docker run -it --rm robotchallenge -h

    # using existing test file 
    docker run -it --rm robotchallenge -f "/app/tests/test_data/sample_problems.txt"
    
    # using new test file 
    docker run -it --rm -v "`pwd`/tests/test_data/sample_problems.txt":"/app/tests/test_data/sample_problems.txt" robotchallenge -f "/app/tests/test_data/sample_problems.txt"
    


--------------------------------------------------------------------------------
## Running Software using prebaked Docker Image


    # pulling image from repo
    docker image pull sheecegardezi/robotchallenge:latest

    # printing help
    docker run -it --rm sheecegardezi/robotchallenge:latest -h

    # using existing test file 
    docker run -it --rm sheecegardezi/robotchallenge:latest -f "/app/tests/test_data/sample_problems.txt"

    # using new test file 
    docker run -it --rm -v "`pwd`/tests/test_data/sample_problems.txt":"/app/tests/test_data/sample_problems.txt" sheecegardezi/robotchallenge:latest -f "/app/tests/test_data/sample_problems.txt"

--------------------------------------------------------------------------------    
### Running Testing

    pytest --cov=robotchallenge -rx -s tests
