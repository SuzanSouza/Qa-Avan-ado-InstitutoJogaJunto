import os  # Importando a biblioteca que interage com o sistema operacional

# Criando uma lista de dados
frutas = ["maçã", "banana", "uva", "morango", "laranja"]

# Verificando o diretório atual
diretorio_atual = os.getcwd()
print(" Diretório atual:", diretorio_atual)

# Criando uma nova pasta chamada "meus_dados"
nova_pasta = os.path.join(diretorio_atual, "meus_dados")  # Cria o caminho da nova pasta
os.makedirs(nova_pasta, exist_ok=True)  # Cria a pasta (sem erro se ela já existir)
print(" Pasta criada em:", nova_pasta)

# Caminho completo do arquivo
arquivo_txt = os.path.join(nova_pasta, "frutas.txt")

# Criando e escrevendo no arquivo
with open(arquivo_txt, "w", encoding="utf-8") as arquivo:
    arquivo.write(" Lista de Frutas:\n")
    for fruta in frutas:
        arquivo.write(f"- {fruta}\n")

print("✅ Arquivo criado e salvo com sucesso em:", arquivo_txt)
