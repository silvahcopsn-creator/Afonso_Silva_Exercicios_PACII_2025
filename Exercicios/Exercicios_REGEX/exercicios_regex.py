# Afonso Silva Exercicios PAC- 2025140271


import json
import re

# Exercício 1: Ler JSON

with open("dados.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

# Exercício 2: Validar emails

regex_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'

def email_valido(email):
    return re.match(regex_email, email)


# Exercício 3: Extrair domínios

def extrair_dominio(url):
    dominio = re.sub(r'https?://(www\.)?', '', url)
    return dominio

print("Domínios:")
for pessoa in dados:
    print(extrair_dominio(pessoa["site"]))

# Exercício 4: Validar NIF

regex_nif = r'^[123568]\d{8}$'

def nif_valido(nif):
    return re.match(regex_nif, nif)

# Exercício 5

def telemovel_valido(tlm):
    numeros = re.sub(r'\D', '', tlm)  
    return len(numeros) == 9

validos = []

for pessoa in dados:
    if (email_valido(pessoa["email"]) and
        nif_valido(pessoa["nif"]) and
        telemovel_valido(pessoa["telemovel"])):
        
        validos.append(pessoa)

with open("validos.json", "w", encoding="utf-8") as f:
    json.dump(validos, f, indent=4, ensure_ascii=False)

# Exercício 6

with open("nomes_emails.txt", "w", encoding="utf-8") as f:
    for pessoa in validos:
        f.write(f"{pessoa['nome']} - {pessoa['email']}\n")