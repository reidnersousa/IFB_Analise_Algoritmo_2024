import os 
caminho_arquivo = 'instances_01_KP/large_scale/knapPI_1_100_1000_1'

if os.path.exists(caminho_arquivo):
    with open(caminho_arquivo,'r')as arquivo:
        conteudo = arquivo.read()
       
else :
    print("O arquivo não existe")


#print(conteudo)

linhas = conteudo.split('\n')

ultima_linha = linhas[-2] 
print()
linhas.pop(-2)
print(linhas)
conteudo  = '\n'.join(linhas)
#print(conteudo)


v = conteudo.split()

valores = []
pesos = [ ]
for i ,numeros in enumerate (v):
    if i % 2 == 0 :
        valores.append(numeros)
    else :
        pesos.append(numeros)

ultima_linha = ultima_linha.split()
print("valores\n",valores)
print("pesos\n",pesos)
print("vetorX\n",ultima_linha)
