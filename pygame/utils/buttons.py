import pygame


def btnFunction(clicked, button_name):
    if clicked:
        if button_name == 'Click':
            print("Super")
        elif button_name == 'Button':
            print("Moon")
        else:
            pass

class Button:
    def __init__(self, screen, name, width, height, x, y):

        self.fillColors = {
            "white": "#ffffff",
            "hover": "#666666",
            "pressed": "#333333",
            "black": "#000000",
            "blue": "#0AEFF7",
        }
        self.screen = screen
        self.name = name
        self.font = pygame.font.Font(None, 24)
        self.text = self.font.render(self.name, True, self.fillColors["black"])
        self.btn_width = width
        self.btn_height = height
        self.posx = x
        self.posy = y

        self.btnSurface = pygame.Surface((self.btn_width, self.btn_height))
        self.btnRect = self.btnSurface.get_rect(center=(self.posx, self.posy))

        self.textSurface = self.text.get_rect(
            center=(self.btn_width // 2, self.btn_height // 2)
        )

        self.mouse = pygame.mouse.get_pos()


    def is_clicked(self, mouse_pos, mouse_press):
        pressed = self.btnRect.collidepoint(mouse_pos) and mouse_press[0]
        btnFunction(pressed, self.name)
            


    def drawBtn(self):

        self.btnSurface.fill(self.fillColors["white"])

        if self.btnRect.collidepoint(self.mouse):
            self.btnSurface.fill(self.fillColors["hover"])
            self.text = self.font.render(self.name, True, self.fillColors["white"])
            if pygame.mouse.get_pressed()[0]:
                self.btnSurface.fill(self.fillColors["blue"])
                btnFunction(True,self.name)

        self.btnSurface.blit(self.text, self.textSurface)
        self.screen.blit(self.btnSurface, self.btnRect.topleft)

    
