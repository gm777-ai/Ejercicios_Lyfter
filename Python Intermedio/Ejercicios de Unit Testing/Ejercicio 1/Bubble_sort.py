def bubble_sort(numbers):
    if not isinstance(numbers, list):
        raise TypeError("El parámetro debe ser una lista")

    sorted_list = numbers.copy()
    # sorted_list = "hola" Puse esto aqui solo para probar nada mas


    for i in range(len(sorted_list)):
        for j in range(0, len(sorted_list) - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]

    return sorted_list