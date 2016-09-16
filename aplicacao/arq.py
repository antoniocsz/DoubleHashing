#!/usr/bin/env python
# -*- coding: utf-8 -*


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


# Funções Principais
def gravar_registro(namefile, TAM, registro, posicao):
    ''' Insere o registro no arquivo e/ou inicia um arquivo.'''
    if arquivoExiste(namefile):
        escrever_arquivo(namefile, "r+b", registro, posicao)
    else:
        for i in range(TAM):
            reg = compactar()
            pos = i * len(reg)
            if i != 0:
                escrever_arquivo(namefile, "r+b", reg, pos)
            else:
                escrever_arquivo(namefile, "wb", reg, pos)
        escrever_arquivo(namefile, "r+b", registro, posicao)
    return True


def buscar_chave(namefile, TAM , posicao, chave):
    ''' Verifica se a chave já existe no arquivo. '''
    with open(namefile, 'rb') as arquivo:
        arquivo.seek(0, 2)
        conteudo = arquivo.tell()
        tamanho = conteudo // TAM
    if arquivoExiste(namefile):
        with open(namefile, 'rb') as arquivo:
            arquivo.seek(posicao*tamanho, 0)
            conteudo = arquivo.read(tamanho)
            registro = descompactar(conteudo)
            if chave is int(registro[0]):
                return True
    return False


def retorna_registro(namefile, TAM , posicao, chave):
    ''' Verifica se a chave já existe no arquivo. '''
    with open(namefile, 'rb') as arquivo:
        arquivo.seek(0, 2)
        conteudo = arquivo.tell()
        tamanho = conteudo // TAM
    if arquivoExiste(namefile):
        with open(namefile, 'rb') as arquivo:
            arquivo.seek(posicao*tamanho, 0)
            conteudo = arquivo.read(tamanho)
            registro = descompactar(conteudo)
    return registro


def consultar_registro(namefile, TAM , posicao, chave):
    ''' Verifica se a chave já existe no arquivo. '''
    with open(namefile, 'rb') as arquivo:
        arquivo.seek(0, 2)
        conteudo = arquivo.tell()
        tamanho = conteudo // TAM
    if arquivoExiste(namefile):
        with open(namefile, 'rb') as arquivo:
            arquivo.seek(posicao*tamanho, 0)
            conteudo = arquivo.read(tamanho)
            registro = descompactar(conteudo)
            if chave is int(registro[0]):
                return registro
    return None


def remover_registro(namefile, posicao):
    '''Reescreve o registro da posição, passando um registro vazio.'''
    escrever_arquivo(namefile, "r+b", compactar(), posicao*len(compactar()))
