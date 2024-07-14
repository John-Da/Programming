import pygame,sys
import filePath, btnStyle
import countdown


pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 840


# --------- Sizing, Position -----------------
btnElevation = 6

startWidth = 100; startHeight = 40; startPosX = 208; startPosY = 280
addWidth = 140; addHeight = 50; addPosX = 268; addPosY = 125
subtWidth = 140; subtHeight = 50; subtPosX = 297; subtPosY = 250
multWidth = 140; multHeight = 50; multPosX = 336; multPosY = 375
diviWidth = 140; diviHeight = 50; diviPosX = 356; diviPosY = 420
menuWidth = 140; menuHeight = 50; menuPosX = 208; menuPosY = 460
quitWidth = 140; quitHeight = 50; quitPosX = 380; quitPosY = 490
playWidth = 140; playHeight = 50; playPosX = 208; playPosY = 280
resumeWidth = 140; resumeHeight = 50; resumePosX = 208; resumePosY = 280


introTitleX = 100; introTitleY = 40
menuTitleX = 130; menuTitleY = 20
discriptionX = 60; discriptionY = 100


# --------- Colors, Font, Background, Audio -----------------
screenFill = '#DCDDD8'
whiteColor = '#FFFFFF'
text_col = (255, 255, 255)

titleFontSize = 40
btnFontSize = 30
menuFontSize = 40
gameDiscriptionSize = 20

titleFont = pygame.font.Font(None, titleFontSize)
menuFont = pygame.font.Font(None, menuFontSize)
btnFont = pygame.font.Font(None, btnFontSize)
discriptionFont = pygame.font.Font(None, gameDiscriptionSize)

# bgImg = filePath.bgImg


# --------- Pygame Display -----------------
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Math Game")
clock = pygame.time.Clock()


# --------- Buttons -----------------
startBtn = btnStyle.Button("Play", startWidth, startHeight, (startPosX, startPosY), btnFont, btnElevation)

addBtn = btnStyle.Button("Addition", addWidth, addHeight, (addPosX, addPosY), btnFont, btnElevation)
subtBtn = btnStyle.Button("Subtraction", subtWidth, subtHeight, (subtPosX, subtPosY), btnFont, btnElevation)
multBtn = btnStyle.Button("Muliplication", multWidth, multHeight, (multPosX, multPosY), btnFont, btnElevation)
diviBtn = btnStyle.Button("Division", diviWidth, diviHeight, (diviPosX, diviPosY), btnFont, btnElevation)

menuBtn = btnStyle.Button("Menu", menuWidth, menuHeight, (menuPosX, menuPosY), btnFont, btnElevation)

quitBtn = btnStyle.Button("Quit", quitWidth, quitHeight, (quitPosX, quitPosY), btnFont, btnElevation)

playBtn = btnStyle.Button("Play Again", playWidth, playHeight, (playPosX, playPosY), btnFont, btnElevation)

resumeBtn = btnStyle.Button("Resume", resumeWidth, resumeHeight, (resumePosX, resumePosY), btnFont, btnElevation)



# --------- Game Loop -----------------
menu_state = "main"
delayTime = 1
showMenu = False
run = True


def gameLoading():
    pass


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))


def toMenu():
    while run:
        screen.fill(screenFill)
        draw_text("What do you want to play?", menuFont, text_col, 160, 200)
        addBtn.draw(screen)
        subtBtn.draw(screen)
        multBtn.draw(screen)
        diviBtn.draw(screen)
        quitBtn.draw(screen)

    


def main():
    screen.fill('gray')
    global showMenu
    while run:
        screen.fill(screenFill)
        draw_text("Welcome to Math Game", titleFont, text_col, introTitleX, introTitleY)

        with open(filePath.gameLines, 'r') as script:
            lines = script.read()
        draw_text(lines, discriptionFont, text_col, discriptionX, discriptionY)

        if not showMenu:
            startBtn.draw(screen)
            if startBtn.pressed:
                countdown.countdown(delayTime)
                showMenu = True
            else:
                showMenu = False
        else:
            # toMenu()
            addBtn.draw(screen)
            subtBtn.draw(screen)
            multBtn.draw(screen)
            diviBtn.draw(screen)
            quitBtn.draw(screen)
            if quitBtn.pressed:
                countdown.countdown(delayTime)
                pygame.quit()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()    

        pygame.display.update()
        clock.tick(60)



