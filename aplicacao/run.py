#!/usr/bin/env python
# -*- coding: utf-8 -*

import arq

def doubleHashing(chave, tentativas, tamanho):
    ''' Função Hashing. '''
    h1 = chave % tamanho
    h2 = chave // tamanho
    if h2 is 0:
        h2 = 1
    return ((h1 + tentativas * h2) % tamanho)


def inserir(namefile, tamanho):
    ''' Função que insere no arquivo. '''

    chave = int(input())
    nome = input()
    idade =  int(input())

    registro = arq.compactar(chave, nome, idade)
    tentativas = 0

    if not arq.arquivoExiste(namefile):
        posicao = doubleHashing(chave, tentativas, tamanho) * len(registro)
        arq.gravar_registro(namefile, tamanho, registro, posicao)
    else:
        while tentativas < tamanho:
            posicaoSort = doubleHashing(chave, tentativas, tamanho)
            posicaoInsert = posicaoSort * len(registro)
            if arq.buscar_chave(namefile, tamanho, posicaoSort, chave):
                print ('chave já existente %d' % chave)
                break
            else:
                reg = arq.retorna_registro(namefile, tamanho, posicaoSort, chave)
                if reg[0] is -1:
                    arq.gravar_registro(namefile, tamanho, registro, posicaoInsert)
                    break
                else:
                    tentativas += 1


def consultar(namefile, tamanho):
    ''' Função que consulta uma chave no arquivo'''
    chave = int(input())

    if arq.arquivoExiste(namefile):
        tentativas = 0
        while tentativas < tamanho:
            posicao = doubleHashing(chave, tentativas, tamanho)
            registro = arq.consultar_registro(namefile, tamanho, posicao, chave)
            if registro != None:
                print ('chave: %d\n%s\n%d' %(registro[0], registro[1].decode('utf-8'), registro[2]))
                break
            else:
                tentativas += 1
        if tentativas is tamanho:
            print ('chave não encontrada: %d' % chave)


def main(namefile, tamanho):
    ''' Programa principal. '''
    opcao = input()

    if opcao is 'i':
        inserir(namefile, tamanho)
    elif opcao is 'c':
        consultar(namefile, tamanho)
    elif opcao is 'r':
        chave = int(input())
        posicao = doubleHashing(chave, 0, tamanho)
        if arq.remover_registro(namefile, posicao):
            print ('Deletado com sucesso')


if __name__ == '__main__':
    TAMANHO_ARQUIVO = 11
    ARQUIVO = 'arquivo.dat'
    main(ARQUIVO, TAMANHO_ARQUIVO)
