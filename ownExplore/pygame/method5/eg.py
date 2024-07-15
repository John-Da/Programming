import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 100, 250)
HOVER_COLOR = (50, 50, 200)
CLICK_COLOR = (0, 0, 150)
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 100

# Create the screen object
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Button")

# Load button images if needed
# For simplicity, let's just use colors for different states
button_rect = pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 - BUTTON_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT))

# Main loop
running = True
while running:
    screen.fill(WHITE)
    
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    # Check for hover
    if button_rect.collidepoint(mouse_pos):
        if mouse_pressed[0]:  # Left mouse button pressed
            pygame.draw.rect(screen, CLICK_COLOR, button_rect)
        else:
            pygame.draw.rect(screen, HOVER_COLOR, button_rect)
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and button_rect.collidepoint(mouse_pos):
                print("Button clicked!")
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
