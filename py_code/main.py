import ctypes
import os
import sys

# Carrega a biblioteca dinâmica
lib_path = os.path.join("..", "c_code", "libjogador.dylib")
lib = ctypes.CDLL(lib_path)

# Configura a função descreve_jogador
lib.descreve_jogador.argtypes = [ctypes.c_char_p]
lib.descreve_jogador.restype = None

nome = "Lucero"
nome_bytes = nome.encode('utf-8')
lib.descreve_jogador(nome_bytes)
