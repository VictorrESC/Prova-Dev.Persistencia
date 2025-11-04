from bs4 import BeautifulSoup

with open("./questao 5/jogadas.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

tabela = soup.find("table")
linhas = tabela.find_all("tr")[1:]

vitorias_jgd1 = 0

for linha in linhas:
    colunas = linha.find_all("td")
    jogador1 = colunas[0].text.strip()
    jogador2 = colunas[1].text.strip()
    print(f"Jogador 1: {jogador1}, Jogador 2: {jogador2}")
    if (jogador1 == "Pedra" and jogador2 == "Tesoura") or \
       (jogador1 == "Papel" and jogador2 == "Pedra") or \
       (jogador1 == "Tesoura" and jogador2 == "Papel"):
        vitorias_jgd1 += 1

print(f"\nVitórias do Jogador 1: {vitorias_jgd1}")