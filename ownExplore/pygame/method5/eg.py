import pygame

def handle_button_click(is_clicked, button_name):
    if is_clicked:
        if button_name == "Start":
            print("Start")
        # Add more conditions for other buttons if needed
    else:
        pass  # No need to print anything when not clicked

class Button:
    def __init__(self, screen, name, width, height, x, y, btnFunction=None):

        self.fillColors = {
            "white": "#ffffff",
            "hover": "#666666",
            "pressed": "#333333",
            "black": "#000000",
            "blue": "#0AEFF7",
        }
        self.screen = screen
        self.name = name
        self.font = pygame.font.Font(None, 24)
        self.text = self.font.render(self.name, True, self.fillColors["black"])
        self.btn_width = width
        self.btn_height = height
        self.posx = x
        self.posy = y
        self.btnClick = btnFunction
        self.clicked = False

        self.btnSurface = pygame.Surface((self.btn_width, self.btn_height))
        self.btnRect = self.btnSurface.get_rect(center=(self.posx, self.posy))

        self.textSurface = self.text.get_rect(
            center=(self.btn_width // 2, self.btn_height // 2)
        )

        self.mouse = pygame.mouse.get_pos()


    def check_click(self, mouse_pos, mouse_press):
        pressed = self.btnRect.collidepoint(mouse_pos) and mouse_press[0]
        handle_button_click(pressed, self.name)
            


    def drawBtn(self):

        self.btnSurface.fill(self.fillColors["white"])

        if self.btnRect.collidepoint(self.mouse):
            self.btnSurface.fill(self.fillColors["hover"])
            self.text = self.font.render(self.name, True, self.fillColors["white"])
            if pygame.mouse.get_pressed()[0]:
                self.btnSurface.fill(self.fillColors["blue"])

        self.btnSurface.blit(self.text, self.textSurface)
        self.screen.blit(self.btnSurface, self.btnRect.topleft)

    


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    # Create multiple buttons
    start_button = Button(screen,"Start", 140, 40, 350, 180)
    pause_button = Button(screen,"End", 140, 40, 350, 260)
    resume_button = Button(screen,"Resume", 140, 40, 350, 380)

    buttons = [start_button, pause_button, resume_button]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    button.check_click(event.pos, pygame.mouse.get_pressed())

        screen.fill((0, 0, 0))
        for button in buttons:
            button.drawBtn()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()












# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# # Constants
# WIDTH, HEIGHT = 800, 600
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# BUTTON_COLOR = (100, 100, 250)
# HOVER_COLOR = (50, 50, 200)
# CLICK_COLOR = (0, 0, 150)
# BUTTON_WIDTH, BUTTON_HEIGHT = 200, 100

# # Create the screen object
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Animated Button")

# # Load button images if needed
# # For simplicity, let's just use colors for different states
# button_rect = pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 - BUTTON_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT))

# # Main loop
# running = True
# while running:
#     screen.fill(WHITE)
    
#     mouse_pos = pygame.mouse.get_pos()
#     mouse_pressed = pygame.mouse.get_pressed()

#     # Check for hover
#     if button_rect.collidepoint(mouse_pos):
#         if mouse_pressed[0]:  # Left mouse button pressed
#             pygame.draw.rect(screen, CLICK_COLOR, button_rect)
#         else:
#             pygame.draw.rect(screen, HOVER_COLOR, button_rect)
#     else:
#         pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
    
#     # Event handling
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1 and button_rect.collidepoint(mouse_pos):
#                 print("Button clicked!")
    
#     # Update the display
#     pygame.display.flip()

# # Quit Pygame
# pygame.quit()
# sys.exit()
