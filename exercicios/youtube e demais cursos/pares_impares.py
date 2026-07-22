def separar_pares_e_impares(lista_numeros):
    lista_pares = []
    lista_impares = []

    for numero in lista_numeros:
        if numero % 2 == 0:
            lista_pares.append(numero)
        else:
            lista_impares.append(numero)

    return lista_pares, lista_impares

lista_numeros = [1, 3, 4, 5, 6, 2, 7, 9, 8, 12, 15, 10, 25, 33, 19]
lista_pares, lista_impares = separar_pares_e_impares(lista_numeros)

print(f'lista de pares: {lista_pares}')
print(f'lista de impares: {lista_impares}')