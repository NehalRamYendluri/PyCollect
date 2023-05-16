import pygame

class Button():
    def __init__(self,x,y,text,width,height,img=None,colorkey=None,bg=(255,255,255)):
        self.x = x
        self.y = y
        self.text = text
        self.width = width
        self.height = height
        self.font = pygame.font.Font(pygame.font.get_default_font(), 18) 
        self.text1 = pygame.font.Font.render(self.font,self.text,True,(0,0,0),bg)
        self.rect = pygame.Rect(self.x,self.y,width,height)
        self.bg = bg
        if img != None:
          self.img = pygame.transform.scale(img,(self.width,self.height))
          if colorkey != None:
              self.img.set_colorkey(colorkey)
        if img == None:
            self.img= None      
    def draw(self,win):
        if self.img != None:
           win.surface.blit(self.img,dest=(self.x,self.y)) 
        else:   
           pygame.draw.rect(win.surface,self.bg,self.rect)
           win.surface.blit(self.text1,dest=(self.x,self.y))
    def click(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                return True
        return False           
                 
          
