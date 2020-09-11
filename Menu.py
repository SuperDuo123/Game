import pygame
from settings import *
from Window import *
from pygame import surface, display, rect

class Menu():

    def __init__(self):
        self.buttons = {}

        self.background_surface = pygame.Surface((window_width, window_height))
        self.buttons_surface = pygame.Surface((window_width, window_height), pygame.SRCALPHA, 32)



    def check_surfaces(self):
        print(self.background_surface)
        print(self.buttons_surface)


    def load_images(self):
        #do zmiany. Sprobuj uzyc generatorow yield etc. Plus później automatyczne dopasowanie do rozdzielczosci
        self.menu_image = pygame.image.load("Menu/temp_menu.png").convert_alpha()
        self.menu_image = pygame.transform.scale(self.menu_image,(window_width, window_height))
        #load functional buttons and get rect size from them
        self.sound_image = pygame.image.load("Menu/dzwiek.png").convert_alpha()
        self.sound_image_rect = self.sound_image.get_rect()
        self.fullscreen_image = pygame.image.load("Menu/full.png").convert_alpha()
        self.fullscreen_image_rect = self.fullscreen_image.get_rect()

        #load button images and get rect size from them
        self.start_image = pygame.image.load("Menu/start.png").convert_alpha()
        self.start_image_rect = self.start_image.get_rect()
        self.start_image = pygame.transform.scale(self.start_image, (int(self.start_image_rect.width * scaling_width), int(self.start_image_rect.height * scaling_height)))
        self.start_image_rect = self.start_image.get_rect()
        self.buttons[self.start_image] = self.start_image_rect

        self.exit_image = pygame.image.load("Menu/exit.png").convert_alpha()
        self.exit_image_rect = self.exit_image.get_rect()
        self.exit_image = pygame.transform.scale(self.exit_image, (int(self.exit_image_rect.width * scaling_width), int(self.exit_image_rect.height * scaling_height)))
        self.exit_image_rect = self.exit_image.get_rect()
        self.buttons[self.exit_image] = self.exit_image_rect

    def render_background(self):
        self.background_surface.blit(self.menu_image,(0,0))


    '''method renders buttons from dictionary self.buttons in which there are information about rect from image and image coordinates.'''
    def render_buttons(self):
        height = self.start_image_rect.height
        width = self.start_image_rect.width

        for key in self.buttons:
            self.buttons_surface.blit(key, (window_width/2 - width/2 , height))
            self.buttons[key].move(window_width/2 - width/2, height)
            height += self.buttons[key].height + window_height / 10



