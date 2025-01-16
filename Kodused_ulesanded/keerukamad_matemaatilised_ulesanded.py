"""
Math exercises module.

This module contains functions for converting time, calculating sine and cosine,
repeating greetings, and adding numbers. It also includes test cases to verify functionality.
"""

import math


def time_converter(seconds: int) -> str:
    """Convert seconds into hours and minutes."""
    if seconds < 0:
        raise ValueError("Seconds cannot be negative.")
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{seconds} sekundit on {hours} tund(i) ja {minutes} minut(it)."


def student_helper(angle: int) -> str:
    """Calculate sine and cosine of a given angle."""
    sine = round(math.sin(math.radians(angle)), 1)
    cosine = round(math.cos(math.radians(angle)), 1)
    return f"Nurk: {angle}, siinus: {sine}, koosinus: {cosine}."


def greetings(n: int) -> str:
    """Return 'Hey' repeated n times."""
    if n < 0:
        raise ValueError("The number must be 0 or greater.")
    return "Hey" * n


def adding_numbers(num_a: int, num_b: int) -> str:
    """Return given numbers added together as a string."""
    sum_numbers = num_a + num_b
    return str(sum_numbers)


if __name__ == '__main__':
    # Kontrollime funktsioonide väljundeid
    print(time_converter(3661))  # "3661 sekundit on 1 tund(i) ja 1 minut(it)."
    print(student_helper(30))   # "Nurk: 30, siinus: 0.5, koosinus: 0.9."
    print(greetings(3))         # "HeyHeyHey"
    print(greetings(0))         # ""

    # Testime adding_numbers funktsiooni
    print(adding_numbers(3, 9))  # Eeldatavasti "12"
    print(adding_numbers(0, 0))  # Eeldatavasti "0"
    print(adding_numbers(-5, 5))  # Eeldatavasti "0"

    # Automaattestid
    assert time_converter(3661) == "3661 sekundit on 1 tund(i) ja 1 minut(it)."
    assert student_helper(30) == "Nurk: 30, siinus: 0.5, koosinus: 0.9."
    assert greetings(3) == "HeyHeyHey"
    assert greetings(0) == ""
    assert adding_numbers(3, 9) == "12"  # Oodatud tulemus
    assert adding_numbers(0, 0) == "0"
    assert adding_numbers(-5, 5) == "0"

    print("Kõik testid edukad!")
