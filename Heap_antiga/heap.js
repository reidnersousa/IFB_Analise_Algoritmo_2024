class Heap {
  constructor() {
      this.lista_maiores = [];
  }

  sort_heap(vetor) {
      var N = vetor.length;

      for (var i = Math.floor(N / 2) - 1; i >= 0; i--) {
          this.heapify(vetor, N, i);
      }
      for (var j = N - 1; j > 0; j--) {
          var temp = vetor[0];
          vetor[0] = vetor[j];
          vetor[j] = temp;
          this.heapify(vetor, j, 0);
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


function encontrar_maiores_elemenentos(teste,vetor_solucao,objeto_heap){




      while (teste.length > 0) {
          var maior_elemento_subarray = [];

          
          for (const subarray of teste) {
              
              objeto_heap.sort_heap(subarray);
              
              maior_elemento_subarray.push(subarray[subarray.length - 1]);
          }

         
          objeto_heap.sort_heap(maior_elemento_subarray);
         
          var maior_de_todo = maior_elemento_subarray[maior_elemento_subarray.length - 1];
          
          vetor_solucao.push(maior_de_todo);

        
          teste = teste.map(subarray =>{
            var filtered = subarray.filter(numero => numero !== maior_de_todo);
            return filtered.length > 0 ? filtered : null;
          }).filter(Boolean);
          
      }
    }
/*
var teste = [[9, 4, 6], [7,16, 6], [2, 2, 6]];
var vetor_solucao = [];
var objeto_heap = new Heap();
encontrar_maiores_elemenentos(teste,vetor_solucao,objeto_heap)
console.log("Vetor solução:", vetor_solucao);
console.log("Teste final:", teste);
*/
module.exports={Heap,encontrar_maiores_elemenentos}