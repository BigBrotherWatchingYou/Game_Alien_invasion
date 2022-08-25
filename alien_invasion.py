import sys
import pygame

def run_game():
    #initialize the game and create a screen object
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    
    #set the background color
    bg_color = (230, 230, 230)
    #start the routine
    while True:
        #speculate the keyboard and the mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
        
                sys.exit()
        #repaint the screen at every routine
        screen.fill(bg_color)
        
        #visualise the screeen
        pygame.display.flip()

run_game()
