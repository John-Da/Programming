import pygame


# white color 
color = (255,255,255) 
# light shade of the button 
color_light = (170,170,170) 
# dark shade of the button 
color_dark = (100,100,100) 




class PlayBtn:
    def __init__(self, screen):
        self.screen = screen
        self.btnwidth = self.screen.get_width()
        self.btnheight = self.screen.get_height()

        self.font = pygame.font.Font(None, 24)
        self.text = self.font.render('Click', True, color)

        self.mouse = pygame.mouse.get_pos()



    def drawBtn(self):
        if self.btnwidth/2 <= self.mouse[0] <= self.btnwidth/2+140 and self.btnheight/2 <= self.mouse[1] <= self.btnheight/2+40:
            pygame.draw.rect(self.screen, color_light, [self.btnwidth/2, self.btnheight/2, 140, 40])
        else:
            pygame.draw.rect(self.screen, color_dark, [self.btnwidth/2, self.btnheight/2, 140, 40])
        
        return self.screen.blit(self.text, (self.btnwidth/2+50, self.btnheight/2))
    
    
            