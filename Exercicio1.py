nome_fim_de_semana = input("Escreva o nome de um dia da semana: ").lower()

if nome_fim_de_semana in ["sabado", "domingo"]:
    print("fim de semana")
else:
    print("dia normal da semana")