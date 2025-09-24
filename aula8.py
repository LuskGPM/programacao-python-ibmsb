dicionario = {
    'Nome': 'Lucas',
    'Idade': 20,
    'Time': 'Sport',
    'Altura': 1.80
}

for i in dicionario:
    print(f'{i}: {dicionario[i]}')
    
print('-'*100)

for k, i in dicionario.items():
    print(f'{k}: {i}')

print('-'*100)

for i in dicionario.values():
    print(i)
    
print('-'*100)

for i in dicionario.keys():
    print(i)