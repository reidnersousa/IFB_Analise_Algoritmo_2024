class Heap:
    def __init__(self, vetor=[]):
        self.heap = []
        for elemento in vetor:
            self.insert(elemento)

    def insert(self, elemento):
        self.heap.append(elemento)
        self.heapify_up(len(self.heap) - 1)

    def make_heap(self, vetor):
        for elemento in vetor:
            self.insert(elemento)

    def get_max(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def remove_max(self):
        if len(self.heap) == 0:
            return None

        try :
            self.heap[0] = self.heap.pop()
            self.heapify_down(0)
            return False 
        except IndexError:
            return True 
    def heapify_up(self, index):
        index_atual = index
        while index_atual > 0:
            index_pai = (index_atual - 1) // 2
            if self.heap[index_atual] > self.heap[index_pai]:
                self.heap[index_atual], self.heap[index_pai] = self.heap[index_pai], self.heap[index_atual]
                index_atual = index_pai
            else:
                break

    def heapify_down(self, index):
        index_atual = index
        n = len(self.heap)
        while True:
            index_esq_filho = 2 * index_atual + 1
            index_dir_filho = 2 * index_atual + 2
            index_pai = index_atual

            if index_esq_filho < n and self.heap[index_esq_filho] > self.heap[index_pai]:
                index_pai = index_esq_filho

            if index_dir_filho < n and self.heap[index_dir_filho] > self.heap[index_pai]:
                index_pai = index_dir_filho

            if index_pai != index_atual:
                self.heap[index_atual], self.heap[index_pai] = self.heap[index_pai], self.heap[index_atual]
                index_atual = index_pai
            else:
                break

    def heap_to_vetor(self):
        return self.heap[:]





# teste [16,9,7],[6,6,6],[4,2,1]
""" 
teste = [[9, 4, 6], [7, 16, 6], [2, 1, 6]]
vetor_solucao = []

encontrar_maiores_elementos(teste, vetor_solucao)
print("Vetor solução:", vetor_solucao)
print("Teste final:", teste)
""" 