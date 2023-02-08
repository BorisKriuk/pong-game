import pygame
from variables import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR, WHITE, MARGIN, FPS
from paddle_class import Paddle
from ball_class import Ball

pygame.init()

fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong 1.0")
font = pygame.font.SysFont("Constantia", 30)

# define game variables
live_ball = False
cpu_score = 0
player_score = 0
winner = 0
speed_increase = 0


def draw_board():
    screen.fill(BG_COLOR)
    pygame.draw.line(screen, WHITE, (0, MARGIN), (SCREEN_WIDTH, MARGIN), 4)


def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))


# create paddles
player_paddle = Paddle(SCREEN_WIDTH-40, SCREEN_HEIGHT // 2, screen)
cpu_paddle = Paddle(20, SCREEN_HEIGHT // 2, screen)

# create pong ball
pong = Ball(SCREEN_WIDTH-60, SCREEN_HEIGHT // 2 + 50, screen)

running = True
while running:

    fpsClock.tick(FPS)

    draw_board()
    draw_text("CPU: " + str(cpu_score), font, WHITE, 20, 15)
    draw_text("P1: " + str(player_score), font, WHITE, SCREEN_WIDTH-100, 15)
    draw_text("BALL SPEED: " + str(abs(pong.speed_x)), font, WHITE, SCREEN_WIDTH // 2-100, 15)

    # draw paddles
    player_paddle.draw()
    cpu_paddle.draw()

    if live_ball:
        speed_increase += 1
        # move ball
        winner = pong.move(player_paddle, cpu_paddle)
        if winner == 0:
            # move player paddle
            player_paddle.move()
            cpu_paddle.ai(pong)

            # draw ball
            pong.draw()
        else:
            live_ball = False
            if winner == 1:
                player_score += 1
            elif winner == (-1):
                cpu_score += 1

    # print player instructions

    if live_ball == False:
        if winner == 0:
            draw_text("click anywhere to start", font, WHITE, 170, SCREEN_HEIGHT // 2 - 100)
        if winner == 1:
            draw_text("click anywhere to start", font, WHITE, 170, SCREEN_HEIGHT // 2 - 100)
            draw_text("you scored", font, WHITE, 230, SCREEN_HEIGHT // 2 - 180)
        if winner == -1:
            draw_text("click anywhere to start", font, WHITE, 170, SCREEN_HEIGHT // 2 - 100)
            draw_text("computer scored", font, WHITE, 210, SCREEN_HEIGHT // 2 - 180)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not live_ball:
            live_ball = True
            pong.reset(SCREEN_WIDTH-60, SCREEN_HEIGHT // 2 + 50, screen)

    if speed_increase > 500:
        speed_increase = 0
        if pong.speed_x < 0:
            pong.speed_x -= 1
        if pong.speed_x > 0:
            pong.speed_x += 1
        if pong.speed_y < 0:
            pong.speed_y -= 1
        if pong.speed_y > 0:
            pong.speed_y += 1

    pygame.display.update()

pygame.quit()
