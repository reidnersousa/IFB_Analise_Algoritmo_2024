

const {OrdenacaoRaizQuadrada,gerandoAmostra} = require('./OrdenacaoRaizQuadrada')
const {tempoExecucao} = require('./TempoExecucao')
let somaTempos = 0 
const QTD_REPETICOES = 10;
for (i=0;i<QTD_REPETICOES;i++){
    
    vetor_10_4 = gerandoAmostra(10**6);
    const teste= new OrdenacaoRaizQuadrada(vetor_10_4,'Quadrático');
    //console.log(teste.vetor)

    const tempoEx= tempoExecucao(() => teste.etapa4())
    //console.log(tempoEx)
    console.log(">>",teste.vetor_solucao)

    somaTempos += tempoEx


}

var media = somaTempos/QTD_REPETICOES
console.log("media",media)

