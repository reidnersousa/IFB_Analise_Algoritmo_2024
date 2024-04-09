

//const {OrdenacaoRaizQuadrada,gerandoAmostra} = require('./OrdenacaoRaizQuadrada')
const {analisador_empirico} = require('./TempoExecucao')
let somaTempos = 0 
const QTD_REPETICOES = 6;
for (let i=1;i<QTD_REPETICOES;i++){
    const resultado =analisador_empirico(10**i,'Heap')
    
   
    console.log(resultado.tempo_execucao  ,"valor de i",i )
    
    //const resultado_qud =  analisador_empirico(10,'Quadrático')
    //console.log(resultado_qud.tempo_execucao)

   
   
    

    somaTempos += resultado.tempo_execucao


}
var media = somaTempos/QTD_REPETICOES

console.log("media",media)

