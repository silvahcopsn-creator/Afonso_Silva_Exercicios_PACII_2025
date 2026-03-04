def analisar_produto(produto):
    match produto:
        case {"categoria": "eletrônico", "preco": preco} if preco > 1000:
            return "Produto de luxo"

        case {"categoria": "eletrônico", "preco": preco} if preco <= 1000:
            return "Produto comum"

        case {"categoria": "alimento", "preco": _}:
            return "Produto alimentar"

        case _:
            return "Categoria desconhecida"

entrada = {"categoria": "eletrônico", "preco": 1500}
print(analisar_produto(entrada))