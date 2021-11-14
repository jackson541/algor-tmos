import time

def buscador_sequencial(lista, valor):
    """
    Verifica sequencialmente se algum dos elementos da lista eh o valor desejado    
    """
    for index in range(len(lista)):
        if lista[index] == valor:
            return True
    return False



if __name__ == '__main__':
    lista = [numero for numero in range(99999999)]
    agora = time.time()
    
    assert buscador_sequencial(lista, 99999990) == True
    assert buscador_sequencial(lista, 999999999) == False
    
    print(f"demorou {time.time() - agora} segundos")


