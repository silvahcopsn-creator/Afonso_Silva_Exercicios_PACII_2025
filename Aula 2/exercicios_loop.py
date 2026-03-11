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

for i in range (10):

    numero = 
