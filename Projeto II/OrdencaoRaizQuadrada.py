
import numpy as np
import math 
import funcoes as fc
class OrdenacaoRaizQuadrada:
  def __init__(self,vetor):
    self.vetor = vetor
    self.N = len(vetor)
    self.vetor_solucao =[]

  def bubbleSort(self,array):
    for i in range(len(array)-1,0,-1):
      #print(i)
      for j in range(i):
        #print(">>",i)
        if array[j]>array[j+1]:
          temp = array[j]
          array[j] = array[j+1]
          array[j+1] = temp

  def etapa_1(self):
    qtd_partes = np.sqrt(self.N)
    if self.N % qtd_partes == 0:
      lista = []
      j=0
      for i in range(0,int(qtd_partes)):
        j = j+1

        corte = self.vetor[int(qtd_partes)*i:int(qtd_partes)*j]

        lista.append(corte)

    else:
      ### a ultima parte terá tamanho (N mod chão(sqrt(N)))
      chao_sqrt_n  = math.floor(qtd_partes)
      ultima_parte_tamanho =  self.N % chao_sqrt_n



      lista=[]
      j=0
      for i in range(0,int(qtd_partes)):
        j = j+1

        corte = self.vetor[int(qtd_partes)*i:int(qtd_partes)*j]


        lista.append(corte)
      corte_ultimo = self.vetor[int(qtd_partes)*j:]


      lista.append(corte_ultimo)


    return lista
    ## 2. Encontre o maior elemento ei de cada parte Vi , com 1 ≤ i ≤ k.
  def etapa_2(self):

    lista_maiores = []
    for i in self.array_de_array:
      #print(">>>",i)
      if len(i)>0:
        ### Utilizar o bubble sort aqui
        self.bubbleSort(i)

        maior_elemento=i[-1]
        lista_maiores.append(maior_elemento)
      else :
        pass
    lista_maiores = np.array(lista_maiores)
    self.lista_maiores= lista_maiores

  ### Ajusta etapa 3
  def etapa_3(self):


    maior_numero =  np.max(self.lista_maiores)


    for i,sub_array in enumerate(self.array_de_array):
      for j,numero in enumerate(sub_array):
        
        if numero == maior_numero:

          index_a_remover = np.where(sub_array==maior_numero)[0][0]


          self.array_de_array[i] = np.delete(sub_array, index_a_remover)
          break ## tirando  o break ele remove tudo



    self.vetor_solucao.append(np.max(self.lista_maiores))








  def etapa_4(self):
    #print("entrei aqui")
    #print(self.vetor)
    #print(self.N)
    self.array_de_array=self.etapa_1()

    is_array_cheia = True

    while is_array_cheia == True:

      if  not self.array_de_array :

        is_array_cheia = False
      else:

        #print("cheio")

        #print(self.array_de_array)

        self.etapa_2()
        #print("lista_maiores",self.lista_maiores)  ### array([8, 8, 9, 7])
        self.etapa_3()
        #print(">>",self.vetor_solucao) ##[9]
        self.array_de_array = list(filter(np.any,self.array_de_array))

    print("amostra",self.array_de_array,"vetor solucao",self.vetor_solucao)

"""
teste =  fc.gerando_amostra(11)
print("teste",teste)
#teste = [[9, 4, 6], [7, 16, 6], [2, 1, 6]]

objt_test = OrdenacaoRaizQuadrada(teste)
objt_test.etapa_4()
 """ 