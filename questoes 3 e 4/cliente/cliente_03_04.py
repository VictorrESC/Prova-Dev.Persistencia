import httpx

BASE_URL = "http://127.0.0.1:8000"

def adicionar_aluno(nome: str, nota: float):
    res = httpx.post(
        f"{BASE_URL}/alunos", 
        json={"nome": nome, "nota": nota})
    return res.json()

def obter_nota(nome: str):
    res = httpx.get(f"{BASE_URL}/alunos/{nome}")
    return res.json()

def listar_alunos():
    res = httpx.get(f"{BASE_URL}/alunos")
    return res.json()

if __name__ == "__main__":
    print(adicionar_aluno("Victor Emanuel", 9.0))
    print(adicionar_aluno("Jefferson Carvalho", 10.0))
    print(adicionar_aluno("Gustavo Gurgel", 2.5))
    print(obter_nota("Victor Emanuel"))
    print(obter_nota("Gustavo Gurgel"))
    print(adicionar_aluno("Gustavo Gurgel", 10.0))
    print(listar_alunos())