import pygame

pygame.init()


screen = pygame.display.set_mode((1200, 720))


runLoop = True
while runLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


pygame.display.update()