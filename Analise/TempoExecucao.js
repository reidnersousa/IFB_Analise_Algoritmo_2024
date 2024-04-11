
const {OrdenacaoRaizQuadrada,gerandoAmostra} = require('./OrdenacaoRaizQuadrada')

function tempoExecucao(funcao){
    var args =Array.prototype.slice.call(arguments,1);

    
    var inicio = performance.now();

    funcao.apply(null,args);

    return performance.now() - inicio;
    // retorna o tempo em milissegundos 
}


function analisador_empirico(tamanho_entrada,heap_ou_quadratico){
    const  amostra = gerandoAmostra(tamanho_entrada)
    //console.log("amostrar",amostra)
    const objeto_raiz = new OrdenacaoRaizQuadrada(amostra,heap_ou_quadratico,tamanho_entrada)
    var tempo_execucao =  tempoExecucao(()=>objeto_raiz.etapa4())
    const vetor_solucao = objeto_raiz.vetor_solucao
  
    return {tempo_execucao,vetor_solucao}
}


module.exports = { tempoExecucao ,analisador_empirico};