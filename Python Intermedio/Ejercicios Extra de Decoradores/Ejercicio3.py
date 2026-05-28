from functools import wraps
from datetime import datetime


def validate_numbers(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for value in args:
            if not isinstance(value, (int, float)):
                raise TypeError(f"El argumento {value} no es numérico")

        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f"El argumento '{key}' con valor {value} no es numérico")

        return func(*args, **kwargs)

    return wrapper


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        args_text = ", ".join(str(value) for value in args)

        if kwargs:
            kwargs_text = ", ".join(f"{key}={value}" for key, value in kwargs.items())
            if args_text:
                args_text = args_text + ", " + kwargs_text
            else:
                args_text = kwargs_text

        print(f"func:{func.__name__} - args: {args_text} - [{datetime.now()}] - Resultado: {result}")

        return result

    return wrapper


@log_call
@validate_numbers
def multiply(a, b):
    return a * b


result = multiply(3, 4)

print(f"Resultado {result}")