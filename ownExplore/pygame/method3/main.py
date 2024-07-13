import pygame
import btn

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

game_paused = False
menu_state = "main"

gFont = pygame.font.SysFont('arialblack', 40)
text_col = (255, 255, 255)

resume_img = pygame.image.load('').convert_alpha()
option_img = pygame.image.load('').convert_alpha()
quit_img = pygame.image.load('').convert_alpha()


resume_btn = btn.Button(304, 125, resume_img, 1)
option_btn = btn.Button(297, 250, option_img, 1)
quit_btn = btn.Button(336, 375, quit_img, 1)
back_btn = btn.Button(336, 375, quit_img, 1)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))


run = True
while run:
    screen.fill((52, 78, 91))

    if game_paused == True:
        if menu_state == "main":
            if resume_btn.draw(screen):
                game_paused = False
            if option_btn.draw(screen):
                menu_state = "options"
            if quit_btn.draw(screen):
                run = False
        if menu_state == "options":
            if resume_btn.draw(screen):
                game_paused = False
            if option_btn.draw(screen):
                menu_state = "options"
            if quit_btn.draw(screen):
                run = False
            if back_btn.draw(screen):
                menu_state = "main"
    else:
        draw_text("Press SPACE to PAUSE", gFont, text_col, 160, 200)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()