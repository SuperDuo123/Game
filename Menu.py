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


    def load_images(self):
        #do zmiany. Sprobuj uzyc generatorow yield etc.
        self.menu_image = pygame.image.load("Menu/temp_menu.png").convert_alpha()
        self.sound_image = pygame.image.load("Menu/dzwiek.png").convert_alpha()
        self.fullscreen_image = pygame.image.load("Menu/full.png").convert_alpha()
        self.start_image = pygame.image.load("Menu/start.png").convert_alpha()
        self.exit_image = pygame.image.load("Menu/exit.png").convert_alpha()

#menu = Menu()


