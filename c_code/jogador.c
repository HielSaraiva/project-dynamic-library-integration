#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void descreve_jogador(const char* nome) {
    const char* adjetivos[] = {
        "bagre",
        "ligeiro",
        "cabuloso",
        "letal",
        "encapetado",
        "matuto veloz",
        "bicho ruim",
        "canhoto do além",
        "motorzinho da bola",
        "tenebroso"
    };

    int total = sizeof(adjetivos) / sizeof(adjetivos[0]);

    srand((unsigned int)time(NULL));
    int indice = rand() % total;

    printf("O %s é %s.\n", nome, adjetivos[indice]);
}

