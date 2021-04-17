import pygame
import sys
from objects import *

def main():
    pygame.init()
    windows=pygame.display.set_mode((800, 600))

    game=Game()
    while True:
        game.process_event()
        game.run_logic()
        game.display_frame(windows)
        game.CLOCK.tick(100)
if __name__ == '__main__':
    main()