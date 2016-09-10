#!/usr/bin/env python
# -*- coding: utf-8 -*

from struct import *
import run as func
import arrray
import os



# Subfunções
def iniciar(nome_arquivo, parametro_abertura, posicao):
    ''' Inicializa o arquivo. '''
    with open(nome_arquivo, parametro_abertura) as arquivo:
        reg = pack("f20sffc",float(-1),"vazio".encode('utf-8'),-1.0,-1.0,'\n')
        arquivo.seek(posicao*len(reg), 0)
        arquivo.write(reg)


def escrever(nome_arquivo, registro, posicao):
    ''' Escreve no arquivo. '''
    with open(nome_arquivo, 'r+b') as arquivo:
        arquivo.seek(posicao, 0)
        arquivo.write(registro)


def existe(nome_arquivo):
    ''' Verifica se o arquivo existe e retorna um valor booleano'''
    return os.path.exists(nome_arquivo)


# FunçõesPrincipais
def inserirRegistro(registro, nome_arquivo, posicao, TAMANHO):
    ''' Insere o registro no arquivo e/ou inicia um arquivo.'''
    if existe(nome_arquivo):
        escrever(registro, nome_arquivo, posicao)
    else:
        for i in range(TAMANHO):
            if i != 0:
                iniciar(nome_arquivo, 'r+b', i)
            else:
                iniciar(nome_arquivo, 'wb', i)
        escrever(registro, nome_arquivo, posicao)
    return True


def consultarRegistro():
    pass


def deletarRegistro():
    pass
