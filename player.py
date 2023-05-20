import pygame
import math
class Player():

    def __init__(self, x, y, width, height, color, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = vel
        self.rect = pygame.Rect(self.x, self.y, self.width-20, self.height-20)
        self.img = pygame.image.load("assets/helicopter.png").convert_alpha()
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.img = pygame.transform.rotate(self.img,10)
        #self.img.set_colorkey((0, 255, 0))
        self.mask = pygame.mask.from_surface(self.img)
        self.img1 = pygame.transform.flip(self.img,True,False)
        self.img1 = pygame.transform.rotate(self.img1,350)
        #self.img1.set_colorkey((0, 255, 0))
        self.mask1 = pygame.mask.from_surface(self.img1)
        self.left = True
        self.angle = 0
        self.timg = self.img
        self.timg1 = self.img1
        self.vector = pygame.Vector2()
        self.vector.xy = self.x, self.y
        self.vector[:] = self.x, self.y
    def draw(self, win):
           win.blit(self.timg, dest=(self.x, self.y))
    def move(self, keys, win,dt):
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if self.y > 25:
                self.y -= self.vel * dt
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if self.y + self.height < win.height-75:
                self.y += self.vel * dt
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if self.x > 0:
                self.x -= self.vel * dt   
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if self.x + self.width < win.width:
                self.x += self.vel * dt        
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_vec = pygame.Vector2()
        mouse_vec.xy = mouse_pos[0],mouse_pos[1]
        mouse_vec[:]= mouse_pos[0],mouse_pos[1]
        self.angle = -(mouse_vec - self.vector).angle_to(pygame.Vector2(1, 0))   
        self.timg = pygame.transform.rotate(self.img1,360-self.angle)
