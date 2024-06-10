def problema_mochila_prioridade_peso(pesos, valores, tam_mochila):
    # Criar uma lista de tuplas (peso, valor, índice)
    objetos = [(p, v, i) for i, (p, v) in enumerate(zip(pesos, valores))]
    print("objetos",objetos)
    
    # Ordenar os objetos por peso (em ordem crescente)
    objetos.sort(key=lambda x: x[0])
    
    capacidade = 0
    num_itens = 0
    valor_total = 0
    
    for p, v, i in objetos:
        if capacidade + p <= tam_mochila:
            # Se o objeto cabe na mochila, adicioná-lo
            capacidade += p
            num_itens += 1
            valor_total += v
            print(f"Item {i+1}: Peso {p}, Valor {v}")
        else:
            # Se não couber, parar a iteração
            break
    
    print(f"Capacidade utilizada: {capacidade}")
    print(f"Número de itens inseridos: {num_itens}")
    print(f"Valor total: {valor_total}")

# Exemplo de uso:
pesos = [10, 55, 10, 47, 5, 4, 50, 8, 61, 85, 87]
valores = [269, 95, 4, 60, 32, 23, 72, 80, 62, 65, 46]
tam_mochila = 295

problema_mochila_prioridade_peso(pesos, valores, tam_mochila)
