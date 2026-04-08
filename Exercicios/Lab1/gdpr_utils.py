import re

def detectar_dados(mensagem):
    dados = []

    if re.search(r"\S+@\S+\.\S+", mensagem):
        dados.append("email")

    if re.search(r"\d{9}", mensagem):
        dados.append("telefone")

    if re.search(r"\d+\.\d+\.\d+\.\d+", mensagem):
        dados.append("ip")

    return dados