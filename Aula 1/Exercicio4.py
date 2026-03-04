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