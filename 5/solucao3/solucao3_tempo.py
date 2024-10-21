# pip install line-profiler memory-profiler
# para executar o codigo: python -m memory_profiler solucao3_memoria.py (para memória) ////  python -m kernprof -l -v solucao3_tempo.py (para tempo)

from line_profiler import profile #type: ignore

@profile
def tem_duplicados(lista):
    elementos_vistos = set()
    for elemento in lista:
        if elemento in elementos_vistos:
            return True
        elementos_vistos.add(elemento)
    return False
    
    
if __name__ == '__main__':
    lista_teste = [1, 2, 5, 2, 1, 2, 3, 4, 5, 6, 3]
    tem_duplicados(lista_teste)