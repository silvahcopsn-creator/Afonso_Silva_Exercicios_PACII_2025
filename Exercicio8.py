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