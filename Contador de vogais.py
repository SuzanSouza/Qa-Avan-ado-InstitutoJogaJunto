# contar as vogais em uma palavra
def contar_vogais(palavra):
    vogais = "aeiouAEIOU"  # Inclui maiúsculas e minúsculas
    contador = 0

    # Percorre cada letra da palavra
    for letra in palavra:
        if letra in vogais:
            contador += 1

    return contador

# Solicita a palavra do usuário
palavra = input("Digite uma palavra: ")

# Chama a função e armazena o resultado
total_vogais = contar_vogais(palavra)

# Exibe o resultado
print(f"A palavra '{palavra}' tem {total_vogais} vogais.")