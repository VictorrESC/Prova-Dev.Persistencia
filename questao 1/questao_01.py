with open("./questao 1/dados_alunos.txt", "r") as file:
    linha = file.readline()
    soma = 0
    contador = 0
    notas = []
    while linha:
        partes = linha.strip().split("#")
        nota = float(partes[2])
        notas.append(nota)
        soma += nota
        contador += 1
        linha = file.readline()
    if contador > 0:
        media = soma / contador
        print(f"Média das notas: {media:.2f}")
        maior_nota = max(notas)
        menor_nota = min(notas)
        print(f"Maior nota: {maior_nota}")
        print(f"Menor nota: {menor_nota}")
