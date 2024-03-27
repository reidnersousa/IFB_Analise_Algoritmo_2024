

const {OrdenacaoRaizQuadrada,gerandoAmostra} = require('./OrdenacaoRaizQuadrada')
vetor = gerandoAmostra(16)
//vetor =[ 3,4,7,4,10,6,4,8,4,1]
const teste = new OrdenacaoRaizQuadrada(vetor);

resultado=teste.etapa1()
console.log(">>",resultado)