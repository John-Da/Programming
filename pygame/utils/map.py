import sys
import pygame
import random


pygame.font.init()


class Button:
    def __init__(self, text, width, height, x, y):
        self.name = text
        self.btnRect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont("comicsans", 36)
        self.fillColors = {
            "white": "#ffffff",
            "hover": "#666666",
            "pressed": "#333333",
            "black": "#000000",
            "blue": "#0AEFF7",
        }

    def draw(self, screen):
        pygame.draw.rect(screen, self.fillColors["blue"], self.btnRect)
        text_surface = self.font.render(self.name, True, self.fillColors['black'])
        text_x = self.btnRect.x + (self.btnRect.width - text_surface.get_width()) // 2
        text_y = self.btnRect.y + (self.btnRect.height - text_surface.get_height()) // 2
        screen.blit(text_surface, (int(text_x), int(text_y)))

    def isOver(self, pos):
        return self.btnRect.collidepoint(pos)


class RandomMath:
    def __init__(self, screen, x, y):

        self.screen = screen
        self.first_num = random.randint(1, 11)
        self.sec_num = random.randint(1, 11)

        self.answer = self.first_num + self.sec_num

        self.posx = x
        self.posy = y

        self.main_font = pygame.font.SysFont("comicsans", 46)

        self.randomAnswers = self.randomAns()
        self.buttons = self.create_buttons()

    def showQuestion(self):
        question_label = self.main_font.render(
            f"{self.first_num} + {self.sec_num}",
            1,
            ((255, 255, 255)),
        )

        self.screen.blit(question_label, (self.posx // 2 - 40, self.posy))

    def randomAns(self):
        randomNums = set()
        while len(randomNums) < 3:
            num = random.randint(0, 23)
            if num != self.answer:
                randomNums.add(num)
        randomNums.add(self.answer)
        return list(randomNums)

    def create_buttons(self):
        buttons = []
        setSide = 0
        for ans in self.randomAnswers:
            btn_label = Button(str(ans), 80, 50, 120 + setSide, 400)
            buttons.append(btn_label)
            setSide += 100
        return buttons

    def showAnswers(self):
        for button in self.buttons:
            button.draw(self.screen)

    def check_answer(self, pos):
        for button in self.buttons:
            if button.isOver(pos):
                return button.name == str(self.answer)
        return False

    def reset_question(self):
        self.__init__(self.screen, self.posx, self.posy)


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
        self.question = RandomMath(self.screen, self.screenWidth, 160)
        self.gameOver = self.show_game_over()

        

    def run(self):

        def quitnow():
            pygame.quit()
            sys.exit()

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

            if self.lives > 0:
                self.question.showQuestion()
                self.question.showAnswers()
            else:
                self.show_game_over()

            pygame.display.update()

    

        while True:
            self.clock.tick(60)
            redraw_screen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitnow()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.lives > 0:
                        if self.question.check_answer(pos):
                            self.score += 1
                            self.question.reset_question()
                        else:
                            self.question.reset_question()
                            self.lives -= 1

                            
    def show_game_over(self):
            game_over_label = self.main_font.render("Game Over!", 1, (255, 0, 0))
            play_again_btn = Button("Play Again", 200, 50, 220, 400)
            quit_btn = Button("Quit", 200, 50, 220, 470)

            self.screen.blit(
                game_over_label,
                (self.screen.get_width() // 2 - game_over_label.get_width() // 2, 350),
            )

            play_again_btn.draw(self.screen)
            quit_btn.draw(self.screen)

            pos = pygame.mouse.get_pos()
            if play_again_btn.isOver(pos) and pygame.mouse.get_pressed()[0]:
                self.reset_game()
            elif quit_btn.isOver(pos) and pygame.mouse.get_pressed()[0]:
                self.quitnow()

    def reset_game(self):
        self.score = 0
        self.lives = 5
        self.question = RandomMath(self.screen, self.screenWidth, 160)

if __name__ == "__main__":
    app = Game()
    app.run()
