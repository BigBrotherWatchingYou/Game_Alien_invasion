import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #a class to manage bullet

    def __init__(self, ai_settings, screen, ship):
        #create a bullet
        super(Bullet, self).__init__()
        self.screen = screen

        #create a bullet at (0,0)
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store the position
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        #move the mullet
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        #update the position
        self.rect.y = self.y

    def draw_bullet(self):
        #draw a bullet
        pygame.draw.rect(self.screen, self.color, self.rect)
