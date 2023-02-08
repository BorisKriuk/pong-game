import pygame
from variables import MARGIN, SCREEN_HEIGHT, WHITE


class Paddle:
    def __init__(self, x, y, screen):
        self.screen = screen
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 20, 100)
        self.speed = 5

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.rect.top > MARGIN+5:
            self.rect.move_ip(0, (-1)*self.speed)
        elif key[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT-5:
            self.rect.move_ip(0, self.speed)

    def ai(self, pong):
        # ai to move paddle
        # move down
        if self.rect.centery < pong.rect.top and self.rect.bottom < SCREEN_HEIGHT-5:
            self.rect.move_ip(0, self.speed)

        # move up
        if self.rect.centery > pong.rect.bottom and self.rect.top > MARGIN+5:
            self.rect.move_ip(0, (-1) *self.speed)

    def draw(self):
        pygame.draw.rect(self.screen, WHITE, self.rect)
