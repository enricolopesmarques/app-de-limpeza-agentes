from datetime import datetime
import os

def salvar_reuniao(nome_arquivo: str, conteudo, titulo: str = None, feedback_ceo: str = None):
    os.makedirs('historico', exist_ok=True)

    if not isinstance(conteudo, str):
        conteudo = str(conteudo)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    caminho_arquivo = os.path.join('historico', f'{nome_arquivo}_{timestamp}.txt')

    if not titulo:
        titulo = nome_arquivo.replace('_', ' ').title()

    cabecalho = (
        f"{'=' * 80}\n"
        f"📅 Reunião: {titulo}\n"
        f"🕒 Data e Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        f"{'=' * 80}\n\n"
    )

    if feedback_ceo:
        cabecalho += (
            f"💬 Feedback do CEO:\n"
            f"{'-' * 80}\n"
            f"{feedback_ceo}\n"
            f"{'-' * 80}\n\n"
        )

    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        f.write(cabecalho + conteudo)

    print(f"✅ Reunião salva em: {caminho_arquivo}")
