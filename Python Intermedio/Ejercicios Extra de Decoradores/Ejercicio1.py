from functools import wraps


def repeat_twice(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@repeat_twice
def say_hello(name):
    print(f"Hola, {name}")


say_hello("Jeanca")