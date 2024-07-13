import pygame, sys
import btn


pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

btnWidth = 100
btnHeight = 40
btnElevation =6


btnPosX = 208
btnPosY = 280

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Method 2')
clock = pygame.time.Clock()


screenFill = '#DCDDD8'
gFont = pygame.font.Font(None, 30)


button1 = btn.Button('Click me', btnWidth, btnHeight, (btnPosX, btnPosY), gFont, btnElevation)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(screenFill)
    button1.draw(screen)

    pygame.display.update()
    clock.tick(60)








