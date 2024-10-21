# pip install line-profiler memory-profiler
# para executar o codigo: python -m memory_profiler solucao1_memoria.py (para memória) ////  python -m kernprof -l -v solucao1_tempo.py (para tempo)

from line_profiler import profile #type: ignore

@profile
def tem_duplicados(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

if __name__ == '__main__':
    lista_teste = [1, 2, 5, 2, 1, 2, 3, 4, 5, 6, 3]
    tem_duplicados(lista_teste)
