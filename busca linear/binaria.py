from array import array

def buscar(list, nome_busca):
    tamanho_lista = len(list)
    for atual in range(0, tamanho_lista):
        print(atual)
        print(list[atual])
        print(nome_busca)
        if(str(list[atual]).strip() == nome_busca):
            return atual
        
    
    return -1

def main():
    with open('./busca linear/lista_alunos.txt') as arquivo:
        lista = arquivo.read().split(',')
        posicao = buscar(lista, 'Erica')
        print(f'Aluno: {lista[posicao]} esta na posicao {posicao}°')
        
if __name__ == '__main__':
    main()
    