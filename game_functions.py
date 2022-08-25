from lib2to3.pygram import python_grammar_no_print_statement
import sys
import pygame
def check_events():
    #react to the keyboard and  mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
def update_screen(ai_settings, screen, ship):
    #update the screen and switch it to a new screen
    #repaint the screen at every routine
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #visualise the newly painted screen
    pygame.display.flip()
