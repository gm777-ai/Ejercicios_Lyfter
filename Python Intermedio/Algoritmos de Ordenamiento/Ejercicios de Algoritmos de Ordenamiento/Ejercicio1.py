def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                temporary = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temporary

    return numbers


digits = [8, 3, 5, 1, 9, 0, 4, 7, 2, 6, -22, -100, 400, 40, 3, 8, 1, 5, 0]

print("Lista original:")
print(digits)

sorted_digits = bubble_sort(digits)

print("Lista ordenada:")
print(sorted_digits)