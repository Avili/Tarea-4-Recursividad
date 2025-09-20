def es_palindromo(cadena):
    if len(cadena) <= 1:  # si es vacia o de un solo caracter ya no hace mas trabajo
        return "Es palindromo"
    if cadena[0] != cadena[-1]: # compara el primer y ultimo caracter y si no coinciden, directamente lo descarta
        return "No es palindromo"
    return es_palindromo(cadena[1:-1]) #si coinciden lso extremos procede a comparar las demas letras

# texto a identificar
texto = "reconocter"
print(es_palindromo(texto))