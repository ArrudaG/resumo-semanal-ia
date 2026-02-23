import smtplib
import logging
import markdown
import os
import json

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.config.settings import EMAIL_USER, EMAIL_PASSWORD

def enviar_email(assunto, mensagem):
    if not EMAIL_USER or not EMAIL_PASSWORD:
        raise ValueError("Credenciais de email não carregadas")

    try:
        html_content = markdown.markdown(mensagem)

        emails = json.loads(os.environ["REPORT_EMAILS"])

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_USER, EMAIL_PASSWORD)

            for email in emails:
                msg = MIMEMultipart("alternative")
                msg["Subject"] = assunto
                msg["From"] = EMAIL_USER
                msg["To"] = email

                part_text = MIMEText(mensagem, "plain", "utf-8")
                part_html = MIMEText(html_content, "html", "utf-8")

                msg.attach(part_text)
                msg.attach(part_html)

                server.sendmail(
                    EMAIL_USER,
                    email,
                    msg.as_string()
                )
                logging.info(f"Email enviado para {email}")

    except Exception as erro:
        print("ERRO SMTP:", erro)
        logging.error(f"Erro ao enviar o email: {erro}")