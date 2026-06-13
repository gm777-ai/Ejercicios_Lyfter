def sum_all_numbers(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


def reverse_string(text):
    reversed_text = ""

    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]

    return reversed_text


def print_upper_and_lower_count(text):
    upper_count = 0
    lower_count = 0

    for character in text:
        if character.isupper():
            upper_count += 1
        elif character.islower():
            lower_count += 1

    print(f"There's {upper_count} upper cases and {lower_count} lower cases")


def sort_words_by_hyphen(text):
    words = text.split("-")
    words.sort()

    sorted_text = "-".join(words)

    return sorted_text


def is_prime(number):
    if number <= 1:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


def get_prime_numbers(numbers):
    prime_numbers = []

    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)

    return prime_numbers