servidor = {"status": "ok", "tempo_resposta": 350}

if servidor["status"] == "ok" and servidor["tempo_resposta"] > 200:
    print("Servidor lento")

elif servidor["status"] == "ok":
    print("Servidor ativo")

elif servidor["status"] == "erro":
    print("Servidor indisponível")

else:
    print("Estado desconhecido")