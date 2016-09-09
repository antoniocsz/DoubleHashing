#!/usr/bin/env python
# -*- coding: utf-8 -*

from arq import arquivoExiste

def main():
    nomeArquivo = "_arquivo.data"
    TAMANHO_ARQUIVO = 11

    if not arquivoExiste(nomeArquivo):
        print ('Ainda Não')
    else:
        print ('Já existe')

if __name__ == '__main__':
    main()
