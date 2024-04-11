

//const {OrdenacaoRaizQuadrada,gerandoAmostra} = require('./OrdenacaoRaizQuadrada')
const {analisador_empirico} = require('./TempoExecucao')
let somaTempos = 0 
const QTD_REPETICOES = 2;
for (let i=0;i<QTD_REPETICOES;i++){
    
    console.log("Heap")
    const resultado =analisador_empirico(5,'Heap')
    console.log("vetor_solucao",resultado.vetor_solucao)
   
    console.log(resultado.tempo_execucao  ,"valor de i",i )
    console.log("\n")
    console.log("Quad")
    const resultado_qud =  analisador_empirico(5,'Quadrático')
    console.log("vetor_solucao_quad",resultado_qud.vetor_solucao)
    console.log("\n")
   
   
    

    somaTempos += resultado.tempo_execucao


}
var media = somaTempos/QTD_REPETICOES

console.log("media",media)

