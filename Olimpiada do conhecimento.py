# Função que verifica se a matrícula é par ou ímpar
def verificar_grupo(matricula):
    if matricula % 2 == 0:  # Se o resto da divisão por 2 for zero → número par
        return "VOCÊ ESTÁ NO TIME AZUL"
    else:  # Caso contrário → número ímpar
        return "VOCÊ ESTÁ NO TIME AMARELO"

# Solicita o número da matrícula do aluno
numero_matricula = int(input("Digite o número da sua matrícula: "))

# Chama a função e mostra o resultado
mensagem = verificar_grupo(numero_matricula)
print(mensagem)
