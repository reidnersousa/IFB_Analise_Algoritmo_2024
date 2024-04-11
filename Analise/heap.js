class Heap {
  constructor(vetor = []) {
    this.heap = [];
    for (let i = 0; i < vetor.length; i++) {
      this.insert(vetor[i]);
    }
  }

  insert(elemento) {
    this.heap.push(elemento);
    this.heapify_up(this.heap.length - 1);
  }

  make_heap(vetor) {
    for (let i = 0; i < vetor.length; i++) {
      this.insert(vetor[i]);
    }
  }

  get_max() {
    if (this.heap.length === 0) {
      return null;
    }
    return this.heap[0];
  }

  remove_max() {
    const max = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.heapify_down(0);
    return max;
  }

  heapify_up(index) {
    let index_atual = index;
    while (index_atual > 0) {
      const index_pai = Math.floor((index_atual - 1) / 2);
      if (this.heap[index_atual] > this.heap[index_pai]) {
        [this.heap[index_atual], this.heap[index_pai]] = [this.heap[index_pai], this.heap[index_atual]];
        index_atual = index_pai;
      } else {
        break;
      }
    }
  }

  heapify_down(index) {
    let index_atual = index;
    const n = this.heap.length;
    while (true) {
      let index_esq_filho = 2 * index_atual + 1;
      let index_dir_filho = 2 * index_atual + 2;
      let index_pai = index_atual;

      if (index_esq_filho < n && this.heap[index_esq_filho] > this.heap[index_pai]) {
        index_pai = index_esq_filho;
      }
      if (index_dir_filho < n && this.heap[index_dir_filho] > this.heap[index_pai]) {
        index_pai = index_dir_filho;
      }

      if (index_pai !== index_atual) {
        [this.heap[index_atual], this.heap[index_pai]] = [this.heap[index_pai], this.heap[index_atual]];
        index_atual = index_pai;
      } else {
        break;
      }
    }
  }

  heap_to_vetor() {
    return [...this.heap];
  }
}

function encontrar_maiores_elementos(v, tamanho_amostra) {
  const heap = new Heap();
  for (const subvetor of v) {
    for (const elemento of subvetor) {
      heap.insert(elemento);
    }
  }
  const vetor_solucao = [];
  for (let i = 0; i < tamanho_amostra && heap.heap.length > 0; i++) {
    vetor_solucao.push(heap.remove_max());
  }
  return vetor_solucao;
}







/*

const teste = [ [ 1, 4, 2 ], [ 5, 5, 1 ], [ 3, 2, 5 ], [ 2 ] ]
const tamanho_amostra = 10;



const vetor_solucao = encontrar_maiores_elementos(teste, tamanho_amostra);
console.log("Vetor solução:", vetor_solucao);
*/


module.exports={Heap,encontrar_maiores_elementos}