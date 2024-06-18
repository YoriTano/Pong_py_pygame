import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up colors
WHITE = (255, 255, 255)

# Paddle properties
paddle_width = 10
paddle_height = 60
paddle_speed = 5

# Initial positions of paddles
p1_pdl_y = screen_height // 2 - paddle_height // 2
p2_pdl_y = screen_height // 2 - paddle_height // 2

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Handle keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1_pdl_y -= paddle_speed
    if keys[pygame.K_s]:
        p1_pdl_y += paddle_speed
    if keys[pygame.K_u]:
        p2_pdl_y -= paddle_speed
    if keys[pygame.K_j]:
        p2_pdl_y += paddle_speed

    # Ensure paddles stay within bounds
    p1_pdl_y = max(0, min(p1_pdl_y, screen_height - paddle_height))
    p2_pdl_y = max(0, min(p2_pdl_y, screen_height - paddle_height))

    # Draw paddles
    pygame.draw.rect(screen, (0, 0, 0), (0, p1_pdl_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, (0, 0, 0), (screen_width - paddle_width, p2_pdl_y, paddle_width, paddle_height))

    # Update the display
    pygame.display.flip()

    # Delay for smooth animation
    pygame.time.delay(10)

# Quit Pygame
pygame.quit()
sys.exit()
