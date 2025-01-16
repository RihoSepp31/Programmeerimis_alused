"""Math exercises."""
import math
from math import sqrt, pi


def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b.

    This function calculates the sum and difference of two integers
    and returns them as a tuple.
    """
    sum_result = num_a + num_b
    difference = num_a - num_b
    return sum_result, difference


def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result.

    This function performs floating-point division and returns the result.
    """
    division = num_a / num_b
    return division


def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down.

    This function performs integer division and raises an exception
    if division by zero is attempted.
    """
    if num_b == 0:
        raise ValueError("Division by zero is not allowed.")
    return num_a // num_b


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product, power, and remainder of num_a and num_b.

    This function performs three operations:
    1. Multiplication of num_a and num_b.
    2. num_a raised to the power of num_b.
    3. The remainder when num_a is divided by num_b.
    """
    if num_b == 0:
        raise ValueError("Division by zero is not allowed.")
    multiply_numbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return multiply_numbers, power, remainder


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables.

    This function calculates the arithmetic mean of two integers.
    """
    average = (num_a + num_b) / 2
    return average


def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle.

    This function uses the formula πr² to calculate the area of a circle.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    circle_area = pi * (radius ** 2)
    return round(circle_area, 2)


def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle.

    This function uses the formula (sqrt(3)/4) * side_length² to calculate the area.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    triangle_area = (sqrt(3) / 4) * (side_length ** 2)
    return round(triangle_area)


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant for a quadratic equation.

    This function calculates the discriminant using the formula b² - 4ac.
    """
    discriminant = b ** 2 - 4 * a * c
    return discriminant


def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of the hypotenuse given the lengths of the two catheti.

    This function uses the Pythagorean theorem to calculate the hypotenuse.
    """
    hypotenuse: float = sqrt(a ** 2 + b ** 2)
    return hypotenuse


def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of a cathetus given the hypotenuse and the other cathetus.

    This function calculates the length of a cathetus using the Pythagorean theorem.
    """
    if c <= a:
        raise ValueError("Second cathetus cannot be longer than the hypotenuse.")
    b = math.sqrt(c ** 2 - a ** 2)
    return b


if __name__ == '__main__':
    assert sum_and_difference(5, 6) == (11, -1)
    assert sum_and_difference(11, 9) == (20, 2)
    assert float_division(9, 3) == 3.0
    assert round(float_division(10, 3), 2) == 3.33

    assert integer_division(10, 3) == 3
    assert integer_division(7, 11) == 0

    assert powerful_operations(10, 3) == (30, 1000, 1)
    assert powerful_operations(2, 10) == (20, 1024, 2)

    assert find_average(3, 7) == 5.0
    assert find_average(999, 999) == 999.0

    assert area_of_a_circle(1) == 3.14

    assert area_of_an_equilateral_triangle(2) == 2
    assert area_of_an_equilateral_triangle(5) == 11
    assert area_of_an_equilateral_triangle(10) == 43

    assert calculate_discriminant(1, -3, 2) == 1
    assert calculate_discriminant(1, 2, 1) == 0

    assert calculate_hypotenuse_length(3, 4) == 5.0
    assert calculate_hypotenuse_length(5, 12) == 13.0

    assert calculate_cathetus_length(3, 5) == 4.0
    assert calculate_cathetus_length(6, 10) == 8.0

    print("OK")
