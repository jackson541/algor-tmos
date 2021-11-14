import time

def buscador_sequencial(lista, valor):
    """
    Verifica sequencialmente se algum dos elementos da lista eh o valor desejado    
    """
    for index in range(len(lista)):
        if lista[index] == valor:
            return index
    return -1



if __name__ == '__main__':
    lista = [numero for numero in range(1, 19999999)]
    agora = time.time()
    
    assert buscador_sequencial(lista, 19999990) == 19999989
    assert buscador_sequencial(lista, 999999999) == -1
    
    print(f"demorou {time.time() - agora} segundos na busca sequencial")


