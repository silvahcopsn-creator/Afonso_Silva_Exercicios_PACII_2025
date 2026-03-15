nomes = []
moradas = []

ficheiro = "dados.txt"

with open(ficheiro, 'r') as f:
    for linha in f:
        dados = linha.strip().split(';')
        if len(dados) == 2:
            nomes.append(dados[0])
            moradas.append(dados[1])

while True:
    print("1 - Inserir")
    print("2 - Listar")
    print("3 - Salvar")
    print("4 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        nome = input("Nome: ")
        morada = input("Morada: ")
        nomes.append(nome)
        moradas.append(morada)

    elif opcao == "2":
        if len(nomes) == 0:
            print("Nao ha registos.")
        else:
            print("Registos")
            for i in range(len(nomes)):
                print(f"{i+1}. {nomes[i]} - {moradas[i]}")
    elif opcao == "3":
        with open(ficheiro, 'w') as f:
            for i in range(len(nomes)):
                f.write(f"{nomes[i]};{moradas[i]}\n")
            print("Salvo")
    elif opcao == "4":
        with open(ficheiro, 'w') as f:
            for i in range(len(nomes)):
                f.write(f"{nomes[i]};{moradas[i]}\n")
            print("Salvo")
        print("Adeus")
        break
    else:
        print("Opção inválida")