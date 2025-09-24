dicionario = {
    "nome": "lucas",
    "idade": 20,
    "time": "Sport",
    "altura": 1.80,
    "peso": 70
}

print(dicionario)

print(dicionario.keys())
print(dicionario.values())
print(len(dicionario))
dicionario.pop("peso")
print(dicionario)

print('-'*100)

lista_chaves = list(('Nome', 'Idade', 'Time', 'Altura', 'Peso'))
lista_valores = list(('João', 21, 'Vasco', 1.70, 65))

dicionario2 = dict(zip(lista_chaves, lista_valores))

print(f'Lista de chaves: {lista_chaves}, lista valores: {lista_valores}')
print(dicionario2)

lista = list(zip(lista_chaves, lista_valores))

print(f'Lista: {lista}')
print(lista[2][1])

for chave, valor in lista:
    print(f'Chave: {chave}, Valor: {valor}')
    
for chave, valor in dicionario2.items():
    print(f'Chave: {chave}, Valor: {valor}')