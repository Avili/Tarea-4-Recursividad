def eliminar_medio(pila):
    if not pila:
        return pila
    medio = len(pila) // 2
    return pila[:medio] + pila[medio+1:]

# Lista
pila = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(eliminar_medio(pila))