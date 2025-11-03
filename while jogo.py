# Joguinho do número 5 com limite de tentativas

tentativas = 0          # Contador de tentativas
max_tentativas = 3      # Limite de tentativas
numero_correto = 5      # Número que o usuário precisa acertar

while tentativas < max_tentativas:
    x = int(input("Digite um número: "))
    
    if x == numero_correto:
        print(" Parabéns! Você acertou o número 5! ")
        break  # Sai do loop se acertar
    else:
        tentativas += 1
        print(f" Errado! Tentativa {tentativas} de {max_tentativas}.")

if tentativas == max_tentativas and x != numero_correto:
    print(" Suas tentativas acabaram. O número correto era 5.")