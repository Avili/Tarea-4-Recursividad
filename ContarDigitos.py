def contar_digitos(n):
    if n < 10:  # número de un solo un dígito
        return 1
    return 1 + contar_digitos(n // 10)

# numero con mas digitos
numero = 123456789012346
print(contar_digitos(numero))