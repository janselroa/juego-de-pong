import pygame
import sys
from objects import *

pygame.init()

# CONSTANTES
FONDO=pygame.image.load('img/background.png')
CLOCK=pygame.time.Clock()
WIDTH, HEIGHT=800, 600
SIDE=(WIDTH, HEIGHT)
FONT=pygame.font.Font(None, 35)
# colores
BLACK=(0,0,0)
WHITE=(244,244, 244)

windows=pygame.display.set_mode(SIDE)
pygame.display.set_caption('Pong')

sprites_list=pygame.sprite.Group()

# players
player1=Player()
player1.rect.y=300
player1.rect.x=20
sprites_list.add(player1)

player2=Player()
player2.rect.y=300
player2.rect.x=750
sprites_list.add(player2)

# pelota
pelota=Pelota()
pelota.rect.x=400
pelota.rect.y=300
sprites_list.add(pelota)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_w:
        		player1.changespeed(-3)
        	if event.key == pygame.K_s:
        		player1.changespeed(3)
        	if event.key == pygame.K_UP:
        		player2.changespeed(-3)
        	if event.key == pygame.K_DOWN:
        		player2.changespeed(3)
        
        if event.type == pygame.KEYUP:
        	if event.key == pygame.K_w:
        		player1.changespeed(0)
        	if event.key == pygame.K_s:
        		player1.changespeed(0)
       		
       		if event.key == pygame.K_UP:
        		player2.changespeed(0)
        	if event.key == pygame.K_DOWN:
        		player2.changespeed(0)

    # detectando colisiones
    if pygame.sprite.collide_rect(pelota, player1) or  pygame.sprite.collide_rect(pelota, player2):
    	pelota.velocidad_x*=-1
    	pelota.velocidad_y*=-1
    if pelota.rect.x <3:
    	player2.score+=1
    if pelota.rect.x >798:
    	player1.score+=1
    windows.blit(FONDO, (0, 0))
    text_puntaje_p1=FONT.render(f'{player1.score}', 35,WHITE)
    text_puntaje_p2=FONT.render(f'{player2.score}', 35,WHITE)
    windows.blit(text_puntaje_p1,(30, 20))
    windows.blit(text_puntaje_p2,(700, 20))
    sprites_list.draw(windows)
    sprites_list.update()
    pygame.display.flip()
    CLOCK.tick(120)