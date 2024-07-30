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

pygame.init()
SCREEN_WIDTH = 1460
SCREEN_HEITH = 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEITH))
pygame.display.set_caption('Basic Math')
pygameIcon = pygame.image.load(gameIcon)
pygame.display.set_icon(pygameIcon)
clock = pygame.time.Clock()



# //////////--------- Game Function ------------////////////

def roundedRect(surface, color, rect, cornerRadius):
    pygame.draw.rect(surface, color, rect, border_radius=cornerRadius)

class StartButton:
    def __init__(self, screen, text, x, y, width, height, font_size=strtFont, bgColor=ORANGE, textColor=WHITE, padding=10, radius=15):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.width = width + 2 * padding
        self.height = height + 2 * padding
        self.fontSize = font_size
        self.bgColor =  bgColor
        self.textColor = textColor
        self.borderRadius = radius
        self.padding = padding

        self.font = pygame.font.Font(fontTwo, self.fontSize)
        self.textSurface = self.font.render(self.text, True, WHITE)

        self.strtRect = pygame.Rect(self.x, self.y, self.width + 2 * self.padding, self.height + 2 * self.padding)
        self.strtRect = self.textSurface.get_rect(center=self.strtRect.center)


    def draw(self):
        roundedRect(self.screen, self.bgColor, self.strtRect, self.borderRadius)
        self.screen.blit(self.textSurface, self.strtRect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            return self.strtRect.collidedict(mouse_pos)
        return False




class WelcomePage:
    def __init__(self, screen, text='Welcome to Basic Game', fontSize=welFont, pady=80):
        self.screen = screen
        self.text = text
        self.fontSize = fontSize
        self.pady = pady
        self.font = pygame.font.Font(fontOne, self.fontSize)
        self.textSurface = self.font.render(self.text, True, WHITE)
        self.textRect = self.textSurface.get_rect(center=(screen.get_width() // 2, self.pady + self.textSurface.get_height() // 2))

        button_width = 200
        button_height = 80
        button_x = screen.get_width() // 2 - button_width // 2 
        button_y = screen.get_height() // 2 - button_height // 2 + 50
        self.playButton = StartButton(screen, "Play", button_x, button_y, button_width, button_height, padding=10, radius=15)

    def draw(self):
        self.screen.blit(self.textSurface, self.textRect)
        self.playButton.draw()







# //////////--------- Run Function ------------////////////

def main():
    starPage = WelcomePage(screen)
    backGroundImg= pygame.image.load(bgImg)
    resizedBG = pygame.transform.scale(backGroundImg, (SCREEN_WIDTH, SCREEN_HEITH))

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if starPage.playButton.is_clicked(event):
                print("Play button clicked!")
        


        
        screen.blit(resizedBG, (0,0))
        starPage.draw()

        pygame.display.flip()
        clock.tick(60)



if __name__ == "__main__":
    main()