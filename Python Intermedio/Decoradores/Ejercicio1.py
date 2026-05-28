from functools import wraps

def print_params_and_return(func):
    @wraps(func)
    def wrapper(*args, **kwargs):  
        print(f"Parámetros posicionales: {args}")
        print(f"Parámetros nombrados: {kwargs}")

        result = func(*args, **kwargs)

        print(f"Retorno: {result}")
        return result

    return wrapper


@print_params_and_return
def create_username(first_name, last_name):
    username = f"{first_name.lower()}.{last_name.lower()}"
    return username


user = create_username("firu", "firulais")

print(f"Username creado: {user}")