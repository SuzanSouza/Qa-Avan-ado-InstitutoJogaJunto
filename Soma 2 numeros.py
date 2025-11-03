# Função que soma dois números e retorna o resultado
def somar(a, b):
    return a + b

# Solicita os números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Chama a função e guarda o resultado
resultado = somar(num1, num2)

# Exibe o resultado final
print(f"A soma de {num1} + {num2} é = {resultado}")
