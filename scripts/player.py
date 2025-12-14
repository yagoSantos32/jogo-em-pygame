from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self,playerPosicao,colisoes,grupo):
        super().__init__(grupo)
        self.load_imagens()
        self.state, self.frame_index = 'down', 0
        self.image = pygame.image.load(join('imagens', 'player.png')).convert_alpha()
        self.image= pygame.transform.scale(self.image, (100, 100))
        self.rect=self.image.get_rect(topleft=(playerPosicao))
        self.originalImg = None
        self.originalRect = None
        self.hitbox=self.rect.inflate(-80,-60)
        self.__energia=VIDA_MAXIMA
        self.playerDir= pygame.math.Vector2(1,0)    
        self.playerSpeed=300
        self.colisoes=colisoes

    def load_imagens(self):
        self.frames = {'left': [], 'right': [], 'up': [], 'down': []}
        for state in self.frames.keys():
            for folder_path, sub_folders, file_names in walk(join('imagens', 'player', state)):
                if file_names:
                    for file_name in sorted(file_names, key=lambda name: int(name.split('.')[0]) if name.split('.')[0].isdigit() else float('inf')):
                        full_path = join(folder_path, file_name)
                        
                        surf = pygame.image.load(full_path).convert_alpha()
                        surf = pygame.transform.scale(surf, (100, 100))
                        self.frames[state].append(surf)
    
    def animate(self, delta):
        if self.playerDir.x != 0:
            self.state = 'right' if self.playerDir.x > 0 else 'left'
        if self.playerDir.y != 0:
            self.state = 'down' if self.playerDir.y > 0 else 'up'

        self.frame_index += 5 * delta
        self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])]

        if self.state == 'left':
            self.image = pygame.transform.flip(self.image, True, False)

    def pegarEnergia(self):
        return self.__energia

    def mudarEnergia(self, valor):
        self.__energia = max(0, min(valor, VIDA_MAXIMA)) 

    def restaurarVidaCompleta(self):
        self.__energia = VIDA_MAXIMA

    def teclas(self):
        keys=pygame.key.get_pressed()

        self.playerDir.x=int(keys[pygame.K_d]-keys[pygame.K_a] )
        self.playerDir.y=int(keys[pygame.K_s]-keys[pygame.K_w] )

        if self.playerDir.length() > 0: 
            self.playerDir = self.playerDir.normalize()

    def movPlayer(self,delta):
         
     
        self.hitbox.x += self.playerDir.x * self.playerSpeed*delta
        self.colidir("horizontal")
        self.hitbox.y += self.playerDir.y * self.playerSpeed*delta
        self.colidir("vertical")
        self.rect.center=self.hitbox.center

    def colidir(self,direcao):
        for objeto in self.colisoes:
            if objeto.rect.colliderect(self.hitbox): 
                if self.playerDir.x > 0 and direcao =="horizontal":
                    self.hitbox.right=objeto.rect.left
                elif self.playerDir.x < 0 and direcao =="horizontal":
                    self.hitbox.left=objeto.rect.right

                elif self.playerDir.y > 0 and direcao =="vertical":
                    self.hitbox.bottom=objeto.rect.top
                elif self.playerDir.y < 0 and direcao =="vertical":
                    self.hitbox.top=objeto.rect.bottom
    
          
    def alimentar(self,tela):
        if self.originalImg == None:
            self.originalImg = self.image
            self.originalRect = self.rect
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect=self.image.get_rect(bottomleft=(100,tela_y))

        x=self.rect.x+50
        y=self.rect.y
       
        rectLife=pygame.Rect(x,y,(self.__energia*2),30)
        rect=pygame.Rect(x,y,200,30)
    
        pygame.draw.rect(tela,"blue",rectLife,0,4)
        pygame.draw.rect(tela,"black",rect,4,4)


    def restaurar(self):

        if self.originalImg:
            self.image = self.originalImg
            self.rect = self.originalRect
            self.originalImg = None
            self.originalRect = None


    def update(self,delta):
        self.teclas()
        self.movPlayer(delta)
        self.animate(delta)



class Arma(pygame.sprite.Sprite):
    def __init__(self, player, grupo):
        self.player = player
        self.distancia = 60  
        self.direcaoPlayer = pygame.math.Vector2(0, 1)  

        
        super().__init__(grupo)
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA) 
        pygame.draw.circle(self.image, (255, 255, 255), (5, 5), 5)  
        self.rect = self.image.get_rect(center=self.player.rect.center + self.direcaoPlayer * self.distancia)

    def mostra_direcao(self):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        player_pos = pygame.Vector2(tela_x / 2, tela_y / 2)
        self.direcaoPlayer = (mouse_pos - player_pos).normalize()

    def rotacao_Arma(self):
        angle = degrees(atan2(self.direcaoPlayer.x, self.direcaoPlayer.y)) - 90
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)  
        pygame.draw.circle(self.image, (255, 0, 0), (5, 5), 5) 
        self.image = pygame.transform.rotate(self.image, angle)  

    def update(self, _):
        self.mostra_direcao() 
        self.rect.center = self.player.rect.center + self.direcaoPlayer * self.distancia  
        self.rotacao_Arma()  

class Bala(pygame.sprite.Sprite):
    def __init__(self, surf, pos, direcao, grupos):
        super().__init__(grupos)
        self.image = surf
        self.rect = self.image.get_rect(center=pos)
        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = 1000
        self.speed = 1200
        self.direcao = direcao

    def update(self, delta):
        self.rect.center += self.direcao * self.speed * delta
        if pygame.time.get_ticks() - self.spawn_time >= self.lifetime:
            self.kill()






