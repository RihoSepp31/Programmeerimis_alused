"""Function examples."""


# func()
"""Print to console - I'm inside the function."""
def func():
    print("I m inside the function\n")


# my_name_is(name)
"""Print to console - My name is {name}.
:param name: name you want to use
"""
def my_name_is(name:str) -> None:
    print(f"My name is {name}")



# sum_six(num)`
"""Return num + 6.
:param num: number you want to add 6 to"""
def sum_six(num:int) -> int:
    return num + 6


# sum_numbers()
"""Return a + b.
:param a: first number
:param b: second number"""
def sum_numbers(a:int, b:int) -> int:
    return a + b


# usd_to_eur()
"""Return usd * 0.81.
:param usd: amount in USD
:return: amount in EUR"""
def usd_to_eur(usd:float) -> float:
    return usd * 0.81

