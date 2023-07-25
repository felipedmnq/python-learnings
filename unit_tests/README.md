# Unit Tests with Pytest

## What is unit testing?

- Automated tests (usualy functions) that you can write and run to check if your source code is working as intended.
- By running the tests, it's a good (best practice) and fast way to automatically check the entirety of your application.

## Pytest framework

[**pytest docs**](https://docs.pytest.org/en/7.4.x/)

- The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

### Installation

- `pip install -U pytest`
- `poetry add pytest`

### How does it works?

- Pytest will discover tests in your project by the name pattern.
- Pytest will identify all files whose names follow the form `test_*.py` or `\*_test.py`` in the current directory and its subdirectories.
- To be able to identify a test inside a test file, it is necessary to be present in the file a function with the prefix `test_<test name>` or the sufix `<test name>_test`.
- In pytest, each unit test is a function.
- It is best practice to name the test functions as most descriptive as possible. e.g: `test_can_add_item_to_shopping_cart()` - this test will validate if the function `add_item` can properly add an item to the shopping cart as it is expected to do.

#### Anatomy of a test

- From docs:

"In the simplest terms, a test is meant to look at the result of a particular behavior, and make sure that result aligns with what you would expect. Behavior is not something that can be empirically measured, which is why writing tests can be challenging.

“Behavior” is the way in which some system acts in response to a particular situation and/or stimuli. But exactly how or why something is done is not quite as important as what was done.

You can think of a test as being broken down into four steps:

- Arrange
- Act
- Assert
- Cleanup

Arrange is where we prepare everything for our test. This means pretty much everything except for the “act”. It’s lining up the dominoes so that the act can do its thing in one, state-changing step. This can mean preparing objects, starting/killing services, entering records into a database, or even things like defining a URL to query, generating some credentials for a user that doesn’t exist yet, or just waiting for some process to finish.

Act is the singular, state-changing action that kicks off the behavior we want to test. This behavior is what carries out the changing of the state of the system under test (SUT), and it’s the resulting changed state that we can look at to make a judgement about the behavior. This typically takes the form of a function/method call.

Assert is where we look at that resulting state and check if it looks how we’d expect after the dust has settled. It’s where we gather evidence to say the behavior does or does not aligns with what we expect. The assert in our test is where we take that measurement/observation and apply our judgement to it. If something should be green, we’d say assert thing == "green".

Cleanup is where the test picks up after itself, so other tests aren’t being accidentally influenced by it.

At its core, the test is ultimately the act and assert steps, with the arrange step only providing the context. Behavior exists between act and assert."

#### Test Exceptions

- The test passes if an exception is raised, in other words, pytest pass the test if the test fails 🤯.
- `pytest.raises(<Exception type>)`.

#### Pytest.fixtures

- `pytest.fixtures` - used to avoid repeated code.
- From docs: 

"In testing, a fixture provides a defined, reliable and consistent context for the tests. This could include environment (for example a database configured with known parameters) or content (such as a dataset).

Fixtures define the steps and data that constitute the arrange phase of a test (see Anatomy of a test). In pytest, they are functions you define that serve this purpose. They can also be used to define a test’s act phase; this is a powerful technique for designing more complex tests.

The services, state, or other operating environments set up by fixtures are accessed by test functions through arguments. For each fixture used by a test function there is typically a parameter (named after the fixture) in the test function’s definition."

#### Mock dependencies

- Create fake behaviors to be used in unit tests.
- [unittest mock docs](https://docs.python.org/3/library/unittest.mock.html)
- `unittest.mock` from docs:

"Library that allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.

unittest.mock provides a core Mock class removing the need to create a host of stubs throughout your test suite. After performing an action, you can make assertions about which methods / attributes were used and arguments they were called with. You can also specify return values and set needed attributes in the normal way.

Additionally, mock provides a patch() decorator that handles patching module and class level attributes within the scope of a test, along with sentinel for creating unique objects. See the quick guide for some examples of how to use Mock, MagicMock and patch()."



### Commands

- `pytest` - runs all the unit tests it can find.
- `pytest <test file name>.py` - runs all tests in this specific file.
- `pytest <test file name>.py::<test function to be tested>` - runs a specific test fuction inside a specific test file.
- `pytest -s <test file name>.py::<test function to be tested>` - to show the outputs (prints) of the test.
- `pytest -v <test file name>.py::<test function to be tested>` - to have the test verbose.





