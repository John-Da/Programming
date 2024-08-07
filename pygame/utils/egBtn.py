# Imports
import sys
import pygame

# Configuration
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Arial', 40)

objects = []

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
        self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)


def myFunction():
    print('Button Pressed')

Button(30, 30, 400, 100, 'Button One (onePress)', myFunction)
Button(30, 140, 400, 100, 'Button Two (multiPress)', myFunction, True)

while True:
    screen.fill((20, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for object in objects:
        object.process()
    pygame.display.flip()
    fpsClock.tick(fps)







# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# clock = pygame.time.Clock()

# # Create a Pygame window
# window_size = (400, 400)
# screen = pygame.display.set_mode(window_size)
# pygame.display.set_caption("Pygame Clickable Button")

# # Create a font object
# font = pygame.font.Font(None, 24)

# # Create a surface for the button
# button_surface = pygame.Surface((150, 50))

# # Render text on the button
# text = font.render("Click Me", True, (0, 0, 0))
# text_rect = text.get_rect(
#     center=(button_surface.get_width() / 2, button_surface.get_height() / 2)
# )


# # Create a pygame.Rect object that represents the button's boundaries
# button_rect = pygame.Rect(125, 125, 150, 50)  # Adjust the position as needed

# # Start the main loop
# while True:
#     # Set the frame rate
#     clock.tick(60)

#     # Fill the display with color
#     screen.fill((155, 255, 155))

#     # Get events from the event queue
#     for event in pygame.event.get():
#         # Check for the quit event
#         if event.type == pygame.QUIT:
#             # Quit the game
#             pygame.quit()
#             sys.exit()

#         # Check for the mouse button down event
#         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#             # Call the on_mouse_button_down() function
#             if button_rect.collidepoint(event.pos):
#                 print("Button clicked!")

#     # Check if the mouse is over the button. This will create the button hover effect
#     if button_rect.collidepoint(pygame.mouse.get_pos()):
#         pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
#     else:
#         pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
#         pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
#         pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
#         pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)

#     # Shwo the button text
#     button_surface.blit(text, text_rect)

#     # Draw the button on the screen
#     screen.blit(button_surface, (button_rect.x, button_rect.y))

#     # Update the game state
#     pygame.display.update()
