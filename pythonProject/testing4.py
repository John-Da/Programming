import pygame

pygame.init()


screen = pygame.display.set_mode((800, 420))
pygame.display.set_caption("Math Speed Game")
clock = pygame.time.Clock()


# test_surface = pygame.Surface((100, 200))
# test_surface.fill('red')

bgSky = '../Programming/pythonProject/graphics/Sky.png'
bgGrd = '../Programming/pythonProject/graphics/ground.png'
gameFont = '../Programming/pythonProject/font/Pixeltype.ttf'
numbFont = ''


score_font = pygame.font.Font(gameFont, 40)
timer_font = pygame.font.Font(gameFont, 40)
numb_font = pygame.font.Font(numbFont, 40)


sky_surface = pygame.image.load(bgSky)
ground_surface = pygame.image.load(bgGrd)
score_surface = score_font.render('Score: ', False, 'black')
timer_surface = timer_font.render('Timer: ', False, 'black')


choice_operation = ('Addition', 'Subtraction','Multiplication', 'Division')


runLoop = True
while runLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(score_surface, (10, 10))
    screen.blit(timer_surface, (620, 10))

    pygame.display.update()
    clock.tick(60)