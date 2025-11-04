import pandas as pd

receitas = pd.Series([12000, 17500, 14300, 16000, 19500], index=["Luca Brasi", "Peter Clemenza", "Sal Tessio", "Ton Hagen", "Michael Corleone"])

total_semanal = receitas.sum()
print(f"\nTotal arrecadado na semana: US$ {total_semanal:.2f}\n")

media_receitas = receitas.mean()
print(f"Média das receitas: US$ {media_receitas:.2f}\n")

associado_maior_receita = receitas.idxmax()
print(f"Associado que mais arrecadou: {associado_maior_receita}\n")

associados_acima_media = receitas[receitas > media_receitas]
print("Associados que arrecadaram acima da média:\n")
print(associados_acima_media)