# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Verifica se a idade é maior ou igual a 18
if idade >= 18:
    print("Indivíduo possui idade mínima para dirigir")

elif idade == 17:
    print("Indivíduo tem 17 anos e ainda NÃO está apto para dirigir")

else:
    print("Indivíduo NÃO possui idade mínima para dirigir")
