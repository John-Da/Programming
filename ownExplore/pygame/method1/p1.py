import pygame
import btn

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PyGame')

sImg = "../pygame/snail1.png"
eImg = "../pygame/jump.png"

start_img = pygame.image.load(sImg).convert_alpha()
exit_img = pygame.image.load(eImg).convert_alpha()

start_btn = btn.Button(100, 200, start_img, 0.8)
exit_btn = btn.Button(450, 200, exit_img, 0.8)

run = True
while run:

    screen.fill((202, 228, 241))
    if start_btn.draw(screen):
        pass

    if exit_btn.draw(screen):
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            run = False
    

    pygame.display.update()
pygame.quit()
