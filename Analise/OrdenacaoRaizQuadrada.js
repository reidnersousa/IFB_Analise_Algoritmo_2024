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


    etapa2() {
        const lista_maiores = [];
        for (const i of this.array_de_array) {
          if (i.length > 0) {
            // Utilize o bubble sort aqui
            this.bubbleSort(i);
    
            const maior_elemento = i[i.length - 1];
            lista_maiores.push(maior_elemento);
          }
        }
        this.lista_maiores = lista_maiores;
      }

      etapa3() {
       
        
        const maior_numero = Math.max(...this.lista_maiores);
        
        for (let i = 0; i < this.array_de_array.length; i++) {
          const sub_array = this.array_de_array[i];
          for (let j = 0; j < sub_array.length; j++) {
            const numero = sub_array[j];
            if (numero === maior_numero) {
            
              const index_a_remover = sub_array.indexOf(maior_numero);
              
              this.array_de_array[i].splice(index_a_remover, 1);
              
              break;
            }
          }
        }
        
        this.vetor_solucao.push(Math.max(...this.lista_maiores));
        
    }

    etapa4() {
        console.log("entrei aqui");
        console.log(this.vetor);
        console.log(this.N);
        this.array_de_array = this.etapa1();
      
        let is_array_cheia = true;
      
        while (is_array_cheia) {
          if (!this.array_de_array  || !this.array_de_array.length) {
            is_array_cheia = false;
          } else {
            this.etapa2();
            this.etapa3();
            this.array_de_array = this.array_de_array.filter(sub_array => sub_array.length > 0);
          }
        }
      
        //console.log(this.array_de_array, ">>", this.vetor_solucao);
      }
      

  }

  

  module.exports = {OrdenacaoRaizQuadrada ,gerandoAmostra};


