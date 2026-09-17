
def insertion_sort(lista):
    lista=[12, 11, 13, 5, 6, 1, 2, 50, 4, 7, 8, 9, 10, 3, 14, 15, 16, 17, 18, 19, 20, 100, 99, 98, 56, 97, 96, 67, 95, 94, 77, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80] 
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista 
lista_ordenada = insertion_sort([])    
print(lista_ordenada)