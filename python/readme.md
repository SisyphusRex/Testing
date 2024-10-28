Testing in Python requires the use of Pytest.

To install Pytest:
1. **Create Virtual Environment** if not already
    1. Move to program root directory
    2. Type: python -m venv .venv
2. Activate Virtual Environment
    1. Type . .venv/scripts/Activate
3. Install Pytest
    1. Type: python -m pip install pytest
4. Save requirements
    1. Type: python -m pip freeze > requirements.txt
5. When done using program, deactivate virtual environment
    1. Type: deactivate
6. **Install venv from requirements** if needed later on
    1. Type: python -m pip install -r requirements.txt

Your tests should be in a subdirectory called tests.
1. From main directory
    1. Type: mkdir tests
    2. Type: cd tests
    3. Add __init__ file to allow directory locating
        1. type: code __init__.py
    4. add test files
        1. Unit tests
        2. Integration tests
        3. End to End tests

Test file suggestions:
1. Import TestCase to use as abstract class and get its methods
    1. from unittest import TestCase
    2. class YourTests(TestCase):
        ...

Spoof User Input using Monkeypatch:
1. import Pytest, import builtins
2. create response list, first to last
    1. simulated_responses = [...]
3. Create iterator from responses
    iterated_reponses = iter(simulated_responses)
4. Replace input() method with lambda function and iterator
    pytest.MonkeyPatch().setattr(builtins, "input", lambda message: next(iterated_responses))
5. Run the program under Try and assert method, call the attribute of main() you want to compare
    try:
        self.assertEqual(main().my_collection.collection[0].total_cost, 17.75)
    except StopIteration:
    pass


