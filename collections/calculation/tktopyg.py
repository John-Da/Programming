import pygame
import sys

# //////////--------- ASSETS ------------////////////
bgImg = 'calculation/assets/img/bgg.png'

BLACK = (0, 0, 0)
RED = (209, 0, 0)
GRAY = (190, 190, 190)
WHITE = (255, 255, 255)
PURPLE = (130, 59, 246)
ORANGE = (255, 92, 0)
GREEN = (34, 136, 81)
BLUE = (38, 144, 204)
YELLOW = (171, 164, 6)
LIGHT_GREEN = (0, 253, 132)
DARK_RED = (162, 75, 75)

REDHOVER = (255, 125, 51)
GRAYHOVER = (225, 225, 225)

pixFont = 'Helvetica'
welFont = 115
strtFont = 58
menuFont = 88
optionFont = 40
extFont = 18
CURSOR = 'hand2'

ACTION_BTN_SIZE = 50
ACTION_BTN_RADIUS = 15

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 920))
pygame.display.set_caption('Basic Math')

# Load and scale background image
bg_image = pygame.image.load(bgImg)
bg_image = pygame.transform.scale(bg_image, (1280, 920))

def draw_text(surface, text, font, color, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

def welcome_page():
    font_welcome = pygame.font.SysFont(pixFont, welFont)
    font_start = pygame.font.SysFont(pixFont, strtFont)
    font_ext = pygame.font.SysFont(pixFont, extFont)
    
    while True:
        screen.blit(bg_image, (0, 0))
        draw_text(screen, 'Welcome to Basic Math', font_welcome, WHITE, 990, 192)
        
        pygame.draw.rect(screen, ORANGE, (865, 564, 250, 105))
        draw_text(screen, 'START', font_start, BLACK, 990, 617)
        
        pygame.draw.rect(screen, GRAY, (1860, 930, ACTION_BTN_SIZE, ACTION_BTN_SIZE))
        draw_text(screen, 'Q', font_ext, BLACK, 1860 + ACTION_BTN_SIZE // 2, 930 + ACTION_BTN_SIZE // 2)
        
        pygame.draw.rect(screen, GRAY, (1920, 930, ACTION_BTN_SIZE, ACTION_BTN_SIZE))
        draw_text(screen, 's', font_ext, BLACK, 1920 + ACTION_BTN_SIZE // 2, 930 + ACTION_BTN_SIZE // 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 865 < event.pos[0] < 1115 and 564 < event.pos[1] < 669:
                    menu_page()  # Switch to menu page
        
        pygame.display.flip()

def menu_page():
    font_menu = pygame.font.SysFont(pixFont, menuFont)
    
    while True:
        screen.blit(bg_image, (0, 0))
        draw_text(screen, 'Which one do you like to play?', font_menu, WHITE, 990, 192)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()

def main():
    welcome_page()

if __name__ == "__main__":
    main()
