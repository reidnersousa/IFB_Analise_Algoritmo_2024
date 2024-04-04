
class Heap{
    constructor(vetor){
      this.sort_heap(vetor)
      this.lista_maiores =[]
      this.get_maiores_elementos(vetor)
    }
  
    sort_heap(vetor){
      var  N = vetor.length
  
      for(var  i = Math.floor(N/2)-1;i>=0;i--){
        this.heapify(vetor,N,i)
      }
      for(var  i =N-1; i> 0;i-- ){
        var temp = vetor[0]
        vetor[0] = vetor[i]
        vetor[i] = temp
        this.heapify(vetor,i,0)
      }
    }
  
    heapify(vetor,N,i){
      let pai = i
      const filho_esq = 2*i+1
      const filho_dir = 2*i+2
  
      if (filho_esq < N && vetor[filho_esq] > vetor[pai]){
        pai = filho_esq
      }
      if (filho_dir < N && vetor[filho_dir] > vetor[pai]){
        pai = filho_dir
      }
  
      if (pai !== i){
        const swap = vetor[i]
        vetor[i] = vetor[pai]
        vetor[pai]=swap
        this.heapify(vetor,N,pai)
  
      }
  
    }
  
    remover_heap(vetor){
      const maior_numero = vetor.pop()
      return maior_numero
    }
  
    get_maiores_elementos(vetor){
      while(vetor.length > 0){
        this.sort_heap(vetor)
        const maior_num = this.remover_heap(vetor)
        this.lista_maiores.push(maior_num)
      }
  
    }
  }
  
  var teste = [1, 2, 7, 3, 6, 4, 8, 5, 123, 10]
  
  const t = new Heap(teste)
  console.log(t.lista_maiores)