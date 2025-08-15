from config import *

class Animal(pygame.sprite.Sprite):
    def __init__(self, nome, animalPos, tempoReducao,grupo):
        super().__init__(grupo)
        self.nome = nome
        self.animalPos = animalPos
        self.originalImg = None  
        self.originalRect = None  
        self.___energia=100
        self.tempoReducao = tempoReducao 
        self.ultimoTempoReducao = pygame.time.get_ticks()  

    
    def alimentar(self,tela):
        if self.originalImg == None:
            self.originalImg = self.image
            self.originalRect = self.rect
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect(midbottom=(tela_x - 250, 300))

        x=self.rect.x
        y=self.rect.y+20
       
        rectLife=pygame.Rect(x,y,(self.___energia*2),30)
        rect=pygame.Rect(x,y,200,30)
    
        pygame.draw.rect(tela,"blue",rectLife,0,4)
        pygame.draw.rect(tela,"black",rect,4,4)

    
    def restaurar(self):

        if self.originalImg:
            self.image = self.originalImg
            self.rect = self.originalRect
            self.originalImg = None
            self.originalRect = None

    def reduzirEnergia(self):
        tempoAtual = pygame.time.get_ticks()
        if tempoAtual - self.ultimoTempoReducao >= self.tempoReducao:
           
            self.mudarEnergia(self.pegarEnergia() - 5)
            self.ultimoTempoReducao = tempoAtual
           
    def pegarEnergia(self):
        return self.___energia
    def mudarEnergia(self, valor):
        self.___energia = max(0, min(valor, 100)) 
        

class Vaca(Animal):
    def __init__(self, nome, animalPos, tempoReducao,grupo):
        super().__init__(nome, animalPos, tempoReducao,grupo)
        self.image = pygame.image.load(join('imagens','animais', 'vaca.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=animalPos)

class Galinha(Animal):
    def __init__(self, nome, animalPos, tempoReducao,grupo):
        super().__init__(nome, animalPos, tempoReducao,grupo)
        self.image = pygame.image.load(join('imagens','animais', 'galinha.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=animalPos)
class Porco(Animal):
    def __init__(self, nome, animalPos, tempoReducao,grupo):
        super().__init__(nome, animalPos,tempoReducao, grupo)
        self.image = pygame.image.load(join('imagens','animais', 'porco.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=animalPos)
class Ovelha(Animal):
    def __init__(self, nome, animalPos, tempoReducao,grupo):
        super().__init__(nome, animalPos, tempoReducao,grupo)
        self.image = pygame.image.load(join('imagens','animais', 'ovelha.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=animalPos)