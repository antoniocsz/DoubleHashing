#!/usr/bin/env python
# -*- coding: utf-8 -*

from struct import *
import os

# Subfunções
def iniciaArquivo(nome_arquivo, parametro_abertura, posicao):
    ''' Inicializa o arquivo. '''
    with open(nome_arquivo, parametro_abertura) as arquivo:
        reg = pack("f20sffc",float(-1),"vazio".encode('utf-8'),-1.0,-1.0,'\n')
        arquivo.seek(posicao*len(reg), 0)
        arquivo.write(reg)


def escreverArquivo(nome_arquivo, registro, posicao):
    ''' Escreve no arquivo. '''
    with open(nome_arquivo, 'r+b') as arquivo:
        arquivo.seek(posicao, 0)
        arquivo.write(registro)


def arquivoExiste(nome_arquivo):
    ''' Verifica se o arquivo existe e retorna um valor booleano'''
    return os.path.exists(nome_arquivo)


# FunçõesPrincipais
def inserir(registro, nome_arquivo, posicao, TAMANHO):
    ''' Insere o registro no arquivo, inicializa o arquivo.'''
    if arquivoExiste(nome_arquivo):
        escreverArquivo(registro, nome_arquivo, posicao)
    else:
        for i in range(TAMANHO):
            if i != 0:
                iniciaArquivo(nome_arquivo, 'r+b', i)
            else:
                iniciaArquivo(nome_arquivo, 'wb', i)
        escreverArquivo(registro, nome_arquivo, posicao)
    return True


def consultar():
    pass


def deletar():
    pass
