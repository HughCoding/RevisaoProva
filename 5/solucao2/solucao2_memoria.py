# pip install line-profiler memory-profiler
# para executar o codigo: python -m memory_profiler solucao2_memoria.py (para memória) ////  python -m kernprof -l -v solucao2_tempo.py (para tempo)
  
from memory_profiler import profile as mem_profile #type: ignore

@mem_profile
def tem_duplicados(lista):
    lista_ordenada = sorted(lista)
    for i in range(len(lista_ordenada) - 1):
        if lista_ordenada[i] == lista_ordenada[i + 1]:
            return True
    return False

if __name__ == '__main__':
    lista_teste = [1, 2, 5, 2, 1, 2, 3, 4, 5, 6, 3]
    tem_duplicados(lista_teste)