Utility functions and decorators for the workout optimizer application.

import functools

def validate_numeric_input(func):
    Decorator to ensure that CLI inputs requiring numbers are safely parsed.
    
    If an invalid entry (like a string) is provided, it catches the ValueError 
    and prompts the user gracefully instead of crashing.
 
    functools.wraps(func)
    def wrapper(*args, *kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except ValueError:
                print(" Invalid input! Please enter a valid number.")
    return wrapper

validate_numeric_input
def get_positive_integer(prompt_text: str) -> int:
    Prompts user for an integer and ensures it's greater than zero.
    value = int(input(prompt_text))
    if value <= 0:
        raise ValueError
    return value

validate_numeric_input
def get_positive_float(prompt_text: str) -> float:
    Prompts user for a float and ensures it's greater than zero.
    value = float(input(prompt_text)
    if value <= 0:
        raise ValueError
    return value
