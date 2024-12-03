import pygame
PLAYER_SIZE = 200

class Player(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, img="assets/student.png"):
        super().__init__()
        #image
        image = pygame.image.load(img)
        self.image = pygame.transform.scale(image,(PLAYER_SIZE,PLAYER_SIZE))
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y   
        """
        initializes the player character
        args: (int) x and y coordinates of position; (file) jpg of character
        return: None
        """
        
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]: 
            self.rect.x +=10
        if key[pygame.K_LEFT]: 
            self.rect.x -=10
        # if key[pygame.K_UP]: 
        #     self.rect.y -=10
        # if key[pygame.K_DOWN]: 
        #     self.rect.y +=10
        """
        moves position right, left, up, or down by 1
        args: None
        return: None
        """
    
    def update(self):
        self.move()
#make speed decrease when hit by an obstacle???     