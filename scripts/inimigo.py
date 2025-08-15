from config import *

class Inimigo(pygame.sprite.Sprite):
    
    def __init__(self, nome, inimigoPos, grupos):
        super().__init__(grupos)
        self.image = pygame.image.load(join('imagens','inimigo', 'inimigo.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(topleft=inimigoPos).inflate(-70,-70)
        self.Inimigospeed = 200
        self.ataca = False
        self.atacaTime = pygame.time.get_ticks() + 500  
        self.inicio = inimigoPos
        


    def atacando(self):
        if not self.ataca and pygame.time.get_ticks() >= self.atacaTime:
            self.ataca = True
            
            self.rect.center = (randint(0, 1280), randint(0, 720))
           
    def atacaPlayer(self, player, delta):
        if self.ataca:
            direcao = pygame.math.Vector2(player.rect.center) - pygame.math.Vector2(self.rect.center)
            if direcao.length() > 0:
                direcao = direcao.normalize()
            self.rect.center += direcao * self.Inimigospeed * delta 
            if self.rect.colliderect(player.rect):
                player.mudarEnergia(player.pegarEnergia() - 20)
                self.estacaZero()
            
   
    def estacaZero(self):
        self.rect.center = self.inicio

    def morrer(self):
        self.estacaZero()
        