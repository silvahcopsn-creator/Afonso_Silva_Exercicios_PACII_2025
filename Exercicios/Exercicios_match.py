# Afonso Silva Exercicios PAC- 2025140271

#--------------------------------------------s

#Exercicio 1

nome_fim_de_semana = input("Escreva o nome de um dia da semana: ").lower()

match nome_fim_de_semana:
    case "sabado":
        print("fim de semana")
    case "domingo":
        print("fim de semana")
    case _:
        print("dia normal da semana")

#Exercicio 2

nota = int(input("Escreva a sua nota: "))

match nota:
    case n if n >= 90:
        print("Excelente")
    case n if n >= 70:
        print("Bom")
    case n if n >= 50:
        print("Suficiente")
    case _:
        print("Insuficiente")

#Exercicio 3

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

#Exercicio 4

valor = input("Escreve um valor: ")

if valor[0] == "[" and valor[-1] == "]":
    print("Lista")
elif valor.isdigit():
    print("Número inteiro")
elif "." in valor:
    print("Número decimal")
elif valor.isnumeric():
    print("String numérica")
else:
    print("String textual")


#Exercicio 5

mensagem = input("Escreve uma mensagem: ").lower()  

if mensagem == "olá" or mensagem == "bom dia":
    print("Saudação")
elif mensagem.endswith("?"):
    print("Pergunta")
elif "tchau" in mensagem or "adeus" in mensagem:
    print("Despedida")
else:
    print("Mensagem genérica")

#Exercicio 6

servidor = {"status": "ok", "tempo_resposta": 350}

if servidor["status"] == "ok" and servidor["tempo_resposta"] > 200:
    print("Servidor lento")

elif servidor["status"] == "ok":
    print("Servidor ativo")

elif servidor["status"] == "erro":
    print("Servidor indisponível")

else:
    print("Estado desconhecido")


#Exercicio 7

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

#Exercicio 8

def calcular(operacao, n1, n2):
    match operacao:
        case "soma":
            return n1 + n2

        case "subtrai":
            return n1 - n2

        case "multiplica":
            return n1 * n2

        case "divide":
            if n2 != 0:
                return n1 / n2
            else:
                return "Erro: divisão por zero"

        case _:
            return "Operação inválida"


operacao = input("Escreva a operação (soma, subtrai, multiplica, divide): ")
n1 = float(input("Escreva o primeiro número: "))
n2 = float(input("Escreva o segundo número: "))

resultado = calcular(operacao, n1, n2)
print("Resultado:", resultado)

#Exercicio 9

def processar_requisicao(req):
    match req:
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

#Exercicio 10

j1 = input("Jogador 1 (pedra, papel ou tesoura): ").lower()
j2 = input("Jogador 2 (pedra, papel ou tesoura): ").lower()

match (j1, j2):
    case (j1, j2) if j1 == j2:
        print("Empate")
    case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
        print("Jogador 1 venceu")
    case ("tesoura", "pedra") | ("papel", "tesoura") | ("pedra", "papel"):
        print("Jogador 2 venceu")
    case _:
        print("Jogada inválida")