#!/usr/bin/env python
# -*- coding: utf-8 -*

import arq

def doubleHashing(chave, tentativas, tamanho):
    ''' Função Hashing. '''
    h1 = chave % tamanho
    h2 = chave // tamanho
    if h2 is 0:
        h2 = 1
    return ((h1 + tentativas * h2) % tamanho), tentativas+1


def main(namefile, tamanho):
    ''' Programa principal. '''
    opcao = input()

    if opcao is 'i':
        # recebe os valores do registro
        chave = int(input())
        nome = input()
        idade =  int(input())
        registro = arq.compactar(chave, nome, idade)
        posicao = doubleHashing(chave, 0, tamanho) * len(registro)
        arq.gravar_registro(namefile, tamanho, registro, posicao)


if __name__ == '__main__':
    TAMANHO_ARQUIVO = 11
    ARQUIVO = 'arquivo.dat'
    main(ARQUIVO, TAMANHO_ARQUIVO)
