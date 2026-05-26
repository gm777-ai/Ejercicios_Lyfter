from functools import wraps

def only_numbers(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        for value in args:
            if not isinstance(value, (int, float)):
                raise TypeError(f"Error: '{value}' no es un número.")

        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f"Error: el parámetro '{key}' debe ser un número.")

        return func(*args, **kwargs)

    return wrapper


@only_numbers
def calculate_average_speed(distance, time):
    return distance / time

speed = calculate_average_speed(120, 2)

print(f"Velocidad promedio: {speed} km/h")

#speed = calculate_average_speed(120, "2 horas")

#print(speed)

speed = calculate_average_speed(distance=300, time=5)

print(f"Velocidad promedio: {speed} km/h")

speed = calculate_average_speed(distance=300, time="cinco")