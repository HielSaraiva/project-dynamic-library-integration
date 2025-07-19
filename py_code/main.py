from cffi import FFI

ffi = FFI()

# Declaração da função em C
ffi.cdef("""
    void descreve_jogador(const char* nome);
""")

# Carrega a biblioteca dinâmica
lib = ffi.dlopen("./libjogador.dylib")

# Chama a função com um nome de jogador do Fortaleza
nome = "Lucero"
lib.descreve_jogador(nome.encode("utf-8"))
