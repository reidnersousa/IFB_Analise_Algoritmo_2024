class Heap {
  constructor() {
      this.lista_maiores = [];
  }

  sort_heap(vetor) {
      var N = vetor.length;

      for (var i = Math.floor(N / 2) - 1; i >= 0; i--) {
          this.heapify(vetor, N, i);
      }
      for (var i = N - 1; i > 0; i--) {
          var temp = vetor[0];
          vetor[0] = vetor[i];
          vetor[i] = temp;
          this.heapify(vetor, i, 0);
      }

      
  }

  heapify(vetor, N, i) {
      let pai = i;
      const filho_esq = 2 * i + 1;
      const filho_dir = 2 * i + 2;

      if (filho_esq < N && vetor[filho_esq] > vetor[pai]) {
          pai = filho_esq;
      }
      if (filho_dir < N && vetor[filho_dir] > vetor[pai]) {
          pai = filho_dir;
      }

      if (pai !== i) {
          const swap = vetor[i];
          vetor[i] = vetor[pai];
          vetor[pai] = swap;
          this.heapify(vetor, N, pai);
      }
  }


}

var teste = [ [ 9, 4, 6 ], [ 2, 6, 6 ], [ 2, 2, 6 ] ];
vetor_solucao = [ ]
maior_elementos = []
const objeto_heap = new Heap();
for(const j of teste){
  console.log("j",j)
  objeto_heap.sort_heap(j)
  maior_elementos.push(j[j.length-1])

}

objeto_heap.sort_heap(maior_elementos)
maior_de_todo = maior_elementos[maior_elementos.length-1]
vetor_solucao.push(maior_de_todo)

console.log("Teste ordenado:", teste , maior_elementos , vetor_solucao);
teste = teste.map(subarray => subarray.filter(numero=> numero !== maior_de_todo ))

console.log("teste",teste)
/// Segunda parte 
maior_elementos = []
for(const j of teste){
  console.log("j",j)
  objeto_heap.sort_heap(j)
  maior_elementos.push(j[j.length-1])

}
objeto_heap.sort_heap(maior_elementos)
maior_de_todo = maior_elementos[maior_elementos.length-1]
vetor_solucao.push(maior_de_todo)

console.log("Teste ordenado:", teste , maior_elementos , vetor_solucao);
teste = teste.map(subarray => subarray.filter(numero=> numero !== maior_de_todo ))
console.log("testw2",teste)
module.exports={Heap}