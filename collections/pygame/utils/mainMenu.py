import pygame


from mathGame import Game
# from utils.map import btnFunction


class Menu(Game):
    def __init__(self, btnFunction=None):
        super().__init__(btnFunction)
        self.btnFunction = btnFunction

    def runmenu(screen):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            screen.fill((134, 234, 54))
            pygame.display.update()
