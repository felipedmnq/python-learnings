## Unit Tests with Pytest

### What is unit testing?

- Automated tests (usualy functions) that you can write and run to check if your source code is working as intended.
- By running the tests, it's a good (best practice) and fast way to automatically check the entirety of your application.

### Pytest framework

[**pytest docs**](https://docs.pytest.org/en/7.4.x/)

- The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

#### Installation

- `pip install -U pytest`
- `poetry add pytest`

#### How does it works?

- Pytest will discover tests in your project by the name pattern.
- Pytest will identify all files whose names follow the form `test_*.py` or `\*_test.py`` in the current directory and its subdirectories.
- To be able to identify a test inside a test file, it is necessary to be present in the file a function with the prefix `test_<test name>` or the sufix `<test name>_test`.
- In pytest, each unit test is a function.
- It is best practice to name the test functions as most descriptive as possible. e.g: `test_can_add_item_to_shopping_cart()` - this test will validate if the function `add_item` can properly add an item to the shopping cart as it is expected to do.

##### Test Exceptions

- The test passes if an exception is raised, in other words, pytest pass the test if the test fails 🤯.
- `pytest.raises(<Exception type>)`.

#### Commands

- `pytest` - runs all the unit tests it can find.
- `pytest <test file name>.py` - runs all tests in this specific file.
- `pytest <test file name>.py::<test function to be tested>` - runs a specific test fuction inside a specific test file.
- `pytest -s <test file name>.py::<test function to be tested>` - to show the outputs (prints) of the test.
- `pytest -v <test file name>.py::<test function to be tested>` - to have the test verbose.





