import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up colors
WHITE = (255, 255, 255)

# Ball properties
x_coord = screen_width // 2
y_coord = screen_height // 2
velocity_x = round(random.random() / 10, 2)
velocity_y = round(random.random() / 10, 2)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ball position
    x_coord += velocity_x
    y_coord += velocity_y

    # Check for collisions with walls
    if y_coord + velocity_y >= screen_height or y_coord + velocity_y <= 0:
        velocity_y = -velocity_y

    if x_coord + velocity_x >= screen_width:
        print("Player 1 has won the game.")
        running = False
    elif x_coord + velocity_x <= 0:
        print("Player 2 has won the game.")
        running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(screen, (0, 0, 0), (int(x_coord), int(y_coord)), 5)

    # Update the display
    pygame.display.flip()

    # Delay for smooth animation
    pygame.time.delay(100)

# Quit Pygame
pygame.quit()
