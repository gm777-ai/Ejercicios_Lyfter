from functions_exercises import (
    sum_all_numbers,
    reverse_string,
    print_upper_and_lower_count,
    sort_words_by_hyphen,
    get_prime_numbers
)


# 3. Tests para sum_all_numbers


def test_sum_all_numbers_with_positive_numbers():
    result = sum_all_numbers([4, 6, 2, 29])
    expected_result = 41

    assert result == expected_result


def test_sum_all_numbers_with_negative_numbers():
    result = sum_all_numbers([-5, 10, -2])
    expected_result = 3

    assert result == expected_result


def test_sum_all_numbers_with_empty_list():
    result = sum_all_numbers([])
    expected_result = 0

    assert result == expected_result


# 4. Tests para reverse_string

def test_reverse_string_with_sentence():
    result = reverse_string("Hola mundo")
    expected_result = "odnum aloH"

    assert result == expected_result


def test_reverse_string_with_single_word():
    result = reverse_string("Python")
    expected_result = "nohtyP"

    assert result == expected_result


def test_reverse_string_with_empty_string():
    result = reverse_string("")
    expected_result = ""

    assert result == expected_result


# 5. Tests para print_upper_and_lower_count

def test_print_upper_and_lower_count_with_mixed_text(capsys):
    print_upper_and_lower_count("I love Nación Sushi")

    captured = capsys.readouterr()

    assert captured.out.strip() == "There's 3 upper cases and 13 lower cases"


def test_print_upper_and_lower_count_with_only_uppercase(capsys):
    print_upper_and_lower_count("HELLO")

    captured = capsys.readouterr()

    assert captured.out.strip() == "There's 5 upper cases and 0 lower cases"


def test_print_upper_and_lower_count_with_only_lowercase(capsys):
    print_upper_and_lower_count("hello")

    captured = capsys.readouterr()

    assert captured.out.strip() == "There's 0 upper cases and 5 lower cases"


# 6. Tests para sort_words_by_hyphen

def test_sort_words_by_hyphen_with_example_text():
    result = sort_words_by_hyphen("python-variable-funcion-computadora-monitor")
    expected_result = "computadora-funcion-monitor-python-variable"

    assert result == expected_result


def test_sort_words_by_hyphen_with_short_words():
    result = sort_words_by_hyphen("z-a-c-b")
    expected_result = "a-b-c-z"

    assert result == expected_result


def test_sort_words_by_hyphen_with_animals():
    result = sort_words_by_hyphen("perro-gato-ave")
    expected_result = "ave-gato-perro"

    assert result == expected_result



# 7. Tests para get_prime_numbers


def test_get_prime_numbers_with_mixed_numbers():
    result = get_prime_numbers([1, 4, 6, 7, 13, 9, 67])
    expected_result = [7, 13, 67]

    assert result == expected_result


def test_get_prime_numbers_with_several_primes():
    result = get_prime_numbers([2, 3, 5, 8, 10])
    expected_result = [2, 3, 5]

    assert result == expected_result


def test_get_prime_numbers_with_no_primes():
    result = get_prime_numbers([1, 4, 6, 8, 9, 10])
    expected_result = []

    assert result == expected_result