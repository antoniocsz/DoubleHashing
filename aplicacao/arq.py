#!/usr/bin/env python
# -*- coding: utf-8 -*

from struct import *
import os

def arquivoExiste(nomeArquivo):
    return os.path.exists(nomeArquivo)
