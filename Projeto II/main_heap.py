import funcoes as fc
from OrdencaoRaizQuadrada import OrdenacaoRaizQuadrada
import timeit
N  =10**9

vetor_entrada = fc.gerando_amostra(N)

def main():
    heap_main = OrdenacaoRaizQuadrada(vetor_entrada)
    array_de_array=heap_main.etapa_1()
    #print(array_de_array)
    #print()
    #print(fc.metodo_heap(array_de_array))

tempo_exc= timeit.timeit(main,number=1)
print(tempo_exc)
