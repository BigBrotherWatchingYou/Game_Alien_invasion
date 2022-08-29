import pygame
from pygame.sprite import Group
import sys
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    #initialize
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #create a ship
    ship = Ship(ai_settings, screen)

    #create a group to store the bullet
    bullets = Group()

    #start game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
        
        

run_game()
