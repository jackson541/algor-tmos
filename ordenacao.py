import time
import random

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


def booble_sort(lista):
    """
    O algoritmo de ordenação em bolha se comporta como um tupo de ensaio em que os elementos mais pesados descem para o fundo
    e os mais leves sobem como uma bolha.

    Ex:
    Etapa 1
    [1, 5, 9, 0, 8, 10, 6] -> inicio
    [1, 5, 9, 0, 8, 10, 6] -> 1 menor que 5, mantem
    [1, 5, 9, 0, 8, 10, 6] -> 5 menor que 9, mantem
    [1, 5, 0, 9, 8, 10, 6] -> 9 maior que 0, troca
    [1, 5, 0, 8, 9, 10, 6] -> 9 maior que 8, troca
    [1, 5, 0, 8, 9, 10, 6] -> 9 menor que 10, mantem
    [1, 5, 0, 8, 9, 6, 10] -> 10 maior que 6, troca

    Etapa 2
    [1, 5, 0, 8, 9, 6, 10] -> inicio
    [1, 5, 0, 8, 9, 6, 10] -> 1 menor que 5, mantem
    [1, 0, 5, 8, 9, 6, 10] -> 5 maior que 0, troca
    [1, 0, 5, 8, 9, 6, 10] -> 5 menor que 8, mantem
    [1, 0, 5, 8, 9, 6, 10] -> 8 menor que 9, mantem
    [1, 0, 5, 8, 6, 9, 10] -> 9 maior que 6, troca

    Etapa 3
    [1, 0, 5, 8, 6, 9, 10] -> inicio
    [0, 1, 5, 8, 6, 9, 10] -> 1 maior que 0, troca
    [0, 1, 5, 8, 6, 9, 10] -> 1 menor que 5, mantem
    [0, 1, 5, 8, 6, 9, 10] -> 5 menor que 8, mantem
    [0, 1, 5, 6, 8, 9, 10] -> 8 maior que 6, troca

    Pode ter até N repetições (número de elementos da lista) para ordenar todos par a par
    """
    for posicao_fim in range(len(lista)-1, 0, -1):
        teve_trocas = False
        for posicao_atual in range(posicao_fim):
            if lista[posicao_atual] > lista[posicao_atual+1]:
                teve_trocas = True
                lista[posicao_atual], lista[posicao_atual+1] = lista[posicao_atual+1], lista[posicao_atual]
        if not teve_trocas:
            break

    return lista


if __name__ == '__main__':
    lista = [random.randrange(1000) for _ in range(10000)]
    lista_ordenada = sorted(lista)
    
    agora = time.time()
    assert selecao_direta(lista.copy()) == lista_ordenada
    print(f"demorou {time.time() - agora} para ordenar com selecao direta")

    agora = time.time()
    assert booble_sort(lista.copy()) == lista_ordenada
    print(f"demorou {time.time() - agora} para ordenar com booble sort")


