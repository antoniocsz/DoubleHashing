#!/usr/bin/env python
# -*- coding: utf-8 -*

import arq
import os


def h1(TAM, chave):
    '''Retorna o resto da divisão da chave pelo tamanho.'''
    return (chave % TAM)


def h2(TAM, chave):
    ''' Retorna o quociente da divisão da chave pelo tamanho.'''
    return (chave // TAM)


def funcao_hashing(chave, tentativas, TAM):
    ''' Calcula o valor do double hashing. H(c, i) = [h1(c) + i * h2(c)] mod m.'''
    return h1(TAM, h1(TAM, chave) + tentativas * h2(TAM, chave))


def insertDoubleHashing(namefile, TAM, chave, nome, idade):
    tent = 0
    funcao_hash = funcao_hashing(chave, tent, TAM)
    pass

def main():
    TAMANHO_ARQUIVO = 11
    namefile = '_arquivo.dat'

    OPCAO = input()
    reg = 0
    if OPCAO == 'i':
        chave = int(input())
        nome = input()
        idade = int(input())

    if arq.gravar_arquivo(namefile, TAMANHO_ARQUIVO):
        print ('Ocorreu tudo bem')
    else:
        print ('Deu merda')

if __name__ == '__main__':
    main()
