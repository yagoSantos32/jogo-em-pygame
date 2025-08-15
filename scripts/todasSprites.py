from config import *
class todasSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.tela = pygame.display.get_surface()
        self.poscam = pygame.Vector2()

    def draw(self, playerPos):
      
        if playerPos[0] >= 2811:
            self.poscam.x = -(2811 - tela_x / 2)
        elif playerPos[0] <= 531:
            self.poscam.x = -(531 - tela_x / 2)
        else:
            self.poscam.x = -(playerPos[0] - tela_x / 2)

        if playerPos[1] >= 2833:
            self.poscam.y = -(2833 - tela_y / 2)
        elif playerPos[1] <= 380:
            self.poscam.y = -(380 - tela_y / 2)
        else:
            self.poscam.y = -(playerPos[1] - tela_y / 2)

        for sprite in self:
            self.tela.blit(sprite.image, sprite.rect.topleft + self.poscam)
