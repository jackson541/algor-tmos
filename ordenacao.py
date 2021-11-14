import time

def selecao_direta(lista):
    """
    Percorre uma lista verificando para cada índice qual o menor elemento da lista a partir dele
    para poder tomar a posição desse índice.
    
    Ex:
    [1, 5, 9, 0, 8, 10, 6] -> inicio
    [0, 5, 9, 1, 8, 10, 6] -> 0 menor
    [0, 1, 9, 5, 8, 10, 6] -> 1 menor
    [0, 1, 5, 9, 8, 10, 6] -> 5 menor
    [0, 1, 5, 6, 8, 10, 9] -> 6 menor
    [0, 1, 5, 6, 8, 10, 9] -> 8 menor
    [0, 1, 5, 6, 8, 9, 10] -> 9 menor
    """
    tamanho_total = len(lista)
    for posicao_atual_ordenacao in range(tamanho_total - 1): # -1 porque a ultima posição vai estar ordenada no final
        posicao_do_minimo = posicao_atual_ordenacao
        for posicao_atual_lista in range(posicao_atual_ordenacao + 1, tamanho_total):
            # verifica se o valor atual checado é menor que o valor 
            # mínimo da lista a partir da ultima posição de ordenação
            if lista[posicao_atual_lista] < lista[posicao_do_minimo]:
                posicao_do_minimo = posicao_atual_lista
            
            # troca de lugar o valor mínimo da lista com a posição mínima da vez
            lista[posicao_atual_ordenacao], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[posicao_atual_ordenacao]
    return lista


if __name__ == '__main__':
    lista = [numero for numero in range(1, 9998, 2)]
    lista += [numero for numero in range(9999, 2, -2)]
    lista_ordenada = sorted(lista)
    
    agora = time.time()
    assert selecao_direta(lista) == lista_ordenada
    print(f"demorou {time.time() - agora} para ordenar com selecao_direta")

