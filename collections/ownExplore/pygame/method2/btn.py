import pygame

topColor = '#ADD8E6'
whiteColor = '#FFFFFF'
hoverColor = '#D74B4B'
bottomColor = '#354B5E'

buttonRadius = 4
buttonSelect = 4

class Button:
  
    def __init__(self, text, width, height, pos, gFont, elevation):
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_posY = pos[1]
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = hoverColor

        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = bottomColor

        self.text_surface = gFont.render(text, True, whiteColor)
        self.text_rect = self.text_surface.get_rect(center=self.top_rect.center)

    def draw(self, surface):

        self.top_rect.y = self.original_posY - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(surface, self.bottom_color, self.bottom_rect, border_radius=buttonRadius)
        pygame.draw.rect(surface, self.top_color, self.top_rect, border_radius=buttonRadius)
        surface.blit(self.text_surface, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            # self.top_color = hoverColor
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                # if self.pressed == True:
                self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            # self.top_color = topColor
        
        



    
