"""Math exercises."""
import math
from math import sqrt, pi


def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    sum = num_a + num_b
    difference = num_a - num_b
    return sum, difference


def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    divisiom = num_a / num_b
    return divisiom



def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    # Töisarvuline jagamine
    if num_b == 0:
        raise ValueError("Division by zero is not allowed.")
    return num_a // num_b


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    if num_b == 0:
        raise ValueError("Division by zero is not allowed.")
    multiply_numbers = num_a * num_b #Korrutamine
    power = num_a ** num_b           #Astendamine
    remainder = num_a % num_b        #Ülejääk (modulo)
    return multiply_numbers, power, remainder


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    average = (num_a + num_b) / 2
    return average


def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    import math
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    circle_area = pi * (radius ** 2)
    return round(circle_area,2)


def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle."""
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    triangle_area = (sqrt(3) / 4) * (side_length ** 2)
    return round(triangle_area,)


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    discriminant = b ** 2 - 4 * a * c
    return discriminant


def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    hypotenuse: float = sqrt(a ** 2 + b ** 2)
    return hypotenuse


def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
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
