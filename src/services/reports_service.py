from datetime import datetime
from pathlib import Path

def salvar_report(conteudo):
    agora = datetime.now()
    ano = agora.strftime("%Y")
    mes = agora.strftime("%m")
    data = agora.strftime("%Y-%m-%d")

    repo_root = Path(__file__).parent.parent.parent
    pasta = repo_root ("reports") / ano / mes
    print(f"Criando pasta: {pasta}")
    pasta.mkdir(parents=True, exist_ok=True)

    arquivo = pasta / f"{data}.md"

    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(f"# Relatório Diário - {data}\n\n")
        f.write(conteudo)

    return arquivo
