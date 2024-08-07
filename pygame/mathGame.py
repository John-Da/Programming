import sys
import pygame


from utils.buttons import Button
from utils.map import btnFunction
from utils.filePath import load_img


class Game:
    def __init__(self, btnFunction=None):
        pygame.init()

        pygame.display.set_caption("Basic Math")
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

        self.screenWidth = self.screen.get_width()
        self.screenHeight = self.screen.get_height()

        self.btnFunction = btnFunction


    def run(self):
        while True:
            self.screen.fill((14, 219, 248))
            button = Button(self.screen, "Click", 140, 40, 350, 200, self.btnFunction)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                
            
            button.drawBtn()

            pygame.display.update()
            self.clock.tick(60)



if __name__ == "__main__":
    app = Game(btnFunction)
    app.run()
