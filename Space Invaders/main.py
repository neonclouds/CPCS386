import sys
import pygame

from settings import Settings
from ship import Ship
from aliens import Aliens

import game_functions as gf




def run_game():
    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Space Invaders")

    ship = Ship(screen)

    while True:


        gf.check_events()
        gf.update_screen(settings, screen, ship)

run_game()