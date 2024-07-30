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
pixFont = "Helvetica"
welFont = 115
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

# |||||||||||| Draw Buttons ||||||||||||||
class Buttons:
    def __init__(self):
        ...
    
    def CircularShape(self):...


    def check_click(self):...



# ------== Retangular Shape Buttons ==---------

# |||||||||||| Start Button ||||||||||||||
class StartBtn(Buttons):
    def __init__(self):
        super().__init__()
    
    
# |||||||||||| play Button ||||||||||||||
class StartBtn(Buttons):
    def __init__(self):
        super().__init__()

# |||||||||||| resume Button ||||||||||||||
class StartBtn(Buttons):
    def __init__(self):
        super().__init__()

# |||||||||||| menu Button ||||||||||||||
class StartBtn(Buttons):
    def __init__(self):
        super().__init__()




# ------== Circular Shape Buttons ==---------
# |||||||||||| Exit Button ||||||||||||||
class StartBtn(Buttons):
    def __init__(self):
        super().__init__()

# |||||||||||| score Buttons ||||||||||||||
class StartBtn(Buttons):
    def __init__(self):
        super().__init__()

# |||||||||||| Back Button ||||||||||||||
class StartBtn(Buttons):
    def __init__(self):
        super().__init__()

# |||||||||||| Setting Button ||||||||||||||
class StartBtn(Buttons):
    def __init__(self):
        super().__init__()








# //////////--------- Run Function ------------////////////

def main():

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)



if __name__ == "__main__":
    main()