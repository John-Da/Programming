import sys
import pygame




# //////////--------- ASSETS ------------////////////
bgImg = 'calculation/assets/img/bgg.png'
gameIcon = 'calculation/assets/img/bmlogo.png'

BLACK = '#000000'
RED = '#D10000'
GRAY = '#BEBEBE'
WHITE = '#FFFFFF'
PURPLE = '#823BF6'
ORANGE = '#FF5C00'
GREEN = '#228851'
BLUE = '#2690CC'
YELLOW = '#ABA406'
LIGHT_GREEN = '#00FD84'
DARK_RED = '#A24B4B'


REDHOVER = '#FF7D33'
GRAYHOVER = "#E1E1E1"

# newFont = 'calculation/assets/font/font.ttf'
fontOne = "calculation/assets/font/World Black Shadow.ttf"
fontTwo = "calculation/assets/font/Wall-Painter.ttf"
welFont = 75
strtFont = 58
menuFont = 88
optionFont = 40
extFont = 18
CURSOR = 'hand2'

ACTION_BTN_SIZE = 50
ACTION_BTN_RADIUS = 15
# ACTION_BTN_RADIUS = ACTION_BTN_SIZE // 2




# //////////--------- Game Screen ------------////////////



SCREEN_WIDTH = 1460
SCREEN_HEITH = 900
backGroundImg= pygame.image.load(bgImg)




class Button:
    def __init__(self, x, y, width, height, cornerRadius, text='', on_click=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = ORANGE
        self.text = text
        self.font = pygame.font.Font(fontTwo, strtFont)
        self.cornerRadius = cornerRadius
        self.on_click = on_click

    def on_rander(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=self.cornerRadius)
        if self.text:
            text_surf = self.font.render(self.text, True, WHITE)
            text_rect = text_surf.get_rect(center=self.rect.center)
            surface.blit(text_surf, text_rect)

    
    def check_click(self, position):
        if self.rect.collidepoint(position):
            if self.on_click:
                self.on_click()




class WelcomePage:
    def __init__(self):

        
        def on_button_click():
            print('Button clicked!')


        self.button = Button(680, 460, 160, 84, 15, 'START', on_click=on_button_click)



class Game:
    def __init__(self):
        self.gameRun = True
        pygame.init()
        
        self.resizedBG = pygame.transform.scale(backGroundImg, (SCREEN_WIDTH, SCREEN_HEITH))

        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEITH))
        pygame.display.set_caption('Basic Math')
        pygameIcon = pygame.image.load(gameIcon)
        pygame.display.set_icon(pygameIcon)
        self.clock = pygame.time.Clock()

        

    def runGame(self):
        while self.gameRun:
            self.screen.blit(self.resizedBG, (0,0))

            events = pygame.event.get()
            self.handle_events(events)
            self.button.on_rander(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()
            
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.button.check_click(event.pos)

    def quit(self):
        self.gameRun = False




if __name__ == "__main__":
    game = Game()
    game.runGame()