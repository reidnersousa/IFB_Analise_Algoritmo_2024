from funcao_leitura_large_scale import ler_large_scale
from abordagem_gulosa import abordagem_gulosa

### valores , pesos

v,p,vx =ler_large_scale('instances_01_KP/large_scale/knapPI_1_100_1000_1')
#print(v,"\n",p,"\n",vx)

tam_mochila = 9147
abordagem_gulosa(v,p,vx,tam_mochila)


