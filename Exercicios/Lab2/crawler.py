import requests
from bs4 import BeautifulSoup
import time
import json
from urllib.parse import urljoin, urlparse
import urllib.robotparser

def permitido(url, user_agent="*"):
    rp = urllib.robotparser.RobotFileParser()
    base = urlparse(url)
    robots_url = f"{base.scheme}://{base.netloc}/robots.txt"
    
    rp.set_url(robots_url)
    
    try:
        rp.read()
        return rp.can_fetch(user_agent, url)
    except:
        return False

def crawler(url_inicial, max_paginas):
    visitados = set()
    por_visitar = [url_inicial]
    resultados = []

    while por_visitar and len(visitados) < max_paginas:
        url = por_visitar.pop(0)

        if url in visitados:
            continue

        if not permitido(url):
            print("Bloqueado pelo robots.txt:", url)
            continue

        try:
            headers = {"User-Agent": "MeuCrawlerEducacional"}
            resposta = requests.get(url, headers=headers)

            soup = BeautifulSoup(resposta.text, "html.parser")

            titulo = soup.title.string if soup.title else "Sem título"

            links = []
            for a in soup.find_all("a", href=True):
                link = urljoin(url, a["href"])
                links.append(link)

                if link not in visitados:
                    por_visitar.append(link)

            resultados.append({
                "url": url,
                "titulo": titulo,
                "links": links
            })

            visitados.add(url)

            print("Visitado:", url)

            time.sleep(1)  # delay

        except:
            print("Erro ao aceder:", url)

    with open("resultados.json", "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=4, ensure_ascii=False)

    print("Dados guardados em resultados.json")