# Testing with Pytest

## Objective

The purpose of this assignment is to introduce you to unit testing with pytest and debugging using PyCharm. You will write tests for a buggy Python script, fix the identified issues, and document the process.

## Assignment Tasks

    * Git Repository
        * Inside your repository, create a folder called pytest_assignment/ (or something equally descriptive)
        * Place all files related to this assignment inside this folder.
    * Analyze the Provided Python Script (program.py)
        * This script contains three functions, each with one or more bugs.
        * Your goal is to identify and write tests for these functions.
    * Write Unit Tests (test_program.py)
        * Use pytest to create at least three tests per function.
        * Tests should cover a normal cases, an edge cases, and a corner cases.
    * Run Tests and Capture Proof
        * Run your tests in PyCharm and take a screenshot of all tests passing (showing at least 9 green checks).
        * Save the screenshot as proof.png.
    * Fix Bugs and Document Fixes (fixes.md)
        * After running your tests, fix the identified issues in program.py.
        * Document each fix in fixes.md, explaining:
            * What the bug was.
            * How you identified it.
        * What fix you applied.
    * Submit Your Work
        * Push your code and test files to your GitHub repository.
        * Upload the repository link via the submission portal.

Supplied Code (program.py)

This script contains intentional bugs for you to find and fix.

``` python
def divide_numbers(a, b):
    """Returns the result of a divided by b, rounded to two decimals."""
    result = a / b  # Bug: No handling for division by zero
    return round(result, 2)
 
def reverse_string(s):
    """Returns the reversed string, with each character's case flipped."""
    reversed_s = s[::-1]  # Bug: Might not handle non-string input properly
    flipped_case = ''.join([char.swapcase() for char in reversed_s])
    return flipped_case
 
def get_list_element(lst, index):
    """Returns the element at the given index in the list, or 'Not found' if out of range."""
    if index < len(lst):  # Bug: Incorrect boundary check
        return lst[index]
    else:
        return "Not found"  # Bug: Should probably raise an exception instead
 ```

## Example Test File (test_program.py)

#### This is an example of how you might structure your pytest tests.

``` python
import pytest
from program import divide_numbers, reverse_string, get_list_element
 
def test_divide_numbers():
    assert divide_numbers(10, 3) == 3.33
```

## Deliverables

    program.py (original script with bugs)
    test_program.py (pytest tests covering edge cases)
    proof.png (screenshot of all tests passing)
    fixes.md (list of identified bugs & fixes)
    GitHub repository link (submitted via portal)