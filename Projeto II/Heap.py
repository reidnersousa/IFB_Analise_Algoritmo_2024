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

        max_element = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return max_element

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


def encontrar_maiores_elementos(v, vetor_solucao):
    i = 0
    l = v
    while len(l) > 0:
        maior_elemento_sub_vetor = []

        vetor = l
        l = []
        print("\n\n")
        print("vetor", vetor, "i=", i)
        for sub_vetor in vetor:
            heap_pri = Heap()
            heap_pri.make_heap(sub_vetor)

            maior_elemento_sub_vetor.append(heap_pri.get_max())

            heap_pri.remove_max()

            vetor = heap_pri.heap_to_vetor()
            if len(vetor) == 0:
                continue
            else:
                l.append(vetor)
            print("l dentro do for ", l)

        heap_seg = Heap()
        heap_seg.make_heap(maior_elemento_sub_vetor)
        maior_de_todos = heap_seg.get_max()
        print("Heap_seg", heap_seg)
        vetor_solucao.append(maior_de_todos)
        heap_seg.remove_max()
        aux_vetor = heap_seg.heap_to_vetor()
        print(">>aux_vetor", aux_vetor)

        for j in range(len(aux_vetor)):
            print("aux_vetor", aux_vetor[j], "j", j)

            print("lll", l)
            l[j].extend([aux_vetor[j]])
            print("lll", l)

        print("l", l)

        print("vetor_solucao", vetor_solucao)

        i += 1
        if i == 10:
            break


# teste [16,9,7],[6,6,6],[4,2,1]
""" 
teste = [[9, 4, 6], [7, 16, 6], [2, 1, 6]]
vetor_solucao = []

encontrar_maiores_elementos(teste, vetor_solucao)
print("Vetor solução:", vetor_solucao)
print("Teste final:", teste)
""" 