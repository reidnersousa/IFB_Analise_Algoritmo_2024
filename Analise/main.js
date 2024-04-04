

const {OrdenacaoRaizQuadrada,gerandoAmostra} = require('./OrdenacaoRaizQuadrada')
const {tempoExecucao} = require('./TempoExecucao')
let somaTempos = 0 
const QTD_REPETICOES = 1;
for (i=0;i<QTD_REPETICOES;i++){
    
    vetor_10_4 = gerandoAmostra(9);
    console.log(vetor_10_4)
    
    const teste1= new OrdenacaoRaizQuadrada(vetor_10_4,'Quadrático');
    
    const tempoEx1= tempoExecucao(() => teste1.etapa4())
    console.log("Teste1 ",teste1.vetor_solucao)
    
    
    console.log('\n\n')
    

   
   
    

    //somaTempos += tempoEx


}


var media = somaTempos/QTD_REPETICOES
console.log("media",media)

