#!/usr/bin/env python
# -*- coding: utf-8 -*


from struct import *
import os


# Funções Auxiliares
def arquivoExiste(namefile):
    ''' Verifica se o arquivo existe e retorna um valor booleano'''
    return  os.path.exists(namefile)


def compactar(chave=0, nome="vazio", idade=0):
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


def consultar_registro(namefile, TAM , posicao, chave):
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

# def consultar_registro(namefile, chave, posicao, registro, TAM):
#     with open(namefile,"rb") as arquivo:
#         arquivo.seek(0,2)
#         conteudo = arquivo.tell()
#         tamanho = conteudo / TAM
#     if arquivoExiste(namefile):
#         with open(namefile, 'rb') as arquivo:
#             arquivo.seek(position*(tamanho), 0)
#             conteudo = arquivo.read(tamanho)
#             registro = unpack("i20sic",conteudo)
#             if chave == int(registro[0]):
#                 print (registro[1]).decode('utf-8'), "\n", int(registro[2]) #print valido
#     return None
#
#
# def consulta2(namefile, chave, position, registro, TAM):
#     string = ""
#     arq = open(namefile,"rb")
#     arq.seek(0,2)
#     conteudo = arq.tell()
#     tam = conteudo/TAM
#     arq.close()
#     if isFile(namefile):
#         arq = open(namefile, 'rb')
#         arq.seek(position*(tam), 0)
#         conteudo = arq.read(tam)
#         registro = unpack("f20sffc",conteudo)
#         if chave == int(registro[0]):
#             string = str(int(registro[0]))+" "+(registro[1])+" "+str(int(registro[2]))
#     arq.close()
#     return string
#
#
# def remover_registro(namefile, posicao):
#     '''Reescreve o registro da posição, passando um registro vazio.'''
#     escrever_arquivo(namefile, "r+b", compactar(), posicao)
#
