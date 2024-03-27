

const {OrdenacaoRaizQuadrada,gerandoAmostra} = require('./OrdenacaoRaizQuadrada')
vetor = gerandoAmostra(16)
//vetor =[ 3,4,7,4,10,6,4,8,4,1]
const teste = new OrdenacaoRaizQuadrada(vetor);
/*
teste.etapa1()
console.log(teste.array_de_array)
teste.etapa2()
teste.etapa3()
console.log(">>",teste.lista_maiores)
console.log(teste.vetor_solucao)

*/
teste.etapa4()
console.log(">>",teste.vetor_solucao)