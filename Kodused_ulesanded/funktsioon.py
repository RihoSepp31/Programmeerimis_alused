"""Function examples."""


def func():
    """Return a string - I'm inside the function."""
    return "I'm inside the function\n"


def my_name_is(name: str) -> None:
    """Print to console - My name is {name}.

    :param name: Name you want to use.
    """
    print(f"My name is {name}")


def sum_six(num: int) -> int:
    """Return num + 6.

    :param num: Number you want to add 6 to.
    :return: Result of num + 6.
    """
    return num + 6


def sum_numbers(a: int, b: int) -> int:
    """Return a + b.

    :param a: First number.
    :param b: Second number.
    :return: Sum of a and b.
    """
    return a + b


def usd_to_eur(usd: float) -> float:
    """Return usd * 0.81.

    :param usd: Amount in USD.
    :return: Amount in EUR.
    """
    return round(usd * 0.81, 2)


if __name__ == "__main__":
    print(func())  # "I'm inside the function\n"
    my_name_is("Riho")
    print(sum_six(1))  # 7
    print(sum_numbers(5, 5))  # 10
    print(usd_to_eur(100))  # 81.0
