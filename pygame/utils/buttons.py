import pygame


class Button:
    def __init__(self, screen, text, width, height, x, y, btnFunction=None):

        self.fillColors = {
            "white": "#ffffff",
            "hover": "#666666",
            "pressed": "#333333",
            "black": "#000000",
            "blue": "#0AEFF7",
        }
        self.screen = screen
        self.name = text
        self.font = pygame.font.Font(None, 24)
        self.text = self.font.render(self.name, True, self.fillColors["black"])
        self.btn_width = width
        self.btn_height = height
        self.posx = x
        self.posy = y
        self.btnClick = btnFunction
        self.clicked = False

        self.btnSurface = pygame.Surface((self.btn_width, self.btn_height))
        self.btnRect = self.btnSurface.get_rect(center=(self.posx, self.posy))

        self.textSurface = self.text.get_rect(
            center=(self.btn_width // 2, self.btn_height // 2)
        )

        self.mouse = pygame.mouse.get_pos()

    def drawBtn(self):

        self.btnSurface.fill(self.fillColors["white"])

        if self.btnRect.collidepoint(self.mouse):
            self.btnSurface.fill(self.fillColors["hover"])
            self.text = self.font.render(self.name, True, self.fillColors["white"])
            if pygame.mouse.get_pressed()[0]:
                self.btnSurface.fill(self.fillColors["blue"])

        self.btnSurface.blit(self.text, self.textSurface)
        self.screen.blit(self.btnSurface, self.btnRect.topleft)

    def is_clicked(self, mouse_pos, mouse_press):
        if self.btnRect.collidepoint(mouse_pos) and mouse_press[0]:
            self.clicked = True
            self.btnClick(True)
        else:
            self.btnClick(False)
            self.clicked = False
