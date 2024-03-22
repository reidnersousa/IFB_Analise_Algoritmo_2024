
import numpy as np
import random
import timeit
import matplotlib.pyplot as plt

class Manager:
  def __init__(self, input_10_4 , input_10_5,input_10_6,input_10_7,quantidade_buscas,nome):
    random.seed(42)
    self.nome = nome
    self.QTD_REPETICAO_FOR  = quantidade_buscas

    self.input_4 = input_10_4
    self.input_5 = input_10_5
    self.input_6 = input_10_6
    self.input_7 = input_10_7


    self.amostra_10_4 = self.gerando_amostra(input_10_4)
    self.amostra_10_5 = self.gerando_amostra(input_10_5)
    self.amostra_10_6 = self.gerando_amostra(input_10_6)
    self.amostra_10_7 = self.gerando_amostra(input_10_7)


    self.tempo_sequencial =np.empty(0)
    self.calcular_tempo_sequencial()

    self.tempo_sequencial_otimizado = np.empty(0)
    self.calcular_tempo_sequencial_otimizado()



    self.tempo_binaria = np.empty(0)
    self.calcular_tempo_binaria()






  def calcular_tempo_sequencial(self):
    tempo_sequencial = np.zeros(4)

    tempo_sequencial[0] =self.get_time(self.input_4,self.busca_sequencial)
    tempo_sequencial[1] =self.get_time(self.input_5,self.busca_sequencial)
    tempo_sequencial[2] =self.get_time(self.input_6,self.busca_sequencial)
    tempo_sequencial[3]= self.get_time(self.input_7,self.busca_sequencial)


    self.tempo_sequencial = tempo_sequencial

  def calcular_tempo_sequencial_otimizado(self):
    tempo_sequencial_otimizado = np.zeros(4)

    tempo_sequencial_otimizado[0] =self.get_time(self.input_4,self.busca_sequencial_otimizada)
    tempo_sequencial_otimizado[1] =self.get_time(self.input_5,self.busca_sequencial_otimizada)
    tempo_sequencial_otimizado[2] =self.get_time(self.input_6,self.busca_sequencial_otimizada)
    tempo_sequencial_otimizado[3]= self.get_time(self.input_7,self.busca_sequencial_otimizada)


    self.tempo_sequencial_otimizado = tempo_sequencial_otimizado

  def calcular_tempo_binaria(self):
    tempos_binarios = np.zeros(4)

    tempos_binarios[0] = self.get_time(self.input_4, self.busca_binaria)
    tempos_binarios[1] = self.get_time(self.input_5, self.busca_binaria)
    tempos_binarios[2] = self.get_time(self.input_6, self.busca_binaria)
    tempos_binarios[3] = self.get_time(self.input_7, self.busca_binaria)

    self.tempo_binaria = tempos_binarios



  def get_time(self,entrada,metodo_busca):
    lista_tempo =[]

    for _ in range(self.QTD_REPETICAO_FOR):



      if entrada == 10000:
        amostra = self.amostra_10_4
      elif entrada == 100000:
        amostra = self.amostra_10_5
      elif entrada == 1000000:
        amostra = self.amostra_10_6
      elif entrada == 10000000:
        amostra = self.amostra_10_7



      tempo_sequencial = timeit.timeit(lambda: metodo_busca(amostra),number=1)
      lista_tempo.append(tempo_sequencial)

    soma_do_tempo = np.sum(lista_tempo)

    print("nome metodo: {} tamanho amostra: {:.0e} tempo {:.6f}".format(metodo_busca.__name__, len(amostra), soma_do_tempo))
    return soma_do_tempo

  def gerando_amostra(self,N):
    sequencia = np.random.randint(1, N + 1, N)
    return sequencia

  def busca_sequencial(self,vetor,alvo=None):

    encontrou = False
    if alvo is None:
      alvo = np.random.randint(1,len(vetor)+1)

    for _ ,valor in enumerate(vetor):

      if valor == alvo:
        encontrou = True
        break

    return encontrou

  def busca_sequencial_otimizada(self,vetor,alvo = None):
    encontrou = False

    if alvo is None:
      alvo = np.random.randint(1,len(vetor)+1)

    for i in range(len(vetor)):

      if alvo < vetor[i]:
        encontrou = False
        break
      elif alvo ==vetor[i]:

        encontrou = True
        break


    return encontrou

  def busca_binaria(self,vetor,alvo = None):

    if alvo is None:
      alvo = np.random.randint(1,len(vetor)+1)


    primeiro = 0
    ultimo  = len(vetor)-1
    encontrou = False

    while primeiro <= ultimo  and  not encontrou:

      m = (primeiro + ultimo )//2

      if vetor[m]== alvo:

        encontrou = True
        break

      else :

        if vetor[m]< alvo :
          primeiro = m+1

        elif vetor[m]> alvo :
          ultimo = m-1


    return encontrou

  def gerando_grafico(self):
    tamanho =[1e4,1e5,1e6,1e7]
    tempo=[]

    tempo.append(self.tempo_sequencial)
    tempo.append(self.tempo_sequencial_otimizado)
    tempo.append(self.tempo_binaria)

    algoritmo =['busca sequencial','busca sequencial otimizada','busca binaria']
    plt.figure(figsize=(6,8))
    plt.title(f"Comparação de Tempo quando o numero de busca(q)={self.nome}")
    plt.plot(tamanho ,tempo[0] , label=algoritmo[0],color='blue',linestyle='--')
    plt.plot(tamanho ,tempo[1] , label=algoritmo[1],color='red',linestyle='solid')
    plt.plot(tamanho ,tempo[2] , label=algoritmo[2],color='black',linestyle='--')
    plt.xlabel("Tamanho da Amostra")
    plt.ylabel("Tempo (s)")
    plt.xscale("log")
    plt.yscale("log")



    plt.legend()
    plt.savefig(f'grafido_quando_q={self.nome}.png')


#teste = Manager(10**4,10**5,10**6,10**7,2,'q = teste')
#teste.gerando_grafico()
