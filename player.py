import pygame


class Player():

    def __init__(self, x, y, width, height, color, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = vel
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = pygame.image.load("assets/helicopter.png")
        self.img = pygame.transform.scale(self.img, (64, 64))
        self.img.set_colorkey((255, 255, 255))

    def draw(self, win):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.img, dest=(self.x, self.y))

    def move(self, keys, win):
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if self.y > 0:
                self.y -= self.vel
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if self.y + self.height < win.height:
                self.y += self.vel
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if self.x > 0:
                self.x -= self.vel
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if self.x + self.width < win.width:
                self.x += self.vel
