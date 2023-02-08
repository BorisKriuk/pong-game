import pygame
from variables import MARGIN, SCREEN_HEIGHT, SCREEN_WIDTH, WHITE


class Ball:
    def __init__(self, x, y, screen):
        self.reset(x, y, screen)

    def move(self, player_paddle, cpu_paddle):

        # add collision detection
        # check for collision with top margin
        if self.rect.top < MARGIN:
            self.speed_y *= (-1)

        # check for collision with bottom of the screen
        elif self.rect.bottom > SCREEN_HEIGHT:
            self.speed_y *= (-1)

        # check for collision with paddles
        if self.rect.colliderect(player_paddle) or self.rect.colliderect(cpu_paddle):
            self.speed_x *= (-1)

        # check for out of bounds
        if self.rect.left < 0:
            self.winner = 1
        elif self.rect.right > SCREEN_WIDTH:
            self.winner = -1

        # update ball position
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.winner

    def draw(self):
        pygame.draw.circle(self.screen, WHITE, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)

    def reset(self, x, y, screen):
        self.screen = screen
        self.x = x
        self.y = y
        self.ball_rad = 8
        self.rect = pygame.Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = -4
        self.speed_y = 4
        self.winner = 0  # 1 means P1 has scored and -1 means CPU has scored
