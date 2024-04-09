

const {OrdenacaoRaizQuadrada,gerandoAmostra} = require('./OrdenacaoRaizQuadrada')
const {tempoExecucao , analisador_empirico} = require('./TempoExecucao')
let somaTempos = 0 
const QTD_REPETICOES = 1;
for (i=0;i<QTD_REPETICOES;i++){
    const resultado =analisador_empirico(10**4,'Heap')
    //const resultado_qud =  analisador_empirico(10,'Quadrático')
    console.log(resultado.tempo_execucao)
    //console.log(resultado_qud.tempo_execucao)

   
   
    

    somaTempos += resultado.tempo_execucao


}
var media = somaTempos/QTD_REPETICOES

console.log("media",media)

