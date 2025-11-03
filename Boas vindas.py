# Lista de nomes permitidos
nomes_autorizados = ["Suzan", "Cleuber", "Eliane", "Thiago", "Juliana"]

# Solicita o nome do usuário
nome = input("Digite seu nome: ")

# Verifica se o nome está na lista e exibe a mensagem
if nome in nomes_autorizados:
    print(f"Bem-vindo(a), {nome}!")
else:
    print("Desculpe, você não está na lista de acesso.")
