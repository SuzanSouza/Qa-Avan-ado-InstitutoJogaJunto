#Programa para calculo as média e notas 
nome = input('Digite seu nome: ')

#Coletando as 4 notas
nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))
nota4 = float(input('Digite a 4ª nota: '))

#Calculo das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

#Exibir o resultado
print(f'Olá, {nome}! Sua Média é: {media:.1f} pontos.')
