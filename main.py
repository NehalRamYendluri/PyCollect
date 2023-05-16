import pygame, sys
from pygame.locals import QUIT
from player import Player
from display import Window
from coin import Coin
import random, time , math
from button import Button
pygame.init()
WIN = Window(500, 400, "Game Test")
player = Player(40, 275, 64, 64, (255, 0, 0), 340)
FPS = 60
clock = pygame.time.Clock()
coins = []
font = pygame.font.Font(pygame.font.get_default_font(), 18)
coinsc = 0
start_time = time.perf_counter()
bg = pygame.image.load("assets/background.png").convert()
bg = pygame.transform.scale(bg,(500,400))
vel = 10
sound = True
sound_img = pygame.image.load("assets/music.png").convert()
cancel = pygame.image.load("assets/checked.png").convert()
cancel.set_colorkey((0,255,0))
pause = False
pause_img = pygame.image.load("assets/pause.png").convert()
pause_img.set_colorkey((255,255,255))
pause_butt = Button(20,20,"p",64,64,img=pause_img,colorkey=(255,255,255))
extra_time = 0
def two_d(num):
    if num < 10:
        num = "0"+str(num)
    return str(num)
def draw(win,dt,curr_time):
    win.surface.blit(bg,dest=(0,0))
    for i in coins:
        if i.y > win.height - 100:
          coins.remove(i)
          continue
        i.y += vel * dt
        i.draw(win)
    player.draw(win.surface)
    fpst = pygame.font.Font.render(font, "FPS: " + str(int(clock.get_fps())),
                                   True, (0, 0, 0))
    win.surface.blit(fpst, dest=(400, 40))
    coinst = pygame.font.Font.render(font, "Coins: " + str(int(coinsc)), True,
                                     (0, 0, 0))
    win.surface.blit(coinst, dest=(100, 40))
    tt = pygame.font.Font.render(font,
                                 "Time: " + str(str(math.floor((curr_time - start_time)/60))+":"+two_d(round((curr_time-start_time) % 60))),
                                 True, (0, 0, 0))
    win.surface.blit(tt, dest=(250, 40))
    pause_butt.draw(win)
#    win.surface.blit(sound_butt,dest=(20,20))
#    if not sound:
#        win.surface.blit(cancel,dest=(20,20))

def pausef(pause,win,et,sound):
    pygame.draw.rect(win.surface,(0,0,0),(115,70,260,210))
    pygame.draw.rect(win.surface,(255,255,255),(120,75,250,200))
    resume_butt = Button(210,115,"Resume",80,20,bg=(125,125,125))
    resume_butt.draw(win)
    exit_butt = Button(210,145,"Exit",80,20,bg=(125,125,125))
    exit_butt.draw(win)
    sound_butt = Button(230,180,"M",64,64,sound_img,colorkey=(0,255,0))
    sound_butt.draw(win)
    if sound ==False:
        win.surface.blit(cancel,dest=(230,180))
    pygame.display.update()
    pause_time = time.perf_counter()
    while pause:
        for event in pygame.event.get():
            if event.type == QUIT or exit_butt.click(event):
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()
            if resume_butt.click(event):
                pause = False
            if sound_butt.click(event):
                if sound == True:
                    bgm.set_volume(0)
                    coinm.set_volume(0)
                    win.surface.blit(cancel,dest=(230,180))
                    sound = False
                else:
                    bgm.set_volume(0.5)
                    coinm.set_volume(0.5)
                    sound = True
                    pygame.draw.rect(win.surface,(255,255,255),(230,180,64,64))
                    sound_butt.draw(win)   
                pygame.display.update()        
    ct = time.perf_counter()            
    et += ct - pause_time
    return et , sound
bgm = pygame.mixer.Sound("assets/soundtrack.mp3")
bgm.set_volume(0.5)
coinm = pygame.mixer.Sound("assets/coin.mp3")
coinm.set_volume(0.5)
pygame.mixer.Channel(0).play(bgm,-1)
while True:
    clock.tick(FPS)
    dt = clock.tick(FPS)/1000
    curr_time = time.perf_counter()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.mixer.quit()
            pygame.quit()
            sys.exit()
        if pause_butt.click(event):
            pause = True
            t = pausef(pause,WIN,extra_time,sound)
            start_time += t[0]    
            sound = t[1]               
    keys = pygame.key.get_pressed()
    if 1 in keys:
        player.move(keys, WIN,dt)
    if len(coins) < 4:
        coins.append(
            Coin(random.randint(0, WIN.width - 100),
                 random.randint(0, WIN.height - 320)))
    
    for i in coins:
        if i.rect.colliderect(player.rect):
            pygame.mixer.Channel(1).play(coinm)
            coinsc += 1
            coins.remove(i)
            if vel < 20:
              vel += 0.5
            elif player.vel < 800:
                vel += 0.25
                player.vel += 2.5
            else:
                vel += 0.125        
        if i.y > WIN.height - 75:
            coins.remove(i)        
    draw(WIN,dt,curr_time)
    pygame.display.update()
