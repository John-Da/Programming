import sys
import pygame


from utils.buttons import Button


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

            button1 = Button(self.screen, "Click", 140, 40, 350, 180)
            button2 = Button(self.screen, "Button", 140, 40, 350, 380)

            buttons = [button1, button2]

            mousepress = pygame.mouse.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons:
                        button.is_clicked(event.pos, mousepress)

            for button in buttons:
                button.drawBtn()

            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    app = Game()
    app.run()
