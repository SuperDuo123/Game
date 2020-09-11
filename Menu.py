import pygame
from settings import *
from pygame import surface, display, rect

class Menu():

    def __init__(self):
        self.background_surface = pygame.surface.Surface((window_width, window_height))
        self.buttons_surface = pygame.surface.Surface((window_width, window_height))

    def check_surfaces(self):
        print(self.background_surface)
        print(self.buttons_surface)
#menu = Menu()


