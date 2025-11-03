#Case Pet Shop
nome = input('Digite o nome do seu pet: ')
idade_pet = int(input('Qual a idade do seu Pet? '))
banho = int(input('Quantos banhos o seu pet já tomou esse ano?'))
print('Porte Grande digite 1\nPorte Médio digite 2\nPorte Pequeno digite 3')
porte = int(input('Qual o porte do seu pet? '))
calculo = idade_pet * 7
print(calculo)
 
 #valor do banho de acordo com o porte
cachorro_grande = 75
cachorro_medio = 60
cachorro_pequeno = 50

#Cálculo do lucro anual de acordo com o porte
if porte == 1:
    custo = 20
    valor_banho = cachorro_grande - custo
    lucro = valor_banho * banho
if porte == 2:
    custo = 15
    valor_banho = cachorro_medio - custo
    lucro = valor_banho * banho
if porte == 3:
    custo = 5
    valor_banho = cachorro_pequeno - custo
    lucro = valor_banho * banho

print(f'Olá, {nome} tem {calculo} anos e nos ultimos 12 meses o lucro com este animal foi de R$ {lucro}')