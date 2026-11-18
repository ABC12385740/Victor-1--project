"""Class 04 - Python basics practice.

Covers the checklist from `FOR-STUDENTS-WITHOUT-PROJECTS.md`:
    1. Install Python
    2. Write Hello World in Python
    3. Write Hello World in a Python function
    4. Print Hello World five times using a loop
    5. Make a list of 5 numbers
    6. Print the list of 5 numbers
    7. Sort the list of 5 numbers and print it

Run with:  python VICTOR_CLASS_04_PYTHON_BASICS.py

Author: Victor (202384014045)
"""

import sys


# --- Task 2: plain Hello World -------------------------------------------

def hello() -> str:
    """Return the classic greeting."""
    return "Hello World"


# --- Task 3: the same greeting, but inside a function ---------------------

def hello_in_function(name: str = "World") -> str:
    """Return the greeting built by a function that takes a name."""
    return f"Hello {name}"


# --- Task 4: five times, using a loop -------------------------------------

def five_times() -> list[str]:
    """Build the greeting five times with a loop and return the lines."""
    lines = []
    for i in range(5):
        lines.append(f"{i + 1}. {hello()}")
    return lines


# --- Task 5: a list of five numbers ---------------------------------------

def make_numbers() -> list[int]:
    """Return the list of five numbers used for tasks 5, 6 and 7."""
    return [42, 7, 19, 3, 88]


# --- Task 6: print the list -----------------------------------------------

def print_numbers(numbers: list[int]) -> None:
    """Print one number per line, so the list contents are easy to read."""
    for number in numbers:
        print(f"   {number}")


# --- Task 7: sort the list and print it -----------------------------------

def sort_numbers(numbers: list[int]) -> None:
    """Print the sorted list twice: a new list, then in-place sorting."""
    print(f"   original: {numbers}")
    print(f"   sorted(): {sorted(numbers)}")
    numbers.sort()
    print(f"   .sort():  {numbers}")


def main() -> None:
    # 1. Python version - proof that the interpreter is installed and reachable
    print("1. Install Python")
    print(f"   version:     {sys.version.split()[0]}")
    print(f"   interpreter: {sys.executable}")

    # 2. Hello World
    print("\n2. Hello World")
    print(f"   {hello()}")

    # 3. Hello World in a function
    print("\n3. Hello World in a function")
    print(f"   {hello_in_function()}")

    # 4. Hello World five times using a loop
    print("\n4. Hello World five times (loop)")
    for line in five_times():
        print(f"   {line}")

    # 5. Make a list of five numbers
    numbers = make_numbers()
    print("\n5. Make a list of 5 numbers")
    print(f"   {numbers}")

    # 6. Print the list
    print("\n6. Print the list of 5 numbers")
    print_numbers(numbers)

    # 7. Sort the list and print it
    print("\n7. Sort the list of 5 numbers and print it")
    sort_numbers(numbers)


if __name__ == "__main__":
    main()
