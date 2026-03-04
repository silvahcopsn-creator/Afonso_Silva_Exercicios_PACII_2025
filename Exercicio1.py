nome_fim_de_semana = input("Escreva o nome de um dia da semana: ").lower()

match nome_fim_de_semana:
    case "sabado":
        print("fim de semana")
    case "domingo":
        print("fim de semana")
    case _:
        print("dia normal da semana")