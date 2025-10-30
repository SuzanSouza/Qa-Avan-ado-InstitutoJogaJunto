# Solicita o valor total da compra
valor_compra = float(input("Digite o valor total da sua compra: R$ "))

# Verifica o valor e aplica as condições
if valor_compra > 500:
    print("PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%!")
elif valor_compra >= 250:
    print("PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00!")
else:
    print("POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.")