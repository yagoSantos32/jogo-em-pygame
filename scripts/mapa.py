from config import *
class Mapa(pygame.sprite.Sprite):
    def __init__(self,posicao,surface,grupo):
        super().__init__(grupo)
        self.image=surface
        self.rect=self.image.get_rect(topleft=(posicao))

class objColisao(Mapa):
    def __init__(self,posicao,surface,grupo):
        super().__init__(posicao,surface,grupo)
    
class MapaGround(Mapa):
    def __init__(self,posicao,surface,grupo):
        super().__init__(posicao,surface,grupo)


    


