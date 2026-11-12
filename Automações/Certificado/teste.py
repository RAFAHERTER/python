import os
"""from docx import Document


caminho_atual = os.path.dirname(__file__)
caminho_certificado = os.path.join(caminho_atual, "modelo_certificado.docx")

doc = Document(caminho_certificado)
for p in doc.paragraphs:
    #print(repr(p.text))
    for r in p.runs:
        novo_texto = r.text.replace("[ NOME COMPLETO ]", "RAFAEL HERTER DE JESUS")
        r.text = novo_texto
        print("    run:", novo_texto)
doc.save(os.path.join(caminho_atual, "teste_saida.docx"))   
"""

print(os.path.dirname(__file__))
print(__file__)