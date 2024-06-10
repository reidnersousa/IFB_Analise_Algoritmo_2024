pesos = ['10', '55', '10', '47', '5', '4', '50', '8', '61', '85', '87']

valores = ['269', '95', '4', '60', '32', '23', '72', '80', '62', '65', '46']


tam_mochila =295

def list_to_int(lista):
    
    return [int(string) for string in lista]


pesos=list_to_int(pesos)
valores = list_to_int (valores)

def primeira_abordagem (pesos, valores,tam_mochila):
    capacidade = 0
    custo  = 0
    print(pesos,valores)
    ### Uma que prioritariamente 
    while capacidade < tam_mochila:
        menor_valor = min(pesos)
        indice_do_menor = pesos.index(menor_valor)
        print("valores",valores[indice_do_menor],"pesos",pesos[indice_do_menor])

                    
        custo = custo+valores[indice_do_menor]
        capacidade =  capacidade + pesos[indice_do_menor]
       
        pesos.pop(indice_do_menor)
        valores.pop(indice_do_menor)
        print(">>",pesos,valores)


    print(capacidade , custo)
    return None

primeira_abordagem(pesos,valores,tam_mochila)
