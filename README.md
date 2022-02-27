# RobotChallenge

Robot Challenge

--------------------------------------------------------------------------------
## Summary


An attempt at Robot Challenge.

--------------------------------------------------------------------------------
## How to Install


    git clone 
    pip install -r requirements.txt
    pip install -e .

--------------------------------------------------------------------------------
## Running Software 


    robotchallenge --help
    robotchallenge -f "`pwd`/tests/test_data/sample_problems.txt"


--------------------------------------------------------------------------------
## Running Software in Docker 
    
    # building image locally
    docker build -t robotchallenge .

    # printing help
    docker run -it --rm robotchallenge -h

    # using existing test file 
    docker run -it --rm robotchallenge -f "/app/tests/test_data/sample_problems.txt"
    
    # using new test file 
    docker run -it --rm -v "`pwd`/tests/test_data/sample_problems.txt":"/app/tests/test_data/sample_problems.txt" robotchallenge -f "/app/tests/test_data/sample_problems.txt"
    

--------------------------------------------------------------------------------    
### Running Testing


    pytest -rx -s tests