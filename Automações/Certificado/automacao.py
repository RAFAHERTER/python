import os, csv, sys
from docx import Document

caminho_atual = os.path.dirname(__file__)
planilha = 'certificados_alunos.csv'
caminho_planilha = os.path.join(caminho_atual, planilha)
caminho_certificado = os.path.join(caminho_atual, "modelo_certificado.docx")

alunos = []
cont = 0
try:
    with open(caminho_planilha, 'r', encoding='utf-8-sig', newline='') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv, delimiter=';')
        print(leitor_csv.fieldnames)
        for indice, linha in enumerate(leitor_csv):
            alunos.append(linha)
            cont += 1
            doc = Document(caminho_certificado)
            for p in doc.paragraphs:
                for r in p.runs:
                    novo_texto = r.text.replace(f"[ NOME COMPLETO ]", linha["NOME COMPLETO"])
                    r.text = novo_texto
                    print("    run:", novo_texto)
            doc.save(os.path.join(caminho_atual, f'certificado-{linha["NOME COMPLETO"]}.docx'))  
            if cont == 1:
                break
except FileNotFoundError:
    print(f'Arquivo "{planilha}" não encontrado.')
    sys.exit()

