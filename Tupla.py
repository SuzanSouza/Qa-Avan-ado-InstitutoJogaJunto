# Conversão de tupla para lista e manipulação de dados

tupla = ("maçã", "banana", "laranja", "uva", "manga")

lista = list(tupla)

lista.append("abacaxi")
lista.append("melancia")

lista.pop(0)
def new_func(lista):
        lista.pop()

print("Primeiro dado:", lista[0])

print("Quantidade de dados:", len(lista))

pessoa = {
    "Nome": "Suzan","Idade": 33,"Profissão": "QA"}

print("Nome:", pessoa ["Nome"])
