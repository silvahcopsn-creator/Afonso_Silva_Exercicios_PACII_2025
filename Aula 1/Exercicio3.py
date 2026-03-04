tipo = input("Escreve o tipo (compra ou venda): ").lower()
valor = input("Escreve o valor: ")

pedido = {"tipo": tipo, "valor": valor}

match pedido["tipo"]:
    case "compra":
        print("Compra de", pedido["valor"], "€")
    case "venda":
        print("Venda de", pedido["valor"], "€")
    case _:
        print("Pedido desconhecido")

