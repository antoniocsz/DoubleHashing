#!/usr/bin/env python
# -*- coding: utf-8 -*


from struct import *
import pickle
import run as func
import os


# Funções auxiliadoras
def isFile(namefile):
    ''' Verifica se o arquivo existe e retorna um valor booleano'''
    return  os.path.exists(namefile)


def escrever_arquivo(namefile, opcao, registro, posicao):
    '''Abre o arquivo e escreve o registro na posição fornecida.'''
    with open(namefile, opcao) as arquivo:
        arquivo.seek(posicao, 0)
        arquivo.write(registro)


def compacta(chave=0, nome="vazio".encode('utf-8'), idade=0):
    ''' Retorna uma struct formatada: chave, nome e idade.'''
    return pack("i20sic", chave, nome, idade, '\n'.encode('utf-8'))


# Funçoes Principais
def gravar_registro(namefile, TAM, registro=0, posicao=0):
    ''' Insere o registro no arquivo e/ou inicia um arquivo.'''
    if isFile(namefile):
        escrever_arquivo(namefile, "r+b", registro, posicao)
    else:
        for i in range(TAM):
            if i != 0:
                escrever_arquivo(namefile, "r+b", compacta(), i*len(reg))
            else:
                escrever_arquivo(namefile, "wb", compacta(), i*len(reg))
        escrever_arquivo(namefile, "r+b", compacta(), posicao)
    return True


def consultar_registro(namefile, chave, posicao, registro, TAM):
    with open(namefile,"rb") as arquivo:
        arquivo.seek(0,2)
        conteudo = arquivo.tell()
        tamanho = conteudo / TAM
    if isFile(namefile):
        with open(namefile, 'rb') as arquivo:
            arquivo.seek(position*(tamanho), 0)
            conteudo = arquivo.read(tamanho)
            registro = unpack("i20sic",conteudo)
            if chave == int(registro[0]):
                print (registro[1]).decode('utf-8'), "\n", int(registro[2]) #print valido
    return None


def remover_registro(namefile, posicao):
    '''Reescreve o registro da posição, passando um registro vazio.'''
    escrever_arquivo(namefile, "r+b", compacta(), posicao)
