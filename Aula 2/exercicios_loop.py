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