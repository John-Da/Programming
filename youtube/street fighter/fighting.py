import pygame
from charactor import Fighter


pygame.init()


game_name = "Brawler"
background = "/Users/yendahwa/Desktop/MyStuff/MyWorks/Programming/youtube/street fighter/assets/images/background/background.jpg"


screenWidth = 1000
screenHeight = 600


screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption(game_name)

clock = pygame.time.Clock()
FPS = 60

bg_image = pygame.image.load(background).convert_alpha()


def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (screenWidth, screenHeight))
    screen.blit(scaled_bg, (0, 0))


fighter_1 = Fighter(200, 310)
fighter_2 = Fighter(700, 310)

run = True
while run:

    clock.tick(FPS)

    draw_bg()
    fighter_1.move(screenWidth, screenHeight, screen, fighter_2)
    # fighter_2.move(screenWidth,screenHeight)
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()
