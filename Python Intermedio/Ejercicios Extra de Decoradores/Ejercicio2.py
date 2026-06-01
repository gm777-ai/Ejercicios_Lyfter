from functools import wraps

# Trigger para disparar la excepcion si lo pasamos a False 
user_logged_in = True


def requires_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if user_logged_in is not True:
            raise Exception("Usuario no autenticado")

        return func(*args, **kwargs)

    return wrapper


@requires_login
def view_private_messages(username):
    print(f"Mostrando mensajes privados de {username}")


view_private_messages("Firulais")