# -*- encoding: utf-8 -*-
from struct import *
import os


# Funções Auxiliares
def arquivoExiste(namefile):
    ''' Verifica se o arquivo existe e retorna um valor booleano'''
    return  os.path.exists(namefile)


def compactar(chave=-1, nome="vazio", idade=0):
    ''' Retorna uma struct'''
    return pack("i20sic", chave, nome.encode('utf-8'), idade, '\n'.encode('utf-8'))


def descompactar(registro):
    ''' Retorna um registro com: chave, nome e idade.'''
    return unpack("i20sic", registro)


def escrever_arquivo(namefile, opcao, registro, posicao):
    '''Abre o arquivo e escreve o registro na posição fornecida.'''
    with open(namefile, opcao) as arquivo:
        arquivo.seek(posicao, 0)
        arquivo.write(registro)


def tamanho_registro(namefile, TAM):
    ''' Retorna o tamanho de cada registro. '''
    with open(namefile, 'rb') as arquivo:
        arquivo.seek(0, 2)
        conteudo = arquivo.tell()
        tamanho = conteudo // TAM
    return tamanho


def retorna_registro(namefile, TAM , posicao):
    ''' Retorna o registro, com base na posição fornecida. '''
    tamanho = tamanho_registro(namefile, TAM)
    if arquivoExiste(namefile):
        with open(namefile, 'rb') as arquivo:
            arquivo.seek(posicao*tamanho, 0)
            conteudo = arquivo.read(tamanho)
            registro = descompactar(conteudo)
    return registro


# Funções Principais
def gravar_registro(namefile, TAM, registro, posicao):
    ''' Insere o registro no arquivo e/ou inicia um arquivo.'''
    if arquivoExiste(namefile):
        escrever_arquivo(namefile, "r+b", registro, posicao)
    return True


def buscar_chave(namefile, TAM , posicao, chave):
    ''' Verifica se a chave já existe no arquivo. '''
    if arquivoExiste(namefile):
        registro = retorna_registro(namefile, TAM, posicao)
        if chave is int(registro[0]):
            return True
    return False


def consultar_registro(namefile, TAM , posicao, chave):
    ''' Verifica se a chave já existe no arquivo. '''
    if arquivoExiste(namefile):
        registro = retorna_registro(namefile, TAM, posicao)
        if chave is int(registro[0]):
            return registro
    return None


def remover_registro(namefile, posicao):
    '''Reescreve o registro na posição, passando um registro vazio.'''
    escrever_arquivo(namefile, "r+b", compactar(), posicao*len(compactar()))
