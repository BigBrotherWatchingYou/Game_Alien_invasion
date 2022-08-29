import pygame
class Ship():
    def __init__(self, ai_settings, screen):
        #position initialise
        self.screen = screen
        self.ai_settings = ai_settings

        #load bmp
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #move the ship to the bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #store the decimal in the property
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
    #check and move position   
    #update the center instead of rect 
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        self.rect.centerx = self.center
    def blitme(self):
        #paint the ship
        self.screen.blit(self.image, self.rect)

        
    
