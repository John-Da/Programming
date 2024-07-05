import pygame

pygame.init()


screen = pygame.display.set_mode((1200, 720))
pygame.display.set_caption("Math Speed Game")
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 200))
test_surface.fill('red')

runLoop = True
while runLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface, (200,100))

    pygame.display.update()
    clock.tick(60)