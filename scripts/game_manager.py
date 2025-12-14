from config import *
from inimigo import Inimigo
from random import randint

class GameManager:
    def __init__(self, todasSprites, player, animais, inimigos_sprites):
        self.todasSprites = todasSprites
        self.player = player
        self.animais = animais
        self.inimigos_sprites = inimigos_sprites

        self.nivel_atual = 1
        self.tempo_inicio_nivel = pygame.time.get_ticks()
        self.spawn_inimigos()

    def spawn_inimigos(self):
        # Remove todos os inimigos existentes
        for inimigo in self.inimigos_sprites:
            inimigo.kill()
        
        # Determina a quantidade e velocidade de inimigos para o nível atual
        config_nivel = NIVEIS.get(self.nivel_atual, NIVEIS[MAX_NIVEL])
        num_inimigos = config_nivel['inimigos']
        velocidade = config_nivel['velocidade_inimigo']

        # Gera novos inimigos
        for _ in range(num_inimigos):
            # Posição de spawn aleatória (ajustar conforme o mapa)
            spawn_x = randint(0, 4000) # Assumindo um mapa grande
            spawn_y = randint(0, 4000)
            novo_inimigo = Inimigo("mal", (spawn_x, spawn_y), (self.todasSprites, self.inimigos_sprites))
            novo_inimigo.set_speed(velocidade)

    def checar_progressao_nivel(self):
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.tempo_inicio_nivel >= TEMPO_PARA_SUBIR_NIVEL:
            if self.nivel_atual < MAX_NIVEL:
                self.nivel_atual += 1
                self.tempo_inicio_nivel = tempo_atual # Reinicia o contador de tempo
                
                # Restaura a vida do jogador e dos animais
                self.player.restaurarVidaCompleta()
                for animal in self.animais:
                    animal.restaurarVidaCompleta()

                # Gera novos inimigos com a nova configuração de nível
                self.spawn_inimigos()
                print(f"Nível subiu para: {self.nivel_atual}")

    def update(self, delta):
        # Lógica de progressão de nível
        self.checar_progressao_nivel()

        # Lógica de inimigos
        for inimigo in self.inimigos_sprites:
            inimigo.atacando() 
            inimigo.atacaPlayer(self.player, delta)

    def get_nivel_atual(self):
        return self.nivel_atual
