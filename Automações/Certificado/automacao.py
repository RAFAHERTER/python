import os, csv, sys
from docx import Document

caminho_atual = os.path.dirname(__file__) #Caminho do arquivo atual
planilha = 'certificados_alunos.csv'
caminho_planilha = os.path.join(caminho_atual, planilha) #Caminho completo do arquivo CSV
caminho_certificado = os.path.join(caminho_atual, "modelo_certificado.docx") #Caminho completo do arquivo DOCX

try:
    with open(caminho_planilha, 'r', encoding='utf-8-sig', newline='') as arquivo_csv: #Abre o arquivo CSV 
        leitor_csv = csv.DictReader(arquivo_csv, delimiter=';') #Faz a leitura do arquivo CSV, considerando o delimitador ";" e em formato de dicionário. (Sem o delimitador, o Python considera o padrão de vírgula)

        for indice, linha in enumerate(leitor_csv): #"linha" é um dicionário que contém os dados de cada linha do CSV, onde as chaves são os nomes das colunas e os valores são os dados correspondentes. "indice" é o número da linha atual (começando do 0).

            doc = Document(caminho_certificado) #Cria um novo documento a partir do modelo
            for p in doc.paragraphs: #Itera sobre todos os parágrafos do documento

                for r in p.runs: #Itera sobre todos os runs (trechos de texto) dentro de cada parágrafo

                    for chave, valor in linha.items(): #Itera sobre as chaves e valores do dicionário "linha"
                        marcador = f"[ {chave} ]"
                        novo_texto = r.text.replace(marcador, valor) #Substitui o marcador pelo valor correspondente do CSV
                        r.text = novo_texto # Atualiza o texto do run com o novo texto

            #Cria a pasta "Todos_os_certificados" caso não exista e salva o certificado com o nome do aluno e do curso
            os.makedirs(os.path.join(caminho_atual, 'Todos_os_certificados'), exist_ok=True)

            #Cria o caminho completo para salvar o certificado na pasta "Todos_os_certificados"
            caminho_pasta = os.path.join(caminho_atual, 'Todos_os_certificados', f'certificado-{linha["NOME COMPLETO"]}-{linha["NOME DO CURSO FORMADO"]}.docx')
            doc.save(caminho_pasta)

except FileNotFoundError:
    print(f'Arquivo "{planilha}" não encontrado.')
    sys.exit() #Interrompe o código caso o arquivo CSV não seja encontrado
