

const {OrdenacaoRaizQuadrada,gerandoAmostra} = require('./OrdenacaoRaizQuadrada')
const {tempoExecucao , analisador_empirico} = require('./TempoExecucao')
let somaTempos = 0 
const QTD_REPETICOES = 1;
for (i=0;i<QTD_REPETICOES;i++){
    const resultado =analisador_empirico(10000,'Heap')
    
    

   
   
    

    somaTempos += resultado.tempo_execucao


}
var media = somaTempos/QTD_REPETICOES

console.log("media",media)

