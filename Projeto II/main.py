import funcoes as fc
from OrdencaoRaizQuadrada import OrdenacaoRaizQuadrada
import timeit
#from tqdm import tqdm
N  =10**6

print("Tamanho ",N)
vetor_entrada_100 = fc.gerando_amostra(N)
print("Vetor Entrada",vetor_entrada_100)
def main():
    teste2_etapa_4 =OrdenacaoRaizQuadrada(vetor_entrada_100)
    teste2_etapa_4.etapa_4()


qtd_rep = 1
tempo_exc= timeit.timeit(main,number=qtd_rep)

media = tempo_exc/qtd_rep
print(media , "N",N)
