import funcoes as fc
from OrdencaoRaizQuadrada import OrdenacaoRaizQuadrada
import timeit
N  =10**5
print("Tamanho ",N)
vetor_entrada_100 = fc.gerando_amostra(N)

def main():
    teste2_etapa_4 =OrdenacaoRaizQuadrada(vetor_entrada_100)
    teste2_etapa_4.etapa_4()

tempo_exc = timeit.timeit(main,number=1)