import sys
import pygame



from utils.buttons import PlayBtn
from utils.filePath import load_img



class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Basic Math")
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

        self.screenWidth = self.screen.get_width()
        self.screenHeight = self.screen.get_height()



    def run(self):
        while True:
            self.screen.fill((14, 219, 248))

            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type== pygame.MOUSEBUTTONDOWN:
                    if self.screenWidth/2 <= mouse[0] <= self.screenWidth/2+140 and self.screenHeight/2 <= mouse[1] <= self.screenHeight/2+40:
                        print("Clicked")

            PlayBtn(self.screen).drawBtn()






            pygame.display.update()
            self.clock.tick(60)



Game().run()