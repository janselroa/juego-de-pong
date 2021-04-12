import pygame

pygame.init()
BLACK=(0, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('img/player.png')
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.velocidad=0
        self.score=0

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
        self.velocidad_x=3
        self.velocidad_y=3


    def update(self):
        self.rect.y+=self.velocidad_y
        self.rect.x+=self.velocidad_x

        if self.rect.y>600 or self.rect.y<0:
            self.velocidad_y*=-1

        if self.rect.x>800 or self.rect.x<0:
            self.rect.x=400
            self.rect.y=300
            self.velocidad_y*=-1            