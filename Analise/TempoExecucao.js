
function tempoExecucao(funcao){
    var args =Array.prototype.slice.call(arguments,1);

    
    var inicio = performance.now();

    funcao.apply(null,args);

    return performance.now() - inicio;
    // retorna o tempo em milissegundos 
}



module.exports = { tempoExecucao };