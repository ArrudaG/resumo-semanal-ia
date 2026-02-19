from datetime import datetime
from services.email_service import enviar_email
from services.reports_service import salvar_report
from services.news_service import busca_financeiro
from services.ia_service import gerar_resumo

def main():
    try:
        noticia = busca_financeiro()
        if noticia:
            resumo = gerar_resumo(noticia)
            salvar_report(resumo)
            enviar_email(f"Resumo diário: {datetime.now():%d/%m/%Y}", f"{resumo}")
        else:
            print("Nenhuma notícia encontrada")
    except Exception as e:
        print("Erro:",e)

if __name__ == "__main__":
    main()