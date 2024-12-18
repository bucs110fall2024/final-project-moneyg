import pygame
import random

DRINK_SIZE = 100
DRINK_LOWER_SPEED = 1
DRINK_UPPER_SPEED = 5

class Drink(pygame.sprite.Sprite):
    def __init__(self, x, y, img="assets/redbull.png"):
        super().__init__()
        image = pygame.image.load(img)
        self.image = pygame.transform.scale(image,(DRINK_SIZE,DRINK_SIZE))
        self.rect = self.image.get_rect() 
        self.velocity = random.randint(DRINK_LOWER_SPEED, DRINK_UPPER_SPEED)
        self.rect.topleft = (x,y) 
        """
        initializes the falling collectables
        args: (int) x and y coordinates of position; (str) path to jpg file of character
        return: None
        """
        
    def update(self):
        self.rect.y += self.velocity
        """
        moves collectables down toward the player
        args: None
        return: None
        """
