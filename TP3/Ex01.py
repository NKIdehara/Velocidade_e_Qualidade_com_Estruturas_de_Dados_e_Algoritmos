import os

def listar(pasta_inicial):
    for arquivo in os.listdir(pasta_inicial):
        caminho = pasta_inicial + "/" + arquivo
        if os.path.isdir(caminho):
            print(f"Pasta: {caminho}")
            listar(caminho)
        else:
            print(f"Arquivo: {caminho}")

pasta_inicial = "D:/dev"
listar(pasta_inicial)