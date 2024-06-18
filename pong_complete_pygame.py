import math
import random 
import pygame
import stdio
import sys

def pong_input(p1_pdl_y, p2_pdl_y):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1_pdl_y -= 0.1
    if keys[pygame.K_s]:
        p1_pdl_y += 0.1
    if keys[pygame.K_u]:
        p2_pdl_y -= 0.1
    if keys[pygame.K_j]:
        p2_pdl_y += 0.1
    return p1_pdl_y, p2_pdl_y

def boundaries(x_coord, y_coord, velocity_x, velocity_y, p1_pdl_y, p2_pdl_y):
    if (y_coord + velocity_y) >= 1 or (y_coord + velocity_y) <= 0:
        velocity_y = -velocity_y

    if (x_coord + velocity_x) < 0.1 and (p1_pdl_y <= y_coord <= p1_pdl_y + 0.5):
        velocity_x = -velocity_x
    elif (x_coord + velocity_x) > 0.9 and (p2_pdl_y <= y_coord <= p2_pdl_y + 0.5):
        velocity_x = -velocity_x
    elif (x_coord + velocity_x) >= 1:
        print("Player 1 has won the game.")
        pygame.quit()
        sys.exit()
    elif (x_coord + velocity_x) <= 0:
        print("Player 2 has won the game.")
        pygame.quit()
        sys.exit()

    return velocity_x, velocity_y

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    clock = pygame.time.Clock()

    p1_pdl_x = 0.05
    p1_pdl_y = 0.2
    p1_pdl_w = 0.05
    p1_pdl_h = 0.5
    p2_pdl_x = 0.90
    p2_pdl_y = 0.2
    p2_pdl_w = 0.05
    p2_pdl_h = 0.5
    ball_x = 0.4
    ball_y = 0.5
    velocity_x = random.uniform(-0.03, 0.03)
    velocity_y = random.uniform(-0.03, 0.03)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        p1_pdl_y, p2_pdl_y = pong_input(p1_pdl_y, p2_pdl_y)
        velocity_x, velocity_y = boundaries(ball_x, ball_y, velocity_x, velocity_y, p1_pdl_y, p2_pdl_y)
        ball_x += velocity_x
        ball_y += velocity_y

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (255, 255, 255), (p1_pdl_x * 1000, p1_pdl_y * 600, p1_pdl_w * 1000, p1_pdl_h * 600))
        pygame.draw.rect(screen, (255, 255, 255), (p2_pdl_x * 1000, p2_pdl_y * 600, p2_pdl_w * 1000, p2_pdl_h * 600))
        pygame.draw.circle(screen, (255, 255, 255), (int(ball_x * 1000), int(ball_y * 600)), 10)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()