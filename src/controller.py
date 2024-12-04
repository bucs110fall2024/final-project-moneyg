import pygame
import random
from src.button import Button
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
    
    #game state
    self.state = "START"
     
    #background
    self.background = pygame.transform.scale(pygame.image.load("assets/lecturehall.png"), (SCREEN_WIDTH,SCREEN_HEIGHT))
    self.screen.blit(self.background,(0,0)) 
    
    #text
    self.font = pygame.font.Font("assets/font.ttf",50)
    self.lives = 3
    self.text = self.font.render(f"ENERGY LEVELS:{self.lives}/3", False, "White")
        
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
      if self.state == "START":
        self.startloop()
      elif self.state =="END":
        self.endloop()
      elif self.state == "GAME":
        self.gameloop()

  """
  runs game program
  """
    
  def startloop(self):
    while self.state == "START":
      start_background = pygame.transform.scale(pygame.image.load("assets/classroomwing.png"), (SCREEN_WIDTH,SCREEN_HEIGHT))
      self.screen.blit(start_background,(0,0))
      
      pygame.mixer.music.load("assets/classroom.mp3") 
      pygame.mixer.music.play(-1)   
        
      title_font = pygame.font.Font("assets/font.ttf",200)
      title = title_font.render(f"WAKE UP!!", False, "Yellow")
      self.screen.blit(title,(SCREEN_WIDTH/6, SCREEN_HEIGHT - 600))

      start_button = Button(SCREEN_WIDTH/2 - 200, SCREEN_HEIGHT - 250, color=(22,33,120), text = "GO TO CLASS")
      button_group = pygame.sprite.Group()
      button_group.add(start_button)
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        elif start_button.rect.collidepoint(pygame.mouse.get_pos()):
          if event.type == pygame.MOUSEBUTTONDOWN:
              self.state = "GAME"
      
      if start_button.rect.collidepoint(pygame.mouse.get_pos()):
          start_button.highlight()
      else:
          start_button.color_default() 
      
      button_group.draw(self.screen)
      pygame.display.update()

  def endloop(self):
      while self.state == "END":
        start_background = pygame.transform.scale(pygame.image.load("assets/teacheryelling.png"), (SCREEN_WIDTH,SCREEN_HEIGHT))
        self.screen.blit(start_background,(0,0))
        pygame.mixer.music.stop()
        
        end_font = pygame.font.Font("assets/font.ttf",150)
        end = end_font.render(f"YOU FELL ASLEEP!", False, "Yellow")
        self.screen.blit(end,(50, 200))
        
        end_button = Button(SCREEN_WIDTH/2 - 200, SCREEN_HEIGHT - 250, width=425, color=(22,33,120), text = "WAKE BACK UP")
        endbutton_group = pygame.sprite.Group()
        endbutton_group.add(end_button)
        
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            exit()
          elif end_button.rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "START"
                self.lives = 3
                self.text = self.font.render(f"ENERGY LEVELS:{self.lives}/3", False, "White")
          
        if end_button.rect.collidepoint(pygame.mouse.get_pos()):
          end_button.highlight()
        else:
          end_button.color_default() 
        endbutton_group.draw(self.screen)
        pygame.display.update()

  def gameloop(self):
      while self.state == "GAME":
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        #movement
        self.player.move()
            
        #health spawning
        current_time = pygame.time.get_ticks()
        if current_time >= self.collectable_spawn_time:
          self.collectable = Drink(random.randint(0,SCREEN_WIDTH - 20), 0)
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
            snore_sound = pygame.mixer.Sound("assets/snore.mp3")
            pygame.mixer.Sound.play(snore_sound)
            self.text = self.font.render(f"ENERGY LEVELS:{self.lives}/3", False, "White")
              
        health = pygame.sprite.spritecollide(self.player, self.collectable_group, True)
        for life in health:
          if self.lives < 3:
            self.lives += 1
            drink_sound = pygame.mixer.Sound("assets/drink.mp3")
            pygame.mixer.Sound.play(drink_sound)
            self.text = self.font.render(f"ENERGY LEVELS:{self.lives}/3", False, "White")
            
        if self.lives == 0:
          self.state = "END"
          lose_sound = pygame.mixer.Sound("assets/yell.mp3")
          pygame.mixer.Sound.play(lose_sound)

        #redraw
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.text,(10,0))
            
        #draw sprites
        self.player_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.collectable_group.update()
        self.collectable_group.draw(self.screen)
        #print(len(self.enemy_group))

        pygame.display.update()
        clock.tick(80) #controls frame rate   