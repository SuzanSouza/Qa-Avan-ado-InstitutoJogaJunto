from faker import Faker

# Criar o gerador de dados em português do Brasil
fake = Faker('pt_BR')

# Criar a persona
persona = {
    "Nome": fake.name(),
    "Idade": fake.random_int(min=18, max=80),  # Gera idade aleatória entre 18 e 80
    "Cidade": fake.city()
}

# Exibir a persona
print("Persona Gerada:")
for chave, valor in persona.items():
    print(f"{chave}: {valor}")
