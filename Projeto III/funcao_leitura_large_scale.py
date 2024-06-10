import os 

def ler_large_scale(dir_path):
    if os.path.exists(dir_path):
        with open(dir_path,'r') as arquivo:
            conteudo = arquivo.read()
    else:
        print("O arquivo não existe")
    
    linhas =  conteudo.split('\n')
    vetor_x = linhas[-2]
    linhas.pop(-2)
    conteudo = '\n'.join(linhas)

    v =  conteudo.split()

    valores = []
    pesos = []
    for i,num in enumerate(v):
        if i % 2 ==0:
            valores.append(num)
        else:
            pesos.append(num)
    
    vetor_x = vetor_x.split()

  #  print('valores\n',valores)
   # print('pesos\n',pesos)
   # print('vetorX\n',vetor_x)

    return valores,pesos,vetor_x

#v,p,vx =ler_large_scale('instances_01_KP/large_scale/knapPI_1_100_1000_1')
#print(v,"\n",p,"\n",vx)