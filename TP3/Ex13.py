def palindromo(palavra):
    meio = len(palavra) // 2
    comp = len(palavra)
    for i in range(meio):
        if palavra[i].lower() != palavra[comp-i-1].lower():
            return False
    return True

palavra = "ovo"
print(f"{palavra} é palíndromo: {palindromo(palavra)}")
palavra = "Osso"
print(f"{palavra} é palíndromo: {palindromo(palavra)}")
palavra = "motor"
print(f"{palavra} é palíndromo: {palindromo(palavra)}")
palavra = "radar"
print(f"{palavra} é palíndromo: {palindromo(palavra)}")