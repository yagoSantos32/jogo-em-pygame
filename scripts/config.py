import pygame
from pytmx.util_pygame import load_pygame
from random import randint
from os.path import join
from math import atan2,degrees
from os import walk

tela_x,tela_y=1024,700 

escala = 4  # 16x16 -> 64x64
tamanho_tile = 16 * escala  # 64

# --- Configurações de Nível e Inimigos ---
TEMPO_PARA_SUBIR_NIVEL = 30000  # 30 segundos em milissegundos
NIVEIS = {
    1: {'inimigos': 1, 'velocidade_inimigo': 200},
    2: {'inimigos': 3, 'velocidade_inimigo': 250},
    3: {'inimigos': 5, 'velocidade_inimigo': 300},
    4: {'inimigos': 7, 'velocidade_inimigo': 350},
    5: {'inimigos': 10, 'velocidade_inimigo': 400},
}
MAX_NIVEL = max(NIVEIS.keys())
VIDA_MAXIMA = 100
# -----------------------------------------
