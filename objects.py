import pygame, sys
import random

pygame.init()

#colores rgb
BLACK=(0, 0, 0)
WHITE=(255, 255, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image=pygame.image.load('img/player.png')
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.velocidad=0
        self.score=0
        self.rect.x=x
        self.rect.y=y

    def changespeed(self,v):
        self.velocidad=v

    def update(self):
        self.rect.y+=self.velocidad
        if self.rect.y>550 or self.rect.y<0:
            self.velocidad*=-1

class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('img/pelota.png')
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.velocidad_x=4
        self.velocidad_y=5


    def update(self):
        self.rect.y+=self.velocidad_y
        self.rect.x+=self.velocidad_x

        if self.rect.y>600 or self.rect.y<0:
            self.velocidad_y*=-1

        if self.rect.x>800 or self.rect.x<0:
            self.rect.x=400
            self.rect.y=300
            self.velocidad_y*=-1

class Game:
    def __init__(self):
        self.FONDO=pygame.image.load('img/background.png')
        self.CLOCK=pygame.time.Clock()
        self.WIDTH=800 
        self.HEIGHT=600
        self.SIDE=(self.WIDTH, self.HEIGHT)
        self.FONT=pygame.font.Font(None, 35)
        self.BLACK=(0,0,0)
        self.WHITE=(244,244, 244)

        #sprites
        self.all_sprites_list=pygame.sprite.Group()
        self.players_list=pygame.sprite.Group()

        self.player1=Player(20, 300)
        self.player2=Player(750,300)
        
        self.pelota=Pelota()

        self.all_sprites_list.add(self.player1)
        self.all_sprites_list.add(self.player2)
        self.all_sprites_list.add(self.pelota)

    def process_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player1.changespeed(-3)
                if event.key == pygame.K_s:
                    self.player1.changespeed(3)
                if event.key == pygame.K_UP:
                    self.player2.changespeed(-3)
                if event.key == pygame.K_DOWN:
                    self.player2.changespeed(3)
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.player1.changespeed(0)
                if event.key == pygame.K_s:
                    self.player1.changespeed(0)
                
                if event.key == pygame.K_UP:
                    self.player2.changespeed(0)
                if event.key == pygame.K_DOWN:
                    self.player2.changespeed(0)

    def run_logic(self):
        # detectando colisiones
        if pygame.sprite.collide_rect(self.pelota, self.player1) or  pygame.sprite.collide_rect(self.pelota, self.player2):
            self.pelota.velocidad_x*=-1
            self.pelota.velocidad_y*=-1
            self.pelota.velocidad_y=random.randint(1, 10)

        if self.pelota.rect.x <3:
            self.player2.score+=1
        if self.pelota.rect.x >798:
            self.player1.score+=1

    def display_frame(self, windows):
        windows.blit(self.FONDO, (0, 0))
        self.all_sprites_list.draw(windows)
        self.all_sprites_list.update()
        self.text_puntaje_p1=self.FONT.render(f'{self.player1.score}', 35,WHITE)
        self.text_puntaje_p2=self.FONT.render(f'{self.player2.score}', 35,WHITE)
        windows.blit(self.text_puntaje_p1,(30, 20))
        windows.blit(self.text_puntaje_p2,(700, 20))
        pygame.display.flip()
