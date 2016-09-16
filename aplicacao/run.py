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
                reg = arq.retorna_registro(namefile, tamanho, posicaoSort)
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


def remover(namefile, tamanho):
    ''' Remove o registro do arquivo. '''
    chave = int(input())

    if arq.arquivoExiste(namefile):
        tentativas = 0
        while tentativas < tamanho:
            posicao = doubleHashing(chave, tentativas, tamanho)
            registro = arq.consultar_registro(namefile, tamanho, posicao, chave)
            if registro != None:
                arq.remover_registro(namefile, posicao)
                break
            else:
                tentativas += 1
        if tentativas is tamanho:
            print ('chave não encontrada: %d' % chave)


def imprime(namefile, tamanho):
    ''' Imprime a tabela toda. '''
    if arq.arquivoExiste(namefile):
        for posicao in range(tamanho):
            registro = arq.retorna_registro(namefile, tamanho, posicao)
            if registro[0] is -1:
                print('%d: vazio' % posicao)
            else:
                print('%d: %d %s %d' % (posicao, registro[0], registro[1].decode('utf-8'), registro[2]))


def media(namefile, tamanho):
    ''' Calcula a média de acesso dos registros no arquivo. '''
    media = 0
    quantidade = 0

    if arq.arquivoExiste(namefile):
        for posicaoA in range(tamanho):
            registro = arq.retorna_registro(namefile, tamanho, posicaoA)
            if registro[0] is not -1:
                quantidade += 1
                for posicaoB in range(tamanho):
                    tentativa = doubleHashing(registro[0], posicaoB, tamanho)
                    if arq.buscar_chave(namefile, tamanho, tentativa, registro[0]):
                        media += posicaoB+1
                        break

    print ('%.1f' % (media / quantidade))



def main(namefile, tamanho):
    ''' Programa principal. '''

    while True:
        opcao = input()
        if opcao is 'i':
            inserir(namefile, tamanho)
        elif opcao is 'c':
            consultar(namefile, tamanho)
        elif opcao is 'r':
            remover(namefile, tamanho)
        elif opcao is 'p':
            imprime(namefile, tamanho)
        elif opcao is 'm':
            media(namefile, tamanho)
        elif opcao is 'e':
            break


if __name__ == '__main__':
    TAMANHO_ARQUIVO = 11
    ARQUIVO = 'arquivo.dat'
    main(ARQUIVO, TAMANHO_ARQUIVO)
