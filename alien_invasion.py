import sys
import pygame
from settings import Settings
from ship.py import Ship
import game_functions as gf


def run_game():
    #initialize pygame, settings and screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")  

    #create a ship
    ship = Ship(screen)  

    #start the routine
    while True:
        gf.check_events()
        #speculate the keyboard and the mouse
        for event in pygame.event.get():
            if event.type == pygame.quit:
               sys.exit()
        #repaint the screen at every routine
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #visualise the screeen
        pygame.display.flip()

run_game()
