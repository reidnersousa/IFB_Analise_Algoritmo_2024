### Uma que prioritariamente insere os itens de menor peso, 
### procurando maximizar o número de itens inseridos.


def list_to_int(lista):
    
    return [int(string) for string in lista]


def abordagem_gulosa(valores,pesos,vetor_x,tam_mochila):
    valores = list_to_int(valores)
    pesos = list_to_int(pesos)
    vetor_x = list_to_int(vetor_x)

    objetos = [(v,p,vx,i) for i,(v,p,vx) in enumerate(zip(valores,pesos,vetor_x))]
    
    objetos.sort(key=lambda x : int(x[1]))
    
    capacidade = 0
    num_itens  = 0
    valor_total = 0
    X = []

    for p,v,vx,i in objetos:
        if capacidade + p <= tam_mochila:
            capacidade += p
            num_itens += 1 
            valor_total += v 
            print("Item",i+1,":Peso",p,"Valor",v)
            X.append(1)
        else:
            X.append(0)
            break
    print(f"Capacidade utilizada: {capacidade}")
    print(f"Número de itens inseridos: {num_itens}")
    print(f"Valor total: {valor_total}")