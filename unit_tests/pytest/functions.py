def square(x: int | float) -> int | float:
    return x * x


def cube(x: int | float) -> int | float:
    return square(x) * x


def multiply(x: int | float, y: int | float) -> int | float:
    return x * y


def pow_(x: int | float, y: int | float) -> int | float:
    return x**y
