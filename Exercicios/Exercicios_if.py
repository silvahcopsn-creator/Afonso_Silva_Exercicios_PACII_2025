# Afonso Silva Exercicios PAC- 2025140271

#--------------------------------------------s

#Exercicio 1

total = int(input("Segundos: "))

horas = total // 3600
minutos = (total % 3600) // 60
segundos = total % 60

print(f"{horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)")


#Exercicio 2

num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
num3 = int(input("Num3: "))

print("Maior:", max(num1, num2, num3))
print("Menor:", min(num1, num2, num3))

#Exercicio 3

num1 = int(input("Num1: "))
num2 = int(input("Num2: "))

if num1 > num2:
    print("Crescente:", num2, num1)
    print("Decrescente:", num1, num2)
else:
    print("Crescente:", num1, num2)
    print("Decrescente:", num2, num1)

#Exercicio 4

saldo = float(input("Saldo: "))
cheque = float(input("Cheque: "))

if cheque <= saldo:
    saldo -= cheque
    print("Cheque descontado, saldo:", saldo)
else:
    print("Cheque não pode ser descontado")

#Exercicio 5

nums = []

for i in range(3):
    nums.append(int(input(f"Número {i+1}: ")))

nums.sort()

print("Crescente:", nums)
print("Decrescente:", nums[::-1])

#Exercicio 6

nome = input("Nome: ")
compra = float(input("Valor da compra: "))

if compra <= 200:
    desconto = compra * 0.10
elif compra <= 500:
    desconto = compra * 0.15
else:
    desconto = compra * 0.20

total = compra - desconto

print("Nome:", nome)
print("Compra:", compra)
print("Desconto:", desconto)
print("Total a pagar:", total)

#Exercicio 7

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

media = (n1*2 + n2*3 + n3*5) / 10

print("Média:", media)

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")

#Exercicio 8

notas = []
soma = 0

for i in range(10):
    nota = float(input(f"Nota {i+1}: "))
    notas.append(nota)
    soma += nota

media = soma / 10

acima_media = 0
for n in notas:
    if n >= media:
        acima_media += 1

print("Média:", media)
print("Alunos acima ou igual à média:", acima_media)

#Exercicio Switch

mes = int(input("Número do mês: "))

match mes:
    case 1: print("Janeiro")
    case 2: print("Fevereiro")
    case 3: print("Março")
    case 4: print("Abril")
    case 5: print("Maio")
    case 6: print("Junho")
    case 7: print("Julho")
    case 8: print("Agosto")
    case 9: print("Setembro")
    case 10: print("Outubro")
    case 11: print("Novembro")
    case 12: print("Dezembro")
    case _: print("Número inválido")

#Exercicio loop

pares = 0
impares = 0

for i in range(10):
    num = int(input("Número: "))
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Pares:", pares)
print("Ímpares:", impares)  
