import pygame


class Window():

    def __init__(self, width, height, caption):
        self.width = width
        self.height = height
        self.caption = caption
        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(self.caption)
