"""

1. check_if_lists_have_an_equal
def check_if_lists_have_an_equal(list_a, list_b):
    for element_a in list_a:
        for element_b in list_b:
            if element_a == element_b:
                return True
                
    return False
Este algoritmo recibe dos listas y revisa si existe al menos un elemento igual entre ambas.
La función tiene dos ciclos anidados. El primer ciclo recorre list_a y por cada elemento de list_a, el segundo ciclo recorre todos los elementos de list_b.
Si ambas listas tienen n elementos, en el peor caso se realizan n * n comparaciones. Esto sucede cuando no hay ningún elemento igual o cuando el elemento igual se encuentra hasta el final.
Por lo tanto, la complejidad de tiempo es:
CT = O(n²)
En cuanto a la complejidad de espacio, la función no crea listas nuevas ni estructuras adicionales que crezcan dependiendo del tamaño del input. Solamente utiliza variables temporales como element_a y element_b, y retorna True o False.
Por lo tanto, la complejidad de espacio es:
CE = O(1)
Conclusión:
CT = O(n²)
CE = O(1)

2. generate_list_trios
def generate_list_trios(list_a, list_b, list_c):
    result_list = []
    for element_a in list_a:
        for element_b in list_b:
            for element_c in list_c:
                result_list.append(f'{element_a} {element_b} {element_c}')
                
    return result_list
Este algoritmo recibe tres listas y genera todas las combinaciones posibles entre los elementos de list_a, list_b y list_c.
La función tiene tres ciclos anidados. El primer ciclo recorre list_a, el segundo ciclo recorre list_b y el tercer ciclo recorre list_c.
Si las tres listas tienen n elementos cada una, el algoritmo genera:
n * n * n
combinaciones.
Por lo tanto, la complejidad de tiempo es:
CT = O(n³)
En cuanto a la complejidad de espacio, este algoritmo sí crea una nueva lista llamada result_list. Est lista almacena todas las combinaciones posibles generadas por los tres ciclos.
Si cada lista tiene n elementos, entonces result_list almacenará n * n * n elementos. Por eso, la memoria utilizada también crece dependiendo del tamaño combinado de las tres listas.
Por lo tanto, la complejidad de espacio es:
CE = O(n³)
entonce:
CT = O(n³)
CE = O(n³)


"""