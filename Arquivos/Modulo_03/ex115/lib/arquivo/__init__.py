from ex115.lib.interface import *


def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('Houve ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def leiaArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('ERROR ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        arquivo.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        arquivo = open(arq, 'at')
    except:
        print('ERRO na abertura do arquivo!')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('ERRO ao escrever os dados.')
        else:
            print(f'Novo regitro de {nome} adicionado.')
            arquivo.close()

