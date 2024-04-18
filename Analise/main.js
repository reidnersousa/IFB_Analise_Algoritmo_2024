

//const {OrdenacaoRaizQuadrada,gerandoAmostra} = require('./OrdenacaoRaizQuadrada')
const {analisador_empirico} = require('./TempoExecucao')
let somaTempos = 0
// 4 ate 8 
const QTD_REPETICOES = 6;
for (let i=1;i<QTD_REPETICOES;i++){
    
   
    const resultado =analisador_empirico(10**i,'Quadrático')
    
   
   
   
    
    console.log("Tempo por i ",i ,resultado.tempo_execucao)
    somaTempos += resultado.tempo_execucao


}
var media = somaTempos/QTD_REPETICOES

console.log("media Heap",media)

