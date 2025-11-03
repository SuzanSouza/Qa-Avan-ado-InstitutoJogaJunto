import pandas as pd

# Cria o DataFrame
df = pd.DataFrame({
    "Nome": ["Ana", "Carlos", "Mariana", "João", "Paula", "Rafaela", "Pedro"],
    "Idade": [25, 30, 22, 27, 35, 29, 31],
    "Cidade": ["Recife", "Recife", "Recife", "Salvador", "Salvador", "São Paulo", "Manaus"]
})

# Filtra apenas moradores de Recife
recife = df[df["Cidade"] == "Recife"]

# Mostra o resultado
print(recife)


