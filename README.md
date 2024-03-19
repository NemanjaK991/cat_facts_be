# Python Backend Testing Project

This project demonstrates API testing using Python's `requests` module along with `pytest`.

## Installation

1. Clone the repository:

```
git clone git@github.com:NemanjaK991/cat_facts_be.git
```


2. Navigate to the project directory:
```
cd cat_facts_be
```

3. Install the required dependencies:

```
pip install -r backend\requirements.txt
```

## Running Tests

To run the tests, execute the following command in the project directory:
```
pytest -s backend\rest\cat_facts_pytest\test\test_facts.py
```

## Test Cases

Below is a table representing various test cases and their expected results:

| Test Case                   | Endpoint      | Parameters               | Assertion                                          | Expected Status Code |
|-----------------------------|---------------|--------------------------|----------------------------------------------------|----------------------|
| Test GET request            | /facts/random | -                        | Status code, reponse is not empty                  | 200                  |
| Test GET request            | /facts/random | animal_type=cat&amount=3 | Status code, number of retrieved facts, type value | 200                  |

## Additional Information

- `backend/rest/cat_facts_pytest/test`: Contains test files written using `pytest`.
- `backend/rest/common/helpers.py`: Contains common functions needed for sending and validating a http request.
- `requirements.txt`: Contains a list of Python dependencies required for this project.
- `README.md`: This file, containing project information, installation steps, and test case details.
