import pygame

from image_store import bgSky, bgGrd, gameFont1, snail1,playWalk1

pygame.init()


screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Math Speed Game")
clock = pygame.time.Clock()


# test_surface = pygame.Surface((100, 200))
# test_surface.fill('red')


score_font = pygame.font.Font(gameFont1, 40)
timer_font = pygame.font.Font(gameFont1, 40)

score_surface = score_font.render('Score: ', False, 'black')
timer_surface = timer_font.render('Timer: ', False, 'black')

sky_surface = pygame.image.load(bgSky).convert()
ground_surface = pygame.image.load(bgGrd).convert()

snail_posX = 600
snail_posY = 300
snail_surface = pygame.image.load(snail1).convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (snail_posX, snail_posY))


player_surface = pygame.image.load(playWalk1).convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))




runLoop = True
while runLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))

    screen.blit(score_surface, (15, 10))
    screen.blit(timer_surface, (620, 10))

    snail_rect.x -= 2
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)

    pygame.display.update()
    clock.tick(60)