import pygame
import random

DRINK_SIZE = 100
class Drink(pygame.sprite.Sprite):
    def __init__(self, x, y, img="assets/redbull.png"):
        super().__init__()
        image = pygame.image.load(img)
        self.image = pygame.transform.scale(image,(DRINK_SIZE,DRINK_SIZE))
        self.rect = self.image.get_rect() 
        self.velocity = random.randint(1,5)
        self.rect.x = x
        self.rect.y = y   
        """
        initializes the falling powerups
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
        
    def speed(self):
        """
        changes speed of various falling collectables
        args: None
        return: None
        """
    
    def boost(self):
        """
        lowers sleep counter by 1
        args: None
        return: None
        """