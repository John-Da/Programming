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
        self.score = 0
        self.lives = 5
        self.main_font = pygame.font.SysFont("comicsans", 36)
        self.question = RandomMath(self.screen, 140, 400)

    def run(self):
        def quitnow():
            pygame.quit()
            sys.exit()

        def redraw_screen():
            self.screen.fill((0, 0, 0))
            lives_label = self.main_font.render(f"Lives: {self.lives}", 1, (255, 255, 255))
            score_label = self.main_font.render(f"Score: {self.score}", 1, (255, 255, 255))

            self.screen.blit(score_label, (50, 30))
            self.screen.blit(lives_label, (self.screen.get_width() - lives_label.get_width() - 50, 30))

            if self.lives > 0:
                self.question.showQuestion()
                self.question.showAnswers()
            else:
                self.show_game_over()

            pygame.display.update()

        def show_game_over():
            game_over_label = self.main_font.render("Game Over!", 1, (255, 0, 0))
            play_again_btn = Button("Play Again", 200, 50, 220, 400)
            quit_btn = Button("Quit", 200, 50, 220, 470)

            self.screen.blit(game_over_label, (self.screen.get_width() // 2 - game_over_label.get_width() // 2, 350))
            play_again_btn.draw(self.screen)
            quit_btn.draw(self.screen)

            pos = pygame.mouse.get_pos()
            if play_again_btn.isOver(pos) and pygame.mouse.get_pressed()[0]:
                self.reset_game()
            elif quit_btn.isOver(pos) and pygame.mouse.get_pressed()[0]:
                quitnow()

        def reset_game():
            self.score = 0
            self.lives = 5
            self.question = RandomMath(self.screen, 140, 400)  # Create a new question instance

        while True:
            self.clock.tick(60)
            redraw_screen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitnow()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.lives > 0:  # Only check answers if the game is ongoing
                        if self.question.check_answer(pos):
                            self.score += 1
                            self.question.reset_question()
                        else:
                            self.lives -= 1

if __name__ == "__main__":
    app = Game()
    app.run()





















# import sys
# import pygame
# import random

# pygame.font.init()

# class RandomMath:
#     def __init__(self, screen, x, y):
#         self.screen = screen
#         self.first_num = random.randint(1, 11)
#         self.sec_num = random.randint(1, 11)
#         self.operation = {
#             "add": "+",
#             "subt": "-",
#             "multi": "*",
#             "divide": "/",
#         }

#         self.answer = self.first_num + self.sec_num  # Calculate the answer based on the operation
#         self.posx = x
#         self.posy = y
#         self.main_font = pygame.font.SysFont("comicsans", 46)

#         self.answers = self.randomAns()  # Generate answers once during initialization

#     def showQuestion(self):
#         question_label = self.main_font.render(
#             f"{self.first_num} {self.operation['add']} {self.sec_num}",
#             1,
#             ((255, 255, 255)),
#         )
#         self.screen.blit(question_label, (self.posx // 2 - 40, self.posy))

#     def randomAns(self):
#         randomNums = set()
#         while len(randomNums) < 3:  # Ensure we get 3 unique wrong answers
#             num = random.randint(0, 23)
#             if num != self.answer:
#                 randomNums.add(num)
#         randomNums.add(self.answer)  # Add the correct answer
#         return list(randomNums)  # Convert to list for easy access

#     def showAnswers(self):
#         setSide = 0
#         for ans in self.answers:  # Use the pre-generated answers
#             ans_label = self.main_font.render(f"{ans}", 1, ((255, 255, 255)))
#             self.screen.blit(ans_label, (120 + setSide, 400))
#             setSide += 80  # Increment position for the next answer

#     def check_answer(self): 
#         # Placeholder for checking the answer logic
#         pass


# class Game:
#     def __init__(self):
#         pygame.init()
#         pygame.display.set_caption("Basic Math")
#         self.screen = pygame.display.set_mode((640, 880))
#         self.clock = pygame.time.Clock()
#         self.screenWidth = self.screen.get_width()
#         self.screenHeight = self.screen.get_height()
#         self.score = 0
#         self.lives = 5

#         self.main_font = pygame.font.SysFont("comicsans", 36)

#     def run(self):
#         question = RandomMath(self.screen, self.screenWidth, 200)

#         def redraw_screen():
#             self.screen.fill((0, 0, 0))
#             lives_label = self.main_font.render(f"Lives: {self.lives}", 1, (255, 255, 255))
#             score_label = self.main_font.render(f"Score: {self.score}", 1, ((255, 255, 255)))

#             self.screen.blit(score_label, (50, 30))
#             self.screen.blit(lives_label, (self.screenWidth - lives_label.get_width() - 50, 30))

#             question.showQuestion()
#             question.showAnswers()

#             pygame.display.update()

#         while True:
#             self.clock.tick(60)
#             redraw_screen()

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()

# if __name__ == "__main__":
#     app = Game()
#     app.run()























# # import random

# # num1 = random.randint(1, 11)
# # num2 = random.randint(1, 11)
# # operation = {
# #             'add': '+',
# #             'subt': '-',
# #             'multi': '*',
# #             'divide': '/',
# #         }

# # if operation['add'] == '+':
# #     print(f"{num1} {operation['add']} {num2}: {num1+num2}")























# # # Imports
# # import sys
# # import pygame

# # # Configuration
# # pygame.init()
# # fps = 60
# # fpsClock = pygame.time.Clock()
# # width, height = 640, 480
# # screen = pygame.display.set_mode((width, height))

# # font = pygame.font.SysFont('Arial', 40)

# # objects = []

# # class Button():
# #     def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
# #         self.x = x
# #         self.y = y
# #         self.width = width
# #         self.height = height
# #         self.onclickFunction = onclickFunction
# #         self.onePress = onePress
# #         self.alreadyPressed = False

# #         self.fillColors = {
# #             'normal': '#ffffff',
# #             'hover': '#666666',
# #             'pressed': '#333333',
# #         }

# #         self.buttonSurface = pygame.Surface((self.width, self.height))
# #         self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

# #         self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

# #         objects.append(self)

# #     def process(self):
# #         mousePos = pygame.mouse.get_pos()
# #         self.buttonSurface.fill(self.fillColors['normal'])
# #         if self.buttonRect.collidepoint(mousePos):
# #             self.buttonSurface.fill(self.fillColors['hover'])
# #             if pygame.mouse.get_pressed(num_buttons=3)[0]:
# #                 self.buttonSurface.fill(self.fillColors['pressed'])
# #                 if self.onePress:
# #                     self.onclickFunction()
# #                 elif not self.alreadyPressed:
# #                     self.onclickFunction()
# #                     self.alreadyPressed = True
# #             else:
# #                 self.alreadyPressed = False

# #         self.buttonSurface.blit(self.buttonSurf, [
# #         self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
# #             self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
# #         ])
# #         screen.blit(self.buttonSurface, self.buttonRect)


# # def myFunction():
# #     print('Button Pressed')

# # Button(30, 30, 400, 100, 'Button One (onePress)', myFunction)
# # Button(30, 140, 400, 100, 'Button Two (multiPress)', myFunction, True)

# # while True:
# #     screen.fill((20, 20, 20))
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             pygame.quit()
# #             sys.exit()
# #     for object in objects:
# #         object.process()
# #     pygame.display.flip()
# #     fpsClock.tick(fps)







# # # import pygame
# # # import sys

# # # # Initialize Pygame
# # # pygame.init()

# # # clock = pygame.time.Clock()

# # # # Create a Pygame window
# # # window_size = (400, 400)
# # # screen = pygame.display.set_mode(window_size)
# # # pygame.display.set_caption("Pygame Clickable Button")

# # # # Create a font object
# # # font = pygame.font.Font(None, 24)

# # # # Create a surface for the button
# # # button_surface = pygame.Surface((150, 50))

# # # # Render text on the button
# # # text = font.render("Click Me", True, (0, 0, 0))
# # # text_rect = text.get_rect(
# # #     center=(button_surface.get_width() / 2, button_surface.get_height() / 2)
# # # )


# # # # Create a pygame.Rect object that represents the button's boundaries
# # # button_rect = pygame.Rect(125, 125, 150, 50)  # Adjust the position as needed

# # # # Start the main loop
# # # while True:
# # #     # Set the frame rate
# # #     clock.tick(60)

# # #     # Fill the display with color
# # #     screen.fill((155, 255, 155))

# # #     # Get events from the event queue
# # #     for event in pygame.event.get():
# # #         # Check for the quit event
# # #         if event.type == pygame.QUIT:
# # #             # Quit the game
# # #             pygame.quit()
# # #             sys.exit()

# # #         # Check for the mouse button down event
# # #         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
# # #             # Call the on_mouse_button_down() function
# # #             if button_rect.collidepoint(event.pos):
# # #                 print("Button clicked!")

# # #     # Check if the mouse is over the button. This will create the button hover effect
# # #     if button_rect.collidepoint(pygame.mouse.get_pos()):
# # #         pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
# # #     else:
# # #         pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
# # #         pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
# # #         pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
# # #         pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)

# # #     # Shwo the button text
# # #     button_surface.blit(text, text_rect)

# # #     # Draw the button on the screen
# # #     screen.blit(button_surface, (button_rect.x, button_rect.y))

# # #     # Update the game state
# # #     pygame.display.update()
