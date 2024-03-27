function gerandoAmostra(N) {
    const sequencia = [];
    for (let i = 0; i < N; i++) {
      sequencia.push(Math.floor(Math.random() * N) + 1);
    }
    return sequencia;
  }
  
  class OrdenacaoRaizQuadrada {
    constructor(vetor) {
      this.vetor = vetor;
      this.N = vetor.length;
      this.vetor_solucao = [];
    }
  
    bubbleSort(array) {
      for (let i = array.length - 1; i > 0; i--) {
        for (let j = 0; j < i; j++) {
          if (array[j] > array[j + 1]) {
            const temp = array[j];
            array[j] = array[j + 1];
            array[j + 1] = temp;
          }
        }
      }
    }
  
    etapa1() {
      const qtd_partes = Math.sqrt(this.N);
      
      const lista = [];
      if (this.N % qtd_partes === 0) {
        
        var j=0;
        for (let i = 0; i < qtd_partes; i++) {
          j = j +1;
          const corte = this.vetor.slice(qtd_partes * i, qtd_partes *j);
         
          lista.push(corte);
        }   
      } else {
        const chao_sqrt_n = Math.floor(qtd_partes);
        const ultima_parte_tamanho = this.N % chao_sqrt_n;
        
        var j = 0;
        for (let i = 0; i < qtd_partes; i++) {
          
          j = j +1;
          const corte = this.vetor.slice(qtd_partes * i, qtd_partes * j);
         
          lista.push(corte);
        }
  
        //const corte_ultimo = this.vetor.slice(qtd_partes * j);
        //lista.push(corte_ultimo);
        //console.log(">>",corte_ultimo)
      }
  
      return lista;
    }
  }

  

  module.exports = {OrdenacaoRaizQuadrada ,gerandoAmostra};


