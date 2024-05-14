import numpy as np
import math
import random
from HeapDeHeap import HeapDeHeap




def metodo_heap(entrada):
   
  heap_heap = HeapDeHeap()
  heap_heap.recebe_vetor(entrada)
  heap_heap.criar_lista_heaps()
  heap_heap.convert_lista_heap()

  while heap_heap.num_paticoes != 0:
      #print("\n")
      heap_heap.get_maior_lista_heap()
      #heap_heap.imprimir_heaps()
  return heap_heap.lista_ordenada
 # print(heap_heap.lista_ordenada)


   


def gerando_amostra(N):
  sequencia = np.random.randint(1, N + 1, N)
  return sequencia


def eh_multiplo(N,qtd_partes):
  return N % qtd_partes ==0


### teste = [[9, 4, 6], [7, 16, 6], [2, 1, 6],[1]]  ## A metodo_heap espera os dados assim

#teste = gerando_amostra(100)
#print(teste)
#print(metodo_heap(teste))    