import pygame

FONT_SIZE = 55
MESSAGE_XY = 20
class Button(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, width=400, height=100, color="red", text="text"):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color
        self.image.fill(self.color)

        text_color = ("white") 
        self.message = pygame.font.Font("assets/font.ttf", FONT_SIZE).render(text, True, text_color)
        self.image.blit(self.message, (MESSAGE_XY, MESSAGE_XY))
    """
    initializes button
    args: (int) x,y coordinates, (int) width and height, (str/int) color as string or RGB value, (str) button text
    return: None
    """

    def highlight(self):
        highlight_color = []
        for i, c in enumerate(self.color):
            if c+50 < 255:
                highlight_color.append(c+50) 
            else:
                highlight_color.append(255)
        self.image.fill(highlight_color)
        self.image.blit(self.message, (MESSAGE_XY, MESSAGE_XY))
    """
    highlights button
    args: None
    return: None
    """

    def color_default(self):
        self.image.fill(self.color)
        self.image.blit(self.message, (MESSAGE_XY, MESSAGE_XY))
    """
    displays message on button
    args: None
    return: None
    """