# Afonso Silva Exercicios PAC- 2025140271

#--------------------------------------------

#Exercicio 1

def numeros():
    
    numeros_pares= [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
    numeros_impares= [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]

    print("Números pares:", numeros_pares)
    print("Numeros impares:", numeros_impares)

numeros()

#Exercicio 2

for i in range (10):
    numero= int(input("Escreva o número:"))

    if numero % 2== 0:
        print("O numero é par")
    else:
        print("O número é ímpar")

#Exercicio 3

sum = 0

for i in range (10):

    nota= int(input("Escreva a nota dos alunos: "))
    sum= sum + nota 

media = sum  / 10

print("A sua média é:", media)

#Exercicio 4

numero = int(input("Escreva o número: "))

divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1

if divisores == 2:
    print("O número é primo")
else:
    print("O número não é primo")

#Exercicio 5

for i in range (1, 10001):
    print(i)

#Exercicio 6

primos = []
num = 2

while len(primos) < 10:
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
    if primo:
        primos.append(num)
    num += 1

print(primos)

#Exercicio 7

for i in range(10, 1001, 10):
    print(i)

#Exercicio 8

for i in range(10, 1001, 10):
    print(i)

for i in range(15, 996, 10):
    print(i)

#Exercicio 9

while True:
    num = int(input("Digite um número entre 1 e 100: "))
    
    if 1 <= num <= 100:
        break

#Exercicio 10

num = int(input("Digite um número: "))
divisores = 0

for i in range(1, num + 1):
    if num % i == 0:
        divisores += 1

print("Quantidade de divisores:", divisores)

#Exercicio 11

for i in range(1, 6):
    print(str(i) * i)

#Exercicio 12

num = int(input("Digite um número: "))
operacoes = 0

for i in range(1, num):
    print(num, "+", i, "=", num + i)
    print(num, "-", i, "=", num - i)
    print(num, "*", i, "=", num * i)
    print(num, "/", i, "=", num / i)
    
    operacoes += 4

print("Total de operações:", operacoes)


#Exercicio 13

num = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#Exercicio 14

for num in range(1, 101):
    print(f"Tabuada do {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print("-" * 20)  

#Exercicio 15

continuar = True
codigo = 0

while continuar and codigo <= 255:
    for i in range(20):
        if codigo > 255:
            break
        print(f"{codigo}: {chr(codigo)}", end="\t")
        codigo += 1
    print()  
    
    if codigo <= 255:
        resposta = input("Deseja continuar? (s/n): ").lower()
        if resposta != 's':
            continuar = False

#Exercicio 17

total = 0
contador = 0

while contador < 30:
    try:
        num = int(input(f"Digite o {contador+1}º número par (1 a 50): "))
    except ValueError:
        print("Valor inválido! Digite um número inteiro.")
        continue
    
    if 1 <= num <= 50 and num % 2 == 0:
        total += num
        contador += 1
    else:
        print("Número inválido! Deve ser par e entre 1 e 50.")

media = total / 30
print(f"A média dos 30 números pares é: {media}")

#Exercicio 18

limite = int(input("Digite um número limite: "))
contador_perfeitos = 0

for num in range(1, limite + 1):
    soma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            soma_divisores += i
    if soma_divisores == num:
        print(f"{num} é um número perfeito")
        contador_perfeitos += 1

print(f"Existem {contador_perfeitos} números perfeitos até {limite}.")

#Exercicio 19

n = 60
serie = [0, 1]  

while len(serie) < n:
    proximo = serie[-1] + serie[-2]
    serie.append(proximo)

for i, num in enumerate(serie, start=1):
    print(f"{i}: {num}")

#Teste final 1

def is_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def contar_divisores(n):
    cont = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cont += 1
    return cont


def numero_perfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma == n


def analisar_numeros():
    while True:
        try:
            num = int(input("Introduza um número (1-30000): "))
            if 1 <= num <= 30000:
                break
            else:
                print("Valor fora do intervalo.")
        except:
            print("Entrada inválida.")

    contador = 0

    for i in range(num, 0, -1):

        primo = is_primo(i)
        divisores = contar_divisores(i)
        perfeito = numero_perfeito(i)

        print(f"\nNúmero: {i}")
        print("Primo:", primo)
        print("Divisores:", divisores)
        print("Perfeito:", perfeito)

        contador += 1

        if contador % 10 == 0:
            opc = input("Continuar? (s/n): ")
            if opc.lower() != "s":
                break


def calculadora():
    while True:

        print("\nCalculadora")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Tabuada")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "0":
            break

        if op == "5":

            while True:
                try:
                    n = int(input("Número para tabuada (1-1000): "))
                    if 1 <= n <= 1000:
                        break
                    else:
                        print("Valor inválido.")
                except:
                    print("Entrada inválida.")

            contador = 0

            for i in range(1, n + 1):
                print(f"{n} x {i} = {n*i}")

                contador += 1
                if contador % 20 == 0:
                    c = input("Continuar? (s/n): ")
                    if c.lower() != "s":
                        break

        else:
            try:
                a = float(input("Primeiro número: "))
                b = float(input("Segundo número: "))
            except:
                print("Entrada inválida.")
                continue

            if op == "1":
                print("Resultado:", a + b)
            elif op == "2":
                print("Resultado:", a - b)
            elif op == "3":
                print("Resultado:", a * b)
            elif op == "4":
                if b != 0:
                    print("Resultado:", a / b)
                else:
                    print("Erro: divisão por zero")
            else:
                print("Opção inválida")


def menu():
    while True:
        print("\nMENU")
        print("1 - Analisar números")
        print("2 - Calculadora")
        print("0 - Sair")

        escolha = input("Escolha: ")

        if escolha == "1":
            analisar_numeros()
        elif escolha == "2":
            calculadora()
        elif escolha == "0":
            print("Programa terminado.")
            break
        else:
            print("Opção inválida")


menu()

#Teste final 2

clientes = []
num_cliente = 1


def calcular_divida(compra):
    if 100 <= compra <= 200:
        desconto = compra * 0.05
    elif 200 < compra < 500:
        desconto = compra * 0.10
    elif compra >= 500:
        desconto = compra * 0.15
    else:
        desconto = 0

    divida_final = compra - desconto
    return desconto, divida_final


def inserir_cliente():
    global num_cliente

    nome = input("Nome do cliente: ").strip()
    morada = input("Morada: ").strip()

    while True:
        tel = input("Telefone: ")
        if tel.isdigit():
            break
        else:
            print("Telefone inválido.")

    while True:
        nif = input("NIF: ")
        if nif.isdigit() and len(nif) == 9:
            break
        else:
            print("NIF inválido.")

    while True:
        try:
            compra = float(input("Valor da compra: "))
            if compra >= 0:
                break
            else:
                print("Valor inválido.")
        except:
            print("Entrada inválida.")

    desconto, divida = calcular_divida(compra)

    cliente = {
        "num": num_cliente,
        "nome": nome,
        "morada": morada,
        "tel": tel,
        "nif": nif,
        "compra": compra,
        "desconto": desconto,
        "divida": divida
    }

    clientes.append(cliente)

    print("Cliente inserido com sucesso.")
    num_cliente += 1


def listar_clientes():
    if not clientes:
        print("Não existem clientes.")
        return

    for c in clientes:
        print("\nNúmero:", c["num"])
        print("Nome:", c["nome"])
        print("Morada:", c["morada"])
        print("Telefone:", c["tel"])
        print("NIF:", c["nif"])
        print("Compra:", c["compra"])
        print("Desconto:", c["desconto"])
        print("Dívida Final:", c["divida"])

        input("Pressione ENTER para continuar...")


def buscar_cliente():
    try:
        num = int(input("Número do cliente: "))
    except:
        print("Número inválido.")
        return

    for c in clientes:
        if c["num"] == num:
            print("\nNúmero:", c["num"])
            print("Nome:", c["nome"])
            print("Morada:", c["morada"])
            print("Telefone:", c["tel"])
            print("NIF:", c["nif"])
            print("Compra:", c["compra"])
            print("Desconto:", c["desconto"])
            print("Dívida Final:", c["divida"])
            return

    print("Cliente não encontrado.")


def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Inserir Cliente")
        print("2 - Listar Clientes")
        print("3 - Buscar Cliente por Número")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            inserir_cliente()
        elif op == "2":
            listar_clientes()
        elif op == "3":
            buscar_cliente()
        elif op == "0":
            print("Programa terminado.")
            break
        else:
            print("Opção inválida.")


menu()
