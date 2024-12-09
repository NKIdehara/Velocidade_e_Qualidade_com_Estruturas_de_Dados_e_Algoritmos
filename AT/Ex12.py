import os

def listar_arquivos(diretorio):
    for arq in os.listdir(diretorio):
        caminho = os.path.join(diretorio, arq)
        if os.path.isdir(caminho):
            listar_arquivos(caminho)
        else:
            print(caminho)

listar_arquivos("C:\python312\doc")