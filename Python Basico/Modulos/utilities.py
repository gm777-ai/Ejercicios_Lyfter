def remove_upper_cases_from_string(input_string):
    new_string = ""
    for char in input_string:
        if not char.isupper():
            new_string += char
    return new_string