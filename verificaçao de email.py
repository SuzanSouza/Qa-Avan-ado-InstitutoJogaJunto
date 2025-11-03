# Email do usuário
email = input("Digite seu email do Joga Junto: ")

# Verifica se o email contém o domínio correto
if "@jogajuntoinstituto.org" in email:
    print("✅ Email válido!")
else:
    print(" Email inválido! Deve conter @jogajuntoinstituto.org")
