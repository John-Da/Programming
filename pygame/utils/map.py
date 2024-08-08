import sys
import pygame
import random


from buttons import Button

pygame.font.init()


class RandomMath:
    def __init__(self, screen, x, y):

        self.screen = screen
        self.first_num = random.randint(1, 11)
        self.sec_num = random.randint(1, 11)
        self.operation = {
            "add": "+",
            "subt": "-",
            "multi": "*",
            "divide": "/",
        }

        self.answer = self.first_num + self.sec_num

        self.posx = x
        self.posy = y

        self.main_font = pygame.font.SysFont("comicsans", 46)

    def showQuestion(self):
        question_label = self.main_font.render(
            f"{self.first_num} {self.operation['add']} {self.sec_num}",
            1,
            ((255, 255, 255)),
        )

        self.screen.blit(question_label, (self.posx // 2 - 40, self.posy))

    def showAnswers(self):

        ans_label = self.main_font.render(
            f"{self.first_num + self.sec_num}", 1, ((255, 255, 255))
        )

        self.screen.blit(ans_label, (self.posx // 2, self.posy // 2 + 300))

    def randomAns(self):
        randomNums = set()
        while len(randomNums) < 3:
            num = random.randint(0, 20)
            if num != self.realanswer:
                randomNums.add(num)
        randomNums.add(self.realanswer)

    def check_answer(self): ...


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Basic Math")
        self.screen = pygame.display.set_mode((640, 880))
        self.clock = pygame.time.Clock()

        self.screenWidth = self.screen.get_width()
        self.screenHeight = self.screen.get_height()

        self.score = 0
        self.lives = 5

        self.main_font = pygame.font.SysFont("comicsans", 36)

    def run(self):

        question = RandomMath(self.screen, self.screenWidth, 160)

        def redraw_screen():
            self.screen.fill((0, 0, 0))

            lives_label = self.main_font.render(
                f"Lives: {self.lives}", 1, (255, 255, 255)
            )
            score_label = self.main_font.render(
                f"Score: {self.score}", 1, ((255, 255, 255))
            )

            self.screen.blit(score_label, (50, 30))
            self.screen.blit(
                lives_label, (self.screenWidth - lives_label.get_width() - 50, 30)
            )

            question.showQuestion()
            question.showAnswers()

            pygame.display.update()

        while True:
            self.clock.tick(60)
            redraw_screen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    app = Game()
    app.run()
