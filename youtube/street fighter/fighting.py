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


RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
bg_image = pygame.image.load(background).convert_alpha()


def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (screenWidth, screenHeight))
    screen.blit(scaled_bg, (0, 0))


def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2 , 404, 34))
    pygame.draw.rect(screen, RED,(x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))


fighter_1 = Fighter(200, 310)
fighter_2 = Fighter(700, 310)

run = True
while run:

    clock.tick(FPS)

    draw_bg()
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)


    fighter_1.move(screenWidth, screenHeight, screen, fighter_2)
    # fighter_2.move(screenWidth,screenHeight)
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()
