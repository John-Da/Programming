import pygame,sys
import filePath, btnStyle
import countdown


pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 840


# --------- Sizing, Position -----------------
btnElevation = 6

startWidth = 100; startHeight = 40; startPosX = 205; startPosY = 280

addWidth = 140; addHeight = 50; addPosX = 205; addPosY = 250
subtWidth = 140; subtHeight = 50; subtPosX = 205; subtPosY = 313
multWidth = 140; multHeight = 50; multPosX = 205; multPosY = 374
diviWidth = 140; diviHeight = 50; diviPosX = 205; diviPosY = 437
quitWidth = 140; quitHeight = 50; quitPosX = 205; quitPosY = 498

playWidth = 140; playHeight = 50; playPosX = 208; playPosY = 280
resumeWidth = 140; resumeHeight = 50; resumePosX = 208; resumePosY = 280
menuWidth = 140; menuHeight = 50; menuPosX = 208; menuPosY = 208


introTitleX = 100; introTitleY = 40
menuTitleX = 130; menuTitleY = 20
discriptionX = 60; discriptionY = 100


# --------- Colors, Font, Background, Audio -----------------
screenFill = '#DCDDD8'
whiteColor = '#FFFFFF'
text_col = (255, 255, 255)
bgColor = "#3d6466"
darkerCol = "#28393a"
badeeCol = "#badee2"

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
startBtn = btnStyle.Button("Play", startWidth, startHeight, (startPosX, startPosY), btnFont, btnElevation, "play")

addBtn = btnStyle.Button("Addition", addWidth, addHeight, (addPosX, addPosY), btnFont, btnElevation, "addition")
subtBtn = btnStyle.Button("Subtraction", subtWidth, subtHeight, (subtPosX, subtPosY), btnFont, btnElevation, "subtraction")
multBtn = btnStyle.Button("Muliplication", multWidth, multHeight, (multPosX, multPosY), btnFont, btnElevation, "muliplication")
diviBtn = btnStyle.Button("Division", diviWidth, diviHeight, (diviPosX, diviPosY), btnFont, btnElevation, "division")

menuBtn = btnStyle.Button("Menu", menuWidth, menuHeight, (menuPosX, menuPosY), btnFont, btnElevation, "menu")

quitBtn = btnStyle.Button("Quit", quitWidth, quitHeight, (quitPosX, quitPosY), btnFont, btnElevation, "quit")

playBtn = btnStyle.Button("Play Again", playWidth, playHeight, (playPosX, playPosY), btnFont, btnElevation, "again")

resumeBtn = btnStyle.Button("Resume", resumeWidth, resumeHeight, (resumePosX, resumePosY), btnFont, btnElevation, "resume")



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
        screen.fill(bgColor)
        draw_text("Main Menu", titleFont, text_col, introTitleX, introTitleY)
        if addBtn.draw(screen):
            print("Added")
        if subtBtn.draw(screen):
            print("Subtracted")
        if multBtn.draw(screen):
            print("Multiply")
        if diviBtn.draw(screen):
            print("Divided")
        if quitBtn.draw(screen):
            print("Quit")

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()    

    pygame.display.update()
    clock.tick(60)

    


def main():
    global showMenu
    while run:
        screen.fill(bgColor)
        # mouse_pos = pygame.mouse.get_pressed()

        if not showMenu:
            draw_text("Welcome to Math Game", titleFont, text_col, introTitleX, introTitleY)

            with open(filePath.gameLines, 'r') as script:
                lines = script.read()
            draw_text(lines, discriptionFont, text_col, discriptionX, discriptionY)
            
            startBtn.draw(screen)
            if startBtn.pressed:
                countdown.countdown(delayTime)
                showMenu = True
            else:
                showMenu = False
        else:
            draw_text("Main Menu", titleFont, text_col, introTitleX, introTitleY)
            addBtn.draw(screen)
            subtBtn.draw(screen)
            multBtn.draw(screen)
            diviBtn.draw(screen)
            quitBtn.draw(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()    

        pygame.display.update()
        clock.tick(60)



