#!/usr/bin/env python
# -*- coding: utf-8 -*


from struct import *
import run as func
import os


''' Funções auxiliadoras '''
def isFile(namefile):
     ''' Verifica se o arquivo existe e retorna um valor booleano'''
    return  os.path.exists(namefile)


def escrever_arquivo(namefile, opcao, registro, posicao):
    ''' Escreve no arquivo. '''
    with open(namefile, opcao) as arquivo:
        arquivo.seek(posicao, 0)
        arquivo.write(registro)


''' Funçoes Principais'''
def gravar_arquivo(namefile, TAM, registro=0, posicao=0):
    ''' Insere o registro no arquivo e/ou inicia um arquivo.'''
    if isFile(namefile):
        escrever_arquivo(namefile, "r+b", registro, posicao)
    else:
        for i in range(TAM):
            reg = pack("i20sic", 0, "vazio".encode('utf-8'), 0, '\n'.encode('utf-8'))
            if i != 0:
                escrever_arquivo(namefile, "r+b", reg, i*len(reg))
            else:
                escrever_arquivo(namefile, "wb", reg, i*len(reg))
        escrever_arquivo(namefile, "r+b", reg, posicao)
    return True
