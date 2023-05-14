import pygame, sys
from pygame.locals import QUIT
from player import Player
from display import Window
from coin import Coin
import random, time , math

pygame.init()
WIN = Window(500, 400, "Game Test")
player = Player(40, 300, 64, 64, (255, 0, 0), 4)
FPS = 60
clock = pygame.time.Clock()
coins = []
font = pygame.font.Font(pygame.font.get_default_font(), 18)
coinsc = 0
start_time = time.perf_counter()
bg = pygame.image.load("assets/background.png").convert()
bg = pygame.transform.scale(bg,(500,400))
vel = 0.1

def draw(win):
    win.surface.blit(bg,dest=(0,0))
    for i in coins:
        if i.y > win.height - 100:
          coins.remove(i)
          continue
        i.y += vel
        i.draw(win)
    player.draw(win.surface)
    fpst = pygame.font.Font.render(font, "FPS: " + str(int(clock.get_fps())),
                                   True, (0, 0, 0))
    win.surface.blit(fpst, dest=(400, 40))
    coinst = pygame.font.Font.render(font, "Coins: " + str(int(coinsc)), True,
                                     (0, 0, 0))
    curr_time = time.perf_counter()
    win.surface.blit(coinst, dest=(50, 40))
    tt = pygame.font.Font.render(font,
                                 "Time: " + str(str(math.floor((curr_time - start_time)/60))+":"+str(round((curr_time-start_time) % 60))),
                                 True, (0, 0, 0))
    win.surface.blit(tt, dest=(225, 40))


bgm = pygame.mixer.Sound("assets/soundtrack.mp3")
coinm = pygame.mixer.Sound("assets/coin.mp3")
pygame.mixer.Channel(0).play(bgm)
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.mixer.quit()
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if 1 in keys:
        player.move(keys, WIN)
    if len(coins) < 4:
        coins.append(
            Coin(random.randint(0, WIN.width - 100),
                 random.randint(0, WIN.height - 400)))
    for i in coins:
        if i.rect.colliderect(player.rect):
            pygame.mixer.Channel(1).play(coinm)
            coinsc += 1
            coins.remove(i)
            if vel < 0.3:
              vel += 0.02
    draw(WIN)
    pygame.display.update()
