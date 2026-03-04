def processar_requisicao(req):
    match req:
        # GET
        case {"metodo": "GET", "conteudo": _}:
            return "Requisição GET recebida"

        case {"metodo": "POST", "conteudo": conteudo} if conteudo != "":
            return "Requisição POST com dados válidos"

        case {"metodo": "POST", "conteudo": ""}:
            return "Requisição POST sem dados"

        case _:
            return "Método não suportado"


metodo = input("Escreva o método (GET ou POST): ")
conteudo = input("Escreva o conteúdo: ")

requisicao = {
    "metodo": metodo,
    "conteudo": conteudo
}

resultado = processar_requisicao(requisicao)
print("Resultado:", resultado)