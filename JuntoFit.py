# Solicita a frequência atual do aluno
frequencia = int(input("Digite o número de dias consecutivos que o aluno frequentou a academia: "))

# Verifica as condições de acordo com a frequência
if frequencia == 21:
    print("UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ!")
elif frequencia < 21 and frequencia > 0:
    print("VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO")
else:
    print("QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.")