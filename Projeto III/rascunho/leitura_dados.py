import os 


dir = os.listdir('instances_01_KP/low-dimensional')

tam_mochila = 'instances_01_KP/low-dimensional-optimum/f1_l-d_kp_10_269'
if os.path.exists(tam_mochila):
    with open(tam_mochila,'r' )as arq:
        tam = arq.read()
        print(tam)
else:
    print("Errro")
                  

caminho_arquivo = 'instances_01_KP/large_scale/knapPI_1_100_1000_1'

if os.path.exists(caminho_arquivo):
    with open(caminho_arquivo,'r')as arquivo:
        conteudo = arquivo.read()

        print(conteudo)
        print(">>",len(conteudo),conteudo[-1])
else :
    print("O arquivo não existe")

v = conteudo.split()

valores = []
pesos = [ ]
for i ,numeros in enumerate (v):
    if i % 2 == 0 :
        valores.append(numeros)
    else :
        pesos.append(numeros)

#print("valores\n",valores)
#print("pesos\n",pesos)
