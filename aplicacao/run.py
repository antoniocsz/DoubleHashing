#!/usr/bin/env python
# -*- coding: utf-8 -*

import arq
import os


def main():
    TAMANHO_ARQUIVO = 11
    namefile = '_arquivo.dat'

    if arq.gravar_arquivo(namefile, TAMANHO_ARQUIVO):
        print ('Ocorreu tudo bem')
    else:
        print ('Deu merda')

if __name__ == '__main__':
    main()
