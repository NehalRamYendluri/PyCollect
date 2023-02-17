import pygame


class Coin():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.img = pygame.image.load("assets/coin.png").convert()
        self.img = pygame.transform.scale(self.img, (64, 64))
        self.img.set_colorkey((255, 255, 255))

    def draw(self, win):
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        win.surface.blit(self.img, dest=(self.x, self.y))
