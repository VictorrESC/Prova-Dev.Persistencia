from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

contador_id = 1
alunos_df = pd.DataFrame(columns=["id", "nome", "nota"])

class Aluno(BaseModel):
    nome: str
    nota: float

@app.post("/alunos")
def adicionar_aluno(aluno: Aluno):
    global contador_id, alunos_df

    aluno_existente = alunos_df[alunos_df['nome'] == aluno.nome]
    if not aluno_existente.empty:
        alunos_df.loc[aluno_existente.index, 'nota'] = aluno.nota
        return {
            "mensagem": "Nota atualizada com sucesso"
        }

    novo_aluno = {
        "id": contador_id,
        "nome": aluno.nome,
        "nota": aluno.nota
    }

    alunos_df = alunos_df._append(novo_aluno, ignore_index=True)

    contador_id += 1
    return {
        "mensagem": "Aluno adicionado com sucesso",
        "aluno": novo_aluno
    }

@app.get("/alunos/{nome}")
def obter_nota(nome: str):
    aluno = alunos_df[alunos_df['nome'] == nome]
    if aluno.empty:
        raise HTTPException(status_code=404, detail="Aluno não registrado")
    return aluno.to_dict(orient="records")[0]

@app.get("/alunos")
def listar_alunos():
    return alunos_df.to_dict(orient="records")