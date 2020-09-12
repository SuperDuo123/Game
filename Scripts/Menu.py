import pygame
from settings import *
from Window import *
from pygame import surface, display, rect

class Menu():

    def __init__(self):
        """Nested dictionary. Number 0 of dict equals to start button. Number 1 of dict equals to exit button."""
        self.buttons = {0:{},
                        1:{}}
        self.background_surface = pygame.Surface((window_width, window_height))
        self.buttons_surface = pygame.Surface((window_width, window_height), pygame.SRCALPHA, 32)


    #check function. Debug
    def check_surfaces(self):
        print(self.background_surface)
        print(self.buttons_surface)


    def load_images(self):
        #do zmiany. Sprobuj uzyc generatorow yield etc. Plus później automatyczne dopasowanie do rozdzielczosci
        self.menu_image = pygame.image.load("../Grafika/Menu/temp_menu.png").convert_alpha()
        self.menu_image = pygame.transform.scale(self.menu_image, (window_width, window_height))
        #load functional buttons and get rect size from them
        self.sound_image = pygame.image.load("../Grafika/Menu/dzwiek.png").convert_alpha()

        #get rectangle object of an image
        self.sound_image_rect = self.sound_image.get_rect()
        self.fullscreen_image = pygame.image.load("../Grafika/Menu/full.png").convert_alpha()
        # get rectangle object of a scaled image
        self.fullscreen_image_rect = self.fullscreen_image.get_rect()

        #load button images and get rect size from them
        self.start_image = pygame.image.load("../Grafika/Menu/start.png").convert_alpha()
        # get rectangle object of an image
        self.start_image_rect = self.start_image.get_rect()
        self.start_image = pygame.transform.scale(self.start_image, (int(self.start_image_rect.width * scaling_width),
                                                                     int(self.start_image_rect.height * scaling_height)))
        # get rectangle object of a scaled image
        self.start_image_rect = self.start_image.get_rect()
        # add image with corresponding rectangle object to dictionary
        self.buttons[0][self.start_image] = self.start_image_rect

        self.exit_image = pygame.image.load("../Grafika/Menu/exit.png").convert_alpha()
        # get rectangle object of an image
        self.exit_image_rect = self.exit_image.get_rect()
        self.exit_image = pygame.transform.scale(self.exit_image, (int(self.exit_image_rect.width * scaling_width),
                                                                   int(self.exit_image_rect.height * scaling_height)))
        # get rectangle object of a scaled image
        self.exit_image_rect = self.exit_image.get_rect()
        # add image with corresponding rectangle object to dictionary
        self.buttons[1][self.exit_image] = self.exit_image_rect

    def render_background(self):
        #blit background image to background surface
        self.background_surface.blit(self.menu_image,(0,0))


    """method renders buttons from dictionary self.buttons in which there are information about rect from image and 
    image coordinates. """
    def render_buttons(self):
        """Function responsible for scaling the distance between buttons"""
        height = self.start_image_rect.height
        width = self.start_image_rect.width

        """First loop gets number and nested dictionary. Second loop renders buttons"""
        for i, button_dict in self.buttons.items():
            for key in button_dict:
                self.buttons_surface.blit(key, (window_width/2 - width/2 , height))
                self.buttons[i][key].x = window_width/2 - width/2
                self.buttons[i][key].y = height
                height += self.buttons[i][key].height + window_height / 10

    def button_event_listener(self, click_coordinates):
        """Event listener"""
        """First loop gets number and nested dictionary."""
        for i, button_dict in self.buttons.items():
            """Iterates through individual button and associate it with button id (i). If clicked coordinates equals
            to right coordinates of buttons it prints message with button id and button object"""
            for button in button_dict:
                if self.buttons[i][button].x < click_coordinates[0] < self.buttons[i][button].x + self.buttons[i][button].width:
                    if self.buttons[i][button].y < click_coordinates[1] < self.buttons[i][button].y + self.buttons[i][button].height:
                        print(f"You have clicked {button} button with number {i}")




