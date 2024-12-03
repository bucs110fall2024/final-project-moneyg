import pygame
import random
SLEEP_SIZE = 100
class Sleep(pygame.sprite.Sprite):
    def __init__(self, x, y, img="assets/sleepy.png"):
        super().__init__()
        image = pygame.image.load(img)
        self.image = pygame.transform.scale(image,(SLEEP_SIZE,SLEEP_SIZE))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1,5)
        self.rect.topleft = (x,y)
        # self.rect.x = x
        # self.rect.y = y   
        
        """
        initializes the falling obstacles
        args: (int) x and y coordinates of position; (str) path to img file of obstacle
        return: None
        """
        
    def update(self):
        self.rect.y += self.velocity
        
        if self.rect.top > 1500:
            self.rect.y = -self.rect.height
            self.rect.x = random.randint(0,1000 - self.rect.width)
        """
        moves obstacles down toward the player
        args: None
        return: None
        """
        
    def speed(self):
        """
        changes speed of various falling obstacles
        args: None
        return: None
        """
    
    def lose(self):
        """
        increases sleep counter by 1
        args: None
        return: None
        """