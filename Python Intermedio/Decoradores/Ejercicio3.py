from datetime import date
from functools import wraps


class User:
    def __init__(self, full_name, date_of_birth):
        self.full_name = full_name
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()

        user_age = today.year - self.date_of_birth.year

        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            user_age -= 1

        return user_age


def adult_required(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.age < 18:
            raise PermissionError(
                f"{user.full_name} no puede realizar esta acción porque tiene {user.age} años."
            )

        return func(user, *args, **kwargs)

    return wrapper


@adult_required
def rent_car(user, car_model):
    return f"{user.full_name} ha rentado un {car_model} correctamente."


adult_user = User("Maria Lopez", date(1998, 3, 20))
minor_user = User("Pedro Gomez", date(2008, 7, 5))


print(rent_car(adult_user, "Toyota Corolla"))
print(rent_car(minor_user, "Honda Civic"))

# Se que hay cosas quer todavian se pueden mejorar en este codigo como ser: el rango de edad razonable/valida de un ser vivo
# Edad minima, etc. pero solo me apegue a lo que el ejercicio requeria esta vez