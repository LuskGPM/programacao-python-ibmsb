lista = list()

lista.append('Lucas')
lista.append('Paulo')
lista.append('Thiago')

for i in lista:
    print(i)
    
if "Lucas" in lista:
    print('Lucas está na lista')
    
else:
    print('Lucas não está na lista')
    
print(f'Tamanho da lista: {len(lista)}')

listadois = lista.copy()

lista.remove('Lucas')

print(f'Lista um: {lista}')
print(f'Lista dois: {listadois}')
