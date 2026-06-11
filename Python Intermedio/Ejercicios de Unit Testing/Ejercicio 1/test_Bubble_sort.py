import pytest
from Bubble_sort import bubble_sort


def test_bubble_sort_small_list():
    result = bubble_sort([10, 3, 5, 1, 8])
    expected_result = [1, 3, 5, 8, 10]

    assert result == expected_result


def test_bubble_sort_large_list():
    large_list = list(range(120, 0, -1))
    result = bubble_sort(large_list)
    expected_result = list(range(1, 121))

    assert result == expected_result


def test_bubble_sort_empty_list():
    result = bubble_sort([])
    expected_result = []

    assert result == expected_result


def test_bubble_sort_invalid_parameter():
    try:
        bubble_sort("Hola")
        assert False
    except TypeError:
        assert True