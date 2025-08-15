from config import *
from todasSprites import *
from player import *
from animais import *
from inimigo import Inimigo
from mapa import *

class Jogo():
    def __init__(self):
        pygame.init()
        self.tela=pygame.display.set_mode((tela_x,tela_y))
        pygame.display.set_caption("fazenda")
        self.time=pygame.time.Clock()
        
        self.jogar=True
        self.animalAtual = ""
        self.cena="menu"
        self.load_imagens()

      
        self.todasSprites=todasSprites()
        self.colisaoSprites=pygame.sprite.Group()
        self.alimentarSprites=pygame.sprite.Group()

        self.bala_sprites=pygame.sprite.Group()
        self.nao_atira = True 
        self.tempo_tiro = 0
        self.tempo_de_recarga = 600

        self.mapaConfig() 
        self.player=Player((2000,800),self.colisaoSprites,(self.todasSprites,self.alimentarSprites))
        self.gun = Arma(self.player , self.todasSprites)

        self.inimigo = Inimigo("mal", (0, 0), self.todasSprites)

      
        self.vaca = Vaca("zinhagou", (1973,1913), 8000,(self.colisaoSprites,  self.alimentarSprites,self.todasSprites))
        self.ovelha = Ovelha("Livia", (2689, 1336),7000, (self.colisaoSprites,  self.alimentarSprites,self.todasSprites))
        self. galinha = Galinha("Davos", (1629, 979),5000,  (self.colisaoSprites,  self.alimentarSprites,self.todasSprites))
        self.porco = Porco("guguleiteiro", (1278, 1336), 7000,(self.colisaoSprites,  self.alimentarSprites,self.todasSprites))

    def load_imagens(self):
        self.bullet_self = pygame.image.load(join('imagens', 'pedra.png')).convert_alpha()

    def input(self):
        if pygame.mouse.get_pressed()[0] and self.nao_atira:
            pos = self.gun.rect.center + self.gun.direcaoPlayer * 50
            Bala(self.bullet_self, pos, self.gun.direcaoPlayer, (self.todasSprites, self.bala_sprites))
           
            self.nao_atira = False
            self.tempo_tiro = pygame.time.get_ticks()  

    def tempo_arma(self):
        if not self.nao_atira:
            current_time = pygame.time.get_ticks()  
            if current_time - self.tempo_tiro >= self.tempo_de_recarga:
                self.nao_atira = True
       
    def mapaConfig(self):
        mapa = load_pygame(join('data', 'maps', 'world.tmx'))
        
        for x, y, image in mapa.get_layer_by_name('Ground').tiles():
            escalaImg = pygame.transform.scale(image, (tamanho_tile, tamanho_tile))
            MapaGround((x * tamanho_tile, y * tamanho_tile), escalaImg, self.todasSprites)

        for obj in mapa.get_layer_by_name("Objects"):
            escalax = obj.x * escala
            escalay = obj.y * escala
            escalaImg = pygame.transform.scale(obj.image, (obj.width * escala, obj.height * escala))
            objColisao((escalax, escalay), escalaImg, (self.todasSprites, self.colisaoSprites))

        for obj in mapa.get_layer_by_name("Collisions"):
            escalax = obj.x * escala
            escalay = obj.y * escala
            escalaW = obj.width * escala
            escalaH = obj.height * escala
            escalaSurf = pygame.Surface((escalaW,escalaH))
            objColisao((escalax, escalay), escalaSurf, self.colisaoSprites)

    def checarClick(self):
        mousePos=(0,0)
        if pygame.mouse.get_pressed()[0]:  
            mousePos = pygame.mouse.get_pos()
        return mousePos
   
    def reiniciarJogo(self):
        self.todasSprites = todasSprites()
        self.colisaoSprites = pygame.sprite.Group()
        self.alimentarSprites = pygame.sprite.Group()
        self.bala_sprites=pygame.sprite.Group()


        self.mapaConfig()
        self.player = Player((2000, 800), self.colisaoSprites, (self.todasSprites, self.alimentarSprites))
        self.inimigo = Inimigo("mal", (0, 0), self.todasSprites)
        self.gun = Arma(self.player , self.todasSprites)

        self.vaca = Vaca("zinhagou", (1973, 1913), 8000, (self.colisaoSprites, self.alimentarSprites, self.todasSprites))
        self.ovelha = Ovelha("Livia", (2689, 1336), 7000, (self.colisaoSprites, self.alimentarSprites, self.todasSprites))
        self.galinha = Galinha("Davos", (1629, 979), 5000, (self.colisaoSprites, self.alimentarSprites, self.todasSprites))
        self.porco = Porco("guguleiteiro", (1278, 1336), 7000, (self.colisaoSprites, self.alimentarSprites, self.todasSprites))

        self.cena = "mapa"
    
    def menuAlimentar(self, animal):
        esquerda = tela_x / 2 - 60
        topo = tela_y / 2 + 110
        rect = pygame.Rect(esquerda, topo, 400, 200)
        pygame.draw.rect(self.tela, "white", rect, 0, 4)
        pygame.draw.rect(self.tela, "black", rect, 4, 4)
        fonte = pygame.font.Font(None, 30)
        linhas, colunas = 2, 2
        opcoes = ["alimentar", "acariciar", "sair", ""]
        for linha in range(linhas):
            for coluna in range(colunas):
                x = rect.left + rect.width / 4 + (rect.width / 2) * coluna
                y = rect.top + rect.height / 4 + (rect.height / 2) * linha
                i = coluna + 2 * linha
                texto = fonte.render(opcoes[i], True, "black")
                textoRect = texto.get_rect(center=(x, y))
                self.tela.blit(texto, textoRect)

                mousePos = self.checarClick()
                
                if textoRect.collidepoint(mousePos):
                    if opcoes[i] == "sair":
                        animal.restaurar()
                        self.player.restaurar()
                        self.cena = 'mapa'

                    elif opcoes[i] == "alimentar" and self.player.pegarEnergia() > 10 and animal.pegarEnergia() < 100:
                        animal.mudarEnergia(animal.pegarEnergia() + 1)
                        self.player.mudarEnergia(self.player.pegarEnergia() - 1)

                    elif opcoes[i] == "acariciar" and animal.pegarEnergia() > 10 and self.player.pegarEnergia() < 100:
                        animal.mudarEnergia(animal.pegarEnergia() - 1)
                        self.player.mudarEnergia(self.player.pegarEnergia() + 1)

                
    def rodar(self):

  
        while self.jogar:
            if self.cena=="mapa":
                delta=self.time.tick()/1000


                if self.player.pegarEnergia() == 0:
                    self.cena = "game over"
                for animal in [self.vaca, self.ovelha, self.galinha, self.porco]:
                    if animal.pegarEnergia() == 0:
                        self.cena = "game over"
            
                self.tempo_arma()
                self.input()
                self.todasSprites.update(delta)

                for bala in self.bala_sprites:
                    if pygame.sprite.collide_rect(bala, self.inimigo):
                        self.player.mudarEnergia(self.player.pegarEnergia() + 20)
                        self.inimigo.morrer()  
                        bala.kill()
                
            
                self.tela.fill('black')
                self.todasSprites.draw(self.player.rect.center)


                self.inimigo.atacando() 
                self.inimigo.atacaPlayer(self.player, delta)


                animais= [self.galinha, self.vaca, self.porco, self.ovelha]
                for animal in animais:
                    animal.reduzirEnergia()
                    keys=pygame.key.get_pressed()
                    if animal.rect.colliderect(self.player.rect) and keys[pygame.K_e]:
                        self.animalAtual=animal
                        self.cena="alimentar"
                        
                
                  


            elif self.cena == "game over":
                keys=pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    self.reiniciarJogo()
                self.tela.fill("black")
                fonte = pygame.font.Font(None, 74)
                texto = fonte.render("GAME OVER", True, (255, 0, 0))
                self.tela.blit(texto, (tela_x // 2 - texto.get_width() // 2, tela_y // 2 - texto.get_height() // 2))

            elif self.cena=="alimentar":
                self.tela.fill("burlywood2")
                self.alimentarSprites.draw(self.tela)
              
                self.player.alimentar(self.tela)
           
                self.animalAtual.alimentar(self.tela)
                self.menuAlimentar(self.animalAtual)
           
            

            elif self.cena=='menu':
                fundo= pygame.image.load(join('imagens', 'fundo.png')).convert_alpha()
                self.tela.blit(fundo,(0,0))
                fonte=pygame.font.Font(None, 74)
                play = pygame.Rect(tela_x // 2 - 100, tela_y // 2 + 10 , 200, 50)
                sair = pygame.Rect(tela_x // 2 - 100, tela_y // 2 + 200, 200, 50)

                pygame.draw.rect(self.tela, "blue", play)
                pygame.draw.rect(self.tela, "red", sair)

                playTxt = fonte.render("Play", True, "white")
                sairTxt = fonte.render("Exit", True, "white")

                self.tela.blit(playTxt, (play.x + 50, play.y + 5))
                self.tela.blit(sairTxt, (sair.x + 50, sair.y + 5))

                mousePos=self.checarClick()

                if play.collidepoint(mousePos):
                    self.cena = "mapa"
                
                if sair.collidepoint(mousePos):
                    self.jogar = False
                          
               
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.jogar = False

            pygame.display.flip()
        pygame.quit()

game=Jogo()
game.rodar()