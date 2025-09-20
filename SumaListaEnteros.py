def suma_recursiva(lista):
    if not lista: #Caso base (lista vacía)
        return 0
    return lista[0] + suma_recursiva(lista[1:])

# Lista de enteros a sumar
numeros = [6, 9, 10, 45,54]
print(suma_recursiva(numeros))