import pygame
import random
from src.button import Button
from src.player import Player
from src.enemy import Sleep
from src.collectable import Drink

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
PLAYER_X = 700
PLAYER_Y = 600
LIVES = 3
ENERGY_TEXT_SIZE = 50
ENEMIES = 7
ENEMY_DISTANCE = 250
DRINK_TIME_LOW = 2000
DRINK_TIME_HIGH = 10000
TITLE_TEXT_SIZE = 200
BUTTON_COLOR = (22,33,120)
END_TEXT_SIZE = 150
END_TEXT_X = 50
END_TEXT_Y = 200
END_BUTTON_WIDTH = 425
SELF_TEXT_X = 10
SELF_TEXT_Y = 0

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
    self.font = pygame.font.Font("assets/font.ttf", ENERGY_TEXT_SIZE)
    self.lives = 3
    self.text = self.font.render(f"ENERGY LEVELS:{self.lives}/3", False, "White")
        
    #sprite groups
    #player
    self.player_group = pygame.sprite.Group()
    self.player = Player(PLAYER_X,PLAYER_Y)
    self.player_group.add(self.player)
    
    #enemies
    self.enemy_group = pygame.sprite.Group()
    for i in range(ENEMIES):
      self.enemy = Sleep(ENEMY_DISTANCE*i,0)
      self.enemy_group.add(self.enemy)
    
    #collectables
    self.collectable_group = pygame.sprite.Group()
    self.collectable_spawn_time = pygame.time.get_ticks() + random.randint(DRINK_TIME_LOW,DRINK_TIME_HIGH)
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
    #start menu sounds
    bird_sound = pygame.mixer.Sound("assets/birds.mp3")
    bird_sound.play(-1)
    
    while self.state == "START":
      #background
      start_background = pygame.transform.scale(pygame.image.load("assets/classroomwing.png"), (SCREEN_WIDTH,SCREEN_HEIGHT))
      self.screen.blit(start_background,(0,0))
      
      #title
      title_font = pygame.font.Font("assets/font.ttf", TITLE_TEXT_SIZE)
      title = title_font.render(f"WAKE UP!!", False, "Yellow")
      self.screen.blit(title,(SCREEN_WIDTH/6, SCREEN_HEIGHT - 600))

      #start button
      start_button = Button(SCREEN_WIDTH/2 - 200, SCREEN_HEIGHT - 250, color=(BUTTON_COLOR), text = "GO TO CLASS")
      button_group = pygame.sprite.Group()
      button_group.add(start_button)
      
      #button click
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        elif start_button.rect.collidepoint(pygame.mouse.get_pos()):
          if event.type == pygame.MOUSEBUTTONDOWN:
              bird_sound.stop()
              pygame.mixer.music.load("assets/classroom.mp3") 
              pygame.mixer.music.play(-1)  
              self.state = "GAME"
      
      #button highlight
      if start_button.rect.collidepoint(pygame.mouse.get_pos()):
          start_button.highlight()
      else:
          start_button.color_default() 
      
      button_group.draw(self.screen)
      pygame.display.update()

  def endloop(self):
      while self.state == "END":
        #background
        start_background = pygame.transform.scale(pygame.image.load("assets/teacheryelling.png"), (SCREEN_WIDTH,SCREEN_HEIGHT))
        self.screen.blit(start_background,(0,0))
        pygame.mixer.music.stop()
        
        #end text
        end_font = pygame.font.Font("assets/font.ttf",END_TEXT_SIZE)
        end = end_font.render(f"YOU FELL ASLEEP!", False, "Yellow")
        self.screen.blit(end,(END_TEXT_X, END_TEXT_Y))
        
        #end button
        end_button = Button(SCREEN_WIDTH/2 - 200, SCREEN_HEIGHT - 250, width=END_BUTTON_WIDTH, color=(BUTTON_COLOR), text = "WAKE BACK UP")
        endbutton_group = pygame.sprite.Group()
        endbutton_group.add(end_button)
        
        #collisions
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            exit()
          elif end_button.rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "START"
                self.lives = LIVES
                self.text = self.font.render(f"ENERGY LEVELS:{self.lives}/3", False, "White")
        
        #button highlight
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
          self.collectable_spawn_time = current_time + random.randint (DRINK_TIME_LOW, DRINK_TIME_HIGH)
            
        #collisions
        for enemy in self.enemy_group:
          if self.player.hitbox.colliderect(enemy.rect):
            self.enemy_group.remove(enemy)
            respawn_enemy = Sleep(random.randint(0,SCREEN_WIDTH), SCREEN_HEIGHT + 50)
            self.enemy_group.add(respawn_enemy) 
            #counter
            if self.lives > 0:
              self.lives -= 1
              snore_sound = pygame.mixer.Sound("assets/snore.mp3")
              pygame.mixer.Sound.play(snore_sound)
              self.text = self.font.render(f"ENERGY LEVELS:{self.lives}/3", False, "White")
              
        for drink in self.collectable_group:
          if self.player.hitbox.colliderect(drink.rect):
            self.collectable_group.remove(drink)
            #counter
            if self.lives < LIVES:
              self.lives += 1
              drink_sound = pygame.mixer.Sound("assets/drink.mp3")
              pygame.mixer.Sound.play(drink_sound)
              self.text = self.font.render(f"ENERGY LEVELS:{self.lives}/3", False, "White")
          
        #end game
        if self.lives == 0:
          self.state = "END"
          lose_sound = pygame.mixer.Sound("assets/yell.mp3")
          pygame.mixer.Sound.play(lose_sound)

        #redraw
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.text,(SELF_TEXT_X,SELF_TEXT_Y))
            
        #draw sprites
        self.player_group.draw(self.screen)
        #pygame.draw.rect(self.screen, "red", self.player.hitbox, 2) to check hitbox placement
        self.player_group.update()
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.collectable_group.update()
        self.collectable_group.draw(self.screen)

        pygame.display.update()
        clock.tick(80) #controls frame rate   