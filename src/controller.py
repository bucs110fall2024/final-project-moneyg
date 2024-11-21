import pygame
import Player
import Customer

class Controller:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode()
    self.background = pygame.Surface(pygame.display.get_window_size())
    self.background.fill((150, 150, 250))
    """
    initializes screen
    args: None
    return: None
    """
    
  def mainloop(self):
   """
   runs game program
   """
   while(True): 
      #1. Handle events
      for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               exit()

      #2. detect collisions and update models
      #3. Redraw next frame
      #4. Display next frame
      pygame.display.flip()
    
  

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
