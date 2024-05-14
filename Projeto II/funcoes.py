import numpy as np
import math
import random
from HeapDeHeap import HeapDeHeap


teste = [[9, 4, 6], [7, 16, 6], [2, 1, 6],[1]]


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

print(metodo_heap(teste))    
   


def gerando_amostra(N):
  sequencia = np.random.randint(1, N + 1, N)
  return sequencia


def eh_multiplo(N,qtd_partes):
  return N % qtd_partes ==0
