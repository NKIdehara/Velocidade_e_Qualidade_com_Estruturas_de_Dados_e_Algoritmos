def contar_repeticoes(palavra, caracter):
    if len(palavra) == 0:
        return 0
    n = len(palavra)-1
    if palavra[n] == caracter:
        return 1 + contar_repeticoes(palavra[:n], caracter)
    return contar_repeticoes(palavra[:n], caracter)

print(contar_repeticoes("banana", "a"))
print(contar_repeticoes("bernardo", "r"))