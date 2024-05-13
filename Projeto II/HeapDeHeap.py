from Heap import Heap


teste = [[9, 4, 6], [7, 16, 6], [2, 1, 6],[1]]

print(len(teste))

class HeapDeHeap:
    
    
    def recebe_vetor(self,vetor):
        self.v = vetor
        self.tam = len(vetor)
        
    
    def criar_lista_heaps(self):
        lista_heaps = []
        for i in range(self.tam):
            h = Heap()
            lista_heaps.append(h)
        self.lista_heaps = lista_heaps

    def convert_lista_heap(self):
        for indice,num in enumerate(self.v):
            self.lista_heaps[indice].make_heap(num) 


    def imprimir_heaps(self):
        for indice, heap in enumerate(self.lista_heaps):
            print("Heap {}:".format(indice))
            print(heap.heap)    

    def get_maior_lista_heap(self):
         
        lista_maiores = []
        for indice in range (len(self.v)):
          
            lista_maiores.append(self.lista_heaps[indice].get_max())  
       
        heap_maior = Heap()
        heap_maior.make_heap(lista_maiores)
        maior = heap_maior.get_max()
        

        indice = lista_maiores.index(maior)
       

        self.lista_heaps[indice].remove_max()

       
        

heap_heap =  HeapDeHeap()
heap_heap.recebe_vetor(teste)
heap_heap.criar_lista_heaps()
heap_heap.convert_lista_heap()
heap_heap.imprimir_heaps()
heap_heap.get_maior_lista_heap()
print("SSSS")
heap_heap.imprimir_heaps()

