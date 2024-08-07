import pygame


# white color 
# color = (255,255,255) 
# light shade of the button 
# color_light = (170,170,170) 
# dark shade of the button 
# color_dark = (100,100,100) 




class Button:
    def __init__(self,screen, text, width, height, x, y,btnFunction=None, onePress=False):
        

        self.fillColors={
            'white': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
            'black': '#000000',
        }
        self.screen = screen
        self.name = text
        self.font = pygame.font.Font(None, 24)
        self.text = self.font.render(self.name, True, self.fillColors['black'])
        self.btn_width = width
        self.btn_height = height
        self.posx = x
        self.posy = y
        self.onePress = onePress
        self.alreadyPressed = False
        self.btnClick = btnFunction
        self.clicked = False
        
        

        self.btnSurface = pygame.Surface((self.btn_width, self.btn_height))
        self.btnRect = self.btnSurface.get_rect(center=(self.posx, self.posy))

        self.textSurface = self.text.get_rect(center=(self.btn_width//2, self.btn_height//2))

        self.mouse = pygame.mouse.get_pos()



    def drawBtn(self, event):
        self.mouse = pygame.mouse.get_pos()

        self.btnSurface.fill(self.fillColors['white'])

        if self.btnRect.collidepoint(self.mouse):
            self.btnSurface.fill(self.fillColors['hover'])
            self.text = self.font.render(self.name, True, self.fillColors['white'])
            self.is_clicked(event)
            


        self.btnSurface.blit(self.text, self.textSurface)
        self.screen.blit(self.btnSurface, self.btnRect.topleft)


    def is_clicked(self, event):
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if self.btnRect.collidepoint(event.pos):
        #         self.btnClick(True)
        #         self.onePress = False

        # elif event.type == pygame.MOUSEBUTTONUP and self.onePress:
        #     if self.btnRect.collidepoint(event.pos):
        #         self.btnClick(True)
        #         self.onePress = False
        #     self.onePress = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.btnRect.collidepoint(self.mouse):
                self.btnClick(True)

        # if pygame.mouse.get_pressed()[0]:
        #     self.btnSurface.fill(self.fillColors['pressed'])
        #     if self.onePress:
        #         self.btnClick(True)
        #     if not self.alreadyPressed:
        #         self.btnClick(True)
        #         self.alreadyPressed = True
        # else:
        #     self.btnClick(False)
        #     self.alreadyPressed = False

    
            