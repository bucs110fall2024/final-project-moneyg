import pygame
import random
from src.player import Player
from src.enemy import Sleep
from src.collectable import Drink

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
PLAYER_Y = 600
PLAYER_X = 200
clock = pygame.time.Clock()

class Controller:
  def __init__(self):
    super().__init__()
    #create screen
    pygame.init() 
    self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("WAKE UP!!")
     
    #background
    self.background = pygame.transform.scale(pygame.image.load("assets/lecturehall.png"), (SCREEN_WIDTH,SCREEN_HEIGHT))
    self.screen.blit(self.background,(0,0))
    
    #text
    self.font = pygame.font.Font("assets/font.ttf",50)
    self.lives = 3
    self.text = self.font.render(f"ENERGY LEVELS:{self.lives}/3", False, "Black")
        
    #sprite groups
    #player
    self.player_group = pygame.sprite.Group()
    self.player = Player(PLAYER_X,PLAYER_Y)
    self.player_group.add(self.player)
    
    #enemies
    self.enemy_group = pygame.sprite.Group()
    for i in range(6):
      self.enemy = Sleep(250*i,0)
      self.enemy_group.add(self.enemy)
    
    #collectables
    self.collectable_group = pygame.sprite.Group()
    self.collectable_spawn_time = pygame.time.get_ticks() + random.randint(2000,10000)
    
    """
    initializes screen
    args: None
    return: None
    """
    
  def mainloop(self):
      while(True):
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  exit()
          
          #movement
          self.player.move()
          
          #health spawning
          current_time = pygame.time.get_ticks()
          if current_time >= self.collectable_spawn_time:
            self.collectable = Drink(random.randint(0,SCREEN_WIDTH - 20), SCREEN_HEIGHT + 50)
            self.collectable_group.add(self.collectable)
            self.collectable_spawn_time = current_time + random.randint (2000,10000)
          
          #collisions
          enemies = pygame.sprite.spritecollide(self.player, self.enemy_group, True)
          for enemy in enemies:
            respawn_enemy = Sleep(random.randint(0,SCREEN_WIDTH), SCREEN_HEIGHT + 50)
            self.enemy_group.add(respawn_enemy)
            #counter
            if self.lives > 0:
              self.lives -= 1
              self.text = self.font.render(f"ENERGY LEVELS:{self.lives}/3", False, "Black")
            
          health = pygame.sprite.spritecollide(self.player, self.collectable_group, True)
          for life in health:
            if self.lives < 3:
              self.lives += 1
              self.text = self.font.render(f"ENERGY LEVELS:{self.lives}/3", False, "Black")

          #redraw
          self.screen.blit(self.background,(0,0))
          self.screen.blit(self.text,(SCREEN_WIDTH-500,0))
          
          #draw sprites
          self.player_group.draw(self.screen)
          self.enemy_group.update()
          self.enemy_group.draw(self.screen)
          self.collectable_group.update()
          self.collectable_group.draw(self.screen)
          #print(len(self.enemy_group))

          pygame.display.update()
          clock.tick(80) #controls frame rate   
"""
runs game program
"""
    
  #def menuloop(self):
      #event loop
      #update data
      #redraw
      
  #def gameloop(self):
      #event loop
      #update data
      #redraw
    
  #def gameoverloop(self):
      #event loop
      #update data
      #redraw

#self.screen.blit(self.drink.image, self.drink.rect)