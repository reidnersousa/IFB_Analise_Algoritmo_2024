

const {OrdenacaoRaizQuadrada,gerandoAmostra} = require('./OrdenacaoRaizQuadrada')
vetor = gerandoAmostra(10*1)
/// 10**5 Portanto, 257.085 segundos correspondem a cerca de 4,28 minutos. 😊

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
console.log(teste.vetor)
teste.etapa4()
console.log(">>",teste.vetor_solucao)

//vetor =[ 3,4,7,4,10,6,4,8,4,1]


//teste.buscaSequencial(vetor)
