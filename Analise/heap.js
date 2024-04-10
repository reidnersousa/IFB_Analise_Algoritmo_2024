class Heap {
  constructor(vetor=[]) {

      this.heap = [];
      for(let i =0;i < vetor.length;i++){
        this.insert(vetor[i])
      }
  }

  insert(elemento){
    this.heap.push(elemento)
    this.heapify_up(this.heap.length - 1)
  }
  make_heap(vetor){
    for (let i =0 ; i < vetor.length; i ++){
        this.insert(vetor[i])
    }
  }

  get_max(){
    if (this.heap.length === 0){
        return null
    }
    return this.heap[0]
  }

  remove_max(){
   
   
    const max = this.heap[0]
    this.heap[0] =  this.heap.pop()
    this.heapify_down(0)

    return max 
  }

  heapify_up(index){
    let index_atual =  index
    while (index_atual > 0 ){
        const index_pai  = Math.floor((index_atual - 1)/ 2)
        if (this.heap[index_atual] > this.heap[index_pai]){
            [this.heap[index_atual], this.heap[index_pai]] = [this.heap[index_pai],this.heap[index_atual]]
            index_atual = index_pai
        }
        else {
            break;
        }
    }

  }

  heapify_down(index){
    let index_atual  =  index
    const n = this.heap.length
    while(true){
        let index_esq_filho = 2 * index_atual +  1 
        let index_dir_filho = 2 * index_atual + 2
        let index_pai = index_atual

        if (index_esq_filho < n && this.heap[index_esq_filho] > this.heap[index_pai]){
            index_pai  = index_esq_filho

        }
        if (index_esq_filho < n && this.heap[index_esq_filho] > this.heap[index_pai]){
            index_pai  = index_dir_filho 

        }

        if (index_pai !== index_atual){
            [this.heap[index_atual], this.heap[index_pai]] = [this.heap[index_pai] ,this.heap[index_atual]]
            index_atual = index_pai
        }else{
            break 
        }
        

    }

  }
  heap_to_vetor(){
    return [...this.heap]
  }
}



function encontrar_maiores_elementos(v,vetor_solucao){
    var i =0
    var l = v 
    while(l.length>0){
        var maior_elemento_sub_vetor = []
        
        vetor = l 
        var l =[]
        l.length = 0
        console.log("\n\n")
        console.log("vetor",vetor , "i=[",i)
        for (const sub_vetor of vetor){
            
            heap_pri =  new Heap()
            heap_pri.make_heap(sub_vetor)
          
            maior_elemento_sub_vetor.push(heap_pri.get_max())
           
            
            heap_pri.remove_max()
          
            var vetor =heap_pri.heap_to_vetor()
            if(vetor.length === 0 ){
              continue
            }
            else{
              l.push(vetor) 
            }
            console.log("l dentro do for ",l)
            
        }
        var heap_seg =  new Heap()
        heap_seg.make_heap(maior_elemento_sub_vetor)
        var  maior_de_todos = heap_seg.get_max()
        console.log("Heap_seg",heap_seg)
        vetor_solucao.push(maior_de_todos)
        heap_seg.remove_max()
        //console.log("heap_seg",heap_seg)
        var aux_vetor=heap_seg.heap_to_vetor()
        console.log(">>aux_vetor",aux_vetor)
        
        for(let j =0 ; j  < aux_vetor.length;j++){
            console.log("aux_vetor",aux_vetor[j],"j",j)

            console.log("lll",l)
            l[j].push(aux_vetor[j])
            console.log("lll",l)
           
        }
        console.log("l",l)
       

        console.log("vetor_solucao",vetor_solucao)
        
        i = i + 1 
        if(i ==10){
            break
        }
        
    }


}
// teste [16,9,7],[6,6,6],[4,2,1]

var teste = [[9, 4, 6], [7,16, 6], [2, 1, 6]];
var vetor_solucao = [];

encontrar_maiores_elementos(teste,vetor_solucao)
console.log("Vetor solução:", vetor_solucao);
console.log("Teste final:", teste);



module.exports={Heap,encontrar_maiores_elementos}