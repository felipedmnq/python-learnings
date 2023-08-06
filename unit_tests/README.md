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

#### Pytest.fixtures - [DOCS](https://docs.pytest.org/en/6.2.x/reference.html#pytest-fixture)

- `pytest.fixtures` - used to avoid repeated code.
- From docs: 

"In testing, a fixture provides a defined, reliable and consistent context for the tests. This could include environment (for example a database configured with known parameters) or content (such as a dataset).

Fixtures define the steps and data that constitute the arrange phase of a test (see Anatomy of a test). In pytest, they are functions you define that serve this purpose. They can also be used to define a test’s act phase; this is a powerful technique for designing more complex tests.

The services, state, or other operating environments set up by fixtures are accessed by test functions through arguments. For each fixture used by a test function there is typically a parameter (named after the fixture) in the test function’s definition."

- To use fixtures it is applied a decorator - `@pytest.fixture` to the function that will be a fixture and after that pass the fixtured function name as an argument to the function that will be using the fixture.

```
@pytest.fixture
def some_fixture():
    pass
    
def use_fixture(some_fixture):
    pass
```
- It is also possible to use the fixture with `@pytest.mark.usefixtures("some_fixture")`. In this case the fixture name does not need to be passed to the function as an argument.
```
@pytest.mark.usefixtures("some_fixture")
def use_fixture():
    pass
```

- It is possible to set the `autouse=True` anrgument and "automatically" use the fixture for the following test functions.

- To set an alias to the fixture name - `@pytest.fixture(name="<alias>")`.

```
@pytest.fixture(name="fixture_name")
def some_fixture():
    pass
    
def use_fixture(fixture_name):
    pass

```

- To set multiple values to a fixture use `@pytest.fixture(params=(1, 2, 3, 4))` and the `request` method.

```
@pytest.fixture(params=(1, 2, 3, 4))
def some_fixture_use_params(request):
    yield request.params + 2
    
def use_fixture(some_fixture_use_params):
    pass
```

- To display the available fixtures use `pytest --fixtures <test file>.py`.


#### Skip tests

- `@pytest.mark.skip` - The function or class decorated with the skip method will not be tested.
- It is also possible to use the `pytest.skil()` method inside the test function body to skip the test during runtime.
- The `reason` argument is used to document why the test is being skipped.

```
@pytest.fixture(params=[1, 2, 3, 4])
def numbers(request):
    return request.param

@pytest.mark.skip(reason="Mehotod not implemented yet.")
def test_multiply_returns_multiplied_number(numbers):
    assert multiply(numbers) == numbers * numbers

def test_square_returns_squared_number(numbers):
    pytest.skip()
    assert square(numbers) == numbers * numbers
```

- With the decorator `pytest.mark.skipif(<boolean condition>)` it is possible to conditionally skip tests.

#### XFail tests.

- Useful for testing failure code.
- With the `@pytest.mark.xfail(reason="")` - you set the text to be expected to fail.
- Also works wit `pytest.xfail()` method inside the code body.
- Its also possible to use conditions with `@pytest.mark.xfail(<boolean condition>, reason="")` - the test will be expected to fail only if matches the condition.
- With the `raises=Exception` argument we can provide specific Exception errors that we expect to be raised during this test - `@pytest.mark.xfail(raises=AssertionError)`
- The `strict=True` argument means that you are expecting the test to fail and if the test passes, it will fail 🤯 - passing is considered a fail.

```
@pytest.mark.xfail(raises=NotImplementedError, reason="Mehotod not implemented yet.")
def test_multiply_returns_multiplied_number(numbers_1, numbers_2, expected_result):
    assert multiply(numbers_1, numbers_2) == expected_result
```

#### Parametrizing tests - [DOCS](https://docs.pytest.org/en/6.2.x/parametrize.html)

- The `@pytest.mark.parametrize("<args>", [<parameters>])` is used to parametrize tests to run for multiple parameters.
- It is possbile to use multiple paramnetrize decorators to have not dependent parameters - in this case it runs all possible combinations from all parameters.
- It is possible to further controle the arguments passed to the parametrize decorator using `pytest.param()` - it is possible to set one especific param to be skipped - `@pytest.mark.parametrize("numbers", [1, 2, pytest.param(3, marks=pytest.mark.skip), 4, 5])` - here it is also possible to pass a list of marks.
- It is also possible to give logical names to the parameters as an alias - `pytest.param(-1, id="negative")`. 

```
@pytest.mark.parametrize("numbers_1,numbers_2,expected_result", [(1, 2, 2), (2, 4, 8)])
def test_multiply_returns_multiplied_number(numbers_1, numbers_2, expected_result):
    assert multiply(numbers_1, numbers_2) == expected_result


@pytest.mark.parametrize("base", [1, 2])
@pytest.mark.parametrize("exponent", [4, 5])
def test_pow_returns_exponentiated_number(base, exponent):
    assert pow_(base, exponent) == math.pow(base, exponent)

@pytest.mark.parametrize(
    "numbers",
    [1, 2, pytest.param(3, marks=pytest.mark.skip), 4, 5],
)
def test_square_returns_multiplied_number(numbers):
    assert square(numbers) == numbers**2

@pytest.mark.parametrize(
    "numbers",
    [
        pytest.param(-1, id="negative"),
        pytest.param(0, id="zero"),
    ],
)
def test_square_returns_multiplied_number(numbers):
    assert square(numbers) == numbers**2
```

#### Conftest

- In the `conftest.py` file you can setup your fixtures and pytest will automatically import it in the test files.

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
- `pytest <test file name>.py -k <keyword>` - looks for test functions with the `keyword` in the name.
- `pytest <test file name>.py::<test function to be tested>` - runs a specific test fuction inside a specific test file.
- `pytest <test file name>.py::<test class to be tested>` - runs a specific test class inside a specific test file.
- `pytest <test file name>.py::<test class to be tested>::<test function to be tested>` - runs a specific test function in a specific test class inside a specific test file.
- `pytest -s <test file name>.py::<test function to be tested>` - to show the outputs (prints) of the test.
- `pytest -v <test file name>.py::<test function to be tested>` - to have the test verbose.
- Display all tests - `pytest --collectonly`.
- `pytest <test file name>.py> -rs` - Show extra test summary info.
- `pytest --fixtures <test file>.py` - display available fixtures.





