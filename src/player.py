import pygame
import random

PLAYER_SIZE = 200
PLAYER_SPEED = 5
PLAYER_X = 700
PLAYER_Y = 600
PLAYER_DOWN_LIMIT = 900
PLAYER_RIGHT_LIMIT = 1500

class Player(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, img="assets/student.png"):
        super().__init__()
        #image
        image = pygame.image.load(img)
        self.image = pygame.transform.scale(image,(PLAYER_SIZE,PLAYER_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y   
        
        #hitbox
        center = self.rect.center 
        self.hitbox = self.rect.scale_by(0.5)
        self.hitbox.center = center
        
        """
        initializes the player character
        args: (int) x and y coordinates of position; (file) jpg of character
        return: None
        """
        
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]: 
            self.rect.x += PLAYER_SPEED
        if key[pygame.K_LEFT]: 
            self.rect.x -= PLAYER_SPEED
        if key[pygame.K_UP]: 
            self.rect.y -= PLAYER_SPEED
        if key[pygame.K_DOWN]: 
            self.rect.y += PLAYER_SPEED
        self.hitbox.center = self.rect.center #moves hitbox with player
        
        """
        moves position right, left, up, or down by 1
        args: None
        return: None
        """
    
    def update(self):
        if self.hitbox.bottom > PLAYER_DOWN_LIMIT or self.hitbox.top < 0 or self.hitbox.right > PLAYER_RIGHT_LIMIT or self.hitbox.left < 0:
            self.rect.x = PLAYER_X
            self.rect.y = PLAYER_Y
        
        self.move()
