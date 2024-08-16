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

qtd_rep = 50
tempo_exc= timeit.timeit(main,number=qtd_rep)

media = tempo_exc/qtd_rep
print(media , "N",N)
