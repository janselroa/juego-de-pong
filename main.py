import pygame
import sys

pygame.init()

# colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

ventana = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Juego de pong')
icono= pygame.image.load('img/icono.png')
pygame.display.set_icon(icono)
clock = pygame.time.Clock()

ancho_jugadores = 20
altura_jugadores = 130

cordenadas_x_j1 = 20
cordenadas_y_j1 = 200
velocidad_j1 = 0

cordenadas_x_j2 = 750
cordenadas_y_j2 = 200
velocidad_j2 = 0

cord_pelota_x = 400
cord_pelota_y = 250
velocidad_p_y =1
velocidad_p_x = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                velocidad_j1 = -3
            if event.key == pygame.K_s:
                velocidad_j1 = 3

            if event.key == pygame.K_DOWN:
                velocidad_j2 = 3
            if event.key == pygame.K_UP:
                velocidad_j2 = -3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                velocidad_j1 = 0
            if event.key == pygame.K_s:
                velocidad_j1 = 0

            if event.key == pygame.K_DOWN:
                velocidad_j2 = 0
            if event.key == pygame.K_UP:
                velocidad_j2 = 0

    cordenadas_y_j2 += velocidad_j2
    cordenadas_y_j1 += velocidad_j1
    cord_pelota_x += velocidad_p_x
    cord_pelota_y += velocidad_p_y
    # dando limites a los jugadores
    if cord_pelota_y>490 or cord_pelota_y<10:
    	velocidad_p_y*=-1

    if cord_pelota_x < 0 or cord_pelota_x > 800:
        cord_pelota_x = 400
        cord_pelota_y = 250

    ventana.fill(BLACK)
    jugador1 = pygame.draw.rect(
        ventana, WHITE, (cordenadas_x_j1, cordenadas_y_j1, ancho_jugadores, altura_jugadores))
    jugador2 = pygame.draw.rect(
        ventana, WHITE, (cordenadas_x_j2, cordenadas_y_j2, ancho_jugadores, altura_jugadores))
    pelota = pygame.draw.circle(
        ventana, WHITE, (cord_pelota_x, cord_pelota_y), 10)
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
    	velocidad_p_x*=-1
    pygame.display.flip()
    clock.tick(80)