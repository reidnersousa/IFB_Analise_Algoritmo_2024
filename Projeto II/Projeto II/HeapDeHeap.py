from Heap import Heap

#teste = [[1,12],[10,1],[90]]
teste = [[9, 4, 6], [7, 16, 6], [2, 1, 6],[1]]

#print(len(teste))

class HeapDeHeap:
    
    
    def recebe_vetor(self,vetor):
        self.v = vetor
        self.num_paticoes = len(vetor)
        self.lista_ordenada = []
        
    
    def criar_lista_heaps(self):
        lista_heaps = []
        for i in range(self.num_paticoes):
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
        #print("numero paticoes for ",self.num_paticoes)
        for indice in range (self.num_paticoes):
          
            lista_maiores.append(self.lista_heaps[indice].get_max())  
       
        heap_maior = Heap()
        heap_maior.make_heap(lista_maiores)
        maior = heap_maior.get_max()
        
        self.lista_ordenada.append(maior)
        indice = lista_maiores.index(maior)
       
       
        remove_obj= self.lista_heaps[indice].remove_max()
        
        if remove_obj == True:
            del self.lista_heaps[indice]
            self.num_paticoes = self.num_paticoes - 1
       

       
        
""" 
heap_heap =  HeapDeHeap()
heap_heap.recebe_vetor(teste)


heap_heap.criar_lista_heaps()
heap_heap.convert_lista_heap()

 
while heap_heap.num_paticoes != 0:
    print("\n") 
    heap_heap.get_maior_lista_heap()
    heap_heap.imprimir_heaps()

print(heap_heap.lista_ordenada)

""" 


