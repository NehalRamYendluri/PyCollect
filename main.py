import pygame, sys
from pygame.locals import QUIT
from player import Player
from display import Window
from coin import Coin
import random, time , math
from button import Button
from settings import *
pygame.init()
WIN = Window(screen_width*factor, screen_height*factor, "PyCollect")
player = Player(40, 275, 64*factor, 64*factor, (255, 0, 0), 300*factor/2)
clock = pygame.time.Clock()
coins = []
font = pygame.font.Font(pygame.font.get_default_font(), 27)
coinsc = 0
start_time = time.perf_counter()
bg = pygame.image.load("assets/background.png").convert()
bg = pygame.transform.scale(bg,(screen_width*factor,screen_height*factor))
vel = 10 * factor/2
sound = True
sound_img = pygame.image.load("assets/music.png").convert()
cancel = pygame.image.load("assets/checked.png").convert()
cancel = pygame.transform.scale(cancel,(100,100))
cancel.set_colorkey((0,255,0))
pause = False
pause_img = pygame.image.load("assets/pause.png").convert()
pause_img.set_colorkey((255,255,255))
pause_img = pygame.transform.scale2x(pause_img)
pause_butt = Button(40,40,"p",128,128,img=pause_img,colorkey=(255,255,255))
extra_time = 0
def two_d(num):
    if num < 10:
        num = "0"+str(num)
    return str(num)
def draw(win,dt,curr_time):
    win.surface.blit(bg,dest=(0,0))
    for i in coins:
        if i.y > win.height - 200:
          coins.remove(i)
          continue
        i.y += vel * dt
        i.draw(win)
    player.draw(win.surface)
    fpst = pygame.font.Font.render(font, "FPS: " + str(int(clock.get_fps())),
                                   True, (0, 0, 0))
    win.surface.blit(fpst, dest=(200*factor, 20*factor))
    coinst = pygame.font.Font.render(font, "Coins: " + str(int(coinsc)), True,
                                     (0, 0, 0))
    win.surface.blit(coinst, dest=(50*factor, 20*factor))
    tt = pygame.font.Font.render(font,
                                 "Time: " + str(str(math.floor((curr_time - start_time)/60))+":"+two_d(round((curr_time-start_time) % 60))),
                                 True, (0, 0, 0))
    win.surface.blit(tt, dest=(125*factor, 20*factor))
    pause_butt.draw(win.surface)
#    win.surface.blit(sound_butt,dest=(20,20))
#    if not sound:
#        win.surface.blit(cancel,dest=(20,20))

def pausef(pause,win,et,sound):
    pause_surf = pygame.Surface((260*factor/2,210*factor/2))
    pause_surf.fill((125,125,125))
    resume_butt = Button(210,100,"Resume",100,50,bg=(125,125,125))
    resume_butt.draw(pause_surf)
    exit_butt = Button(210,145,"Exit",100,40,bg=(125,125,125))
    exit_butt.draw(pause_surf)
    sound_butt = Button(230,180,"M",100,100,sound_img,colorkey=(0,255,0))
    sound_butt.draw(pause_surf)
    if sound ==False:
        pause_surf.blit(cancel,dest=(230,180))
    win.surface.blit(pause_surf,dest=(200,200))    
    pygame.display.update()
    pause_time = time.perf_counter()
    while pause:
        for event in pygame.event.get():
            if event.type == QUIT or exit_butt.click(event,200,200):
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()
            if resume_butt.click(event,200,200):
                pause = False
            if sound_butt.click(event,200,200):
                if sound == True:
                    bgm.set_volume(0)
                    coinm.set_volume(0)
                    pause_surf.blit(cancel,dest=(230,180))
                    sound = False
                else:
                    bgm.set_volume(0.5)
                    coinm.set_volume(0.5)
                    sound = True
                    pygame.draw.rect(pause_surf,(125,125,125),(230,180,100,100))
                    sound_butt.draw(pause_surf)   
                win.surface.blit(pause_surf,dest=(200,200))    
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
        if pause_butt.click(event,0,0):
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
                 random.randint(0, WIN.height - 320),cfactor))
    for i in coins:
        if player.mask.overlap(i.mask,(i.x-player.x,i.y-player.y)) and player.left or player.mask1.overlap(i.mask,(i.x-player.x,i.y-player.y)) and not player.left:
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
    player.update()                                            
    draw(WIN,dt,curr_time)
    pygame.display.update()
