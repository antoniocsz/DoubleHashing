#!/usr/bin/env python
# -*- coding: utf-8 -*

import arq
import os


def doubleHashing(chave, i, tamanho):
    '''Calcula o DoubleHashing, usando a definição: h(c,i) = [h1(c)+i*h2(c)] mod m'''
    h1 = chave % tamanho
    h2 = chave // tamanho
    if h2 is 0:
        h2 = 1
    return ((h1 + i * h2) % tamanho)


def insere_registro(namefile, tamanho):
    chave = int(input())
    nome = input()
    idade = int(input())

    tentativas = 0
    return doubleHashing(chave, tentativas, tamanho)

def main():
    '''Função principal.'''
    TAMANHO_ARQUIVO = 11
    namefile = '_arquivo.dat'

    opcao = input()

    if opcao is 'i':
        print (insere_registro(namefile, TAMANHO_ARQUIVO))
    elif opcao is 'c':
        pass
    elif opcao is 'r':
        pass
    elif opcao is 'p':
        pass
    elif opcao is 'm':
        pass
    elif opcao is 'e':
        exit()


if __name__ == '__main__':
    main()
