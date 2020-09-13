import pygame
from settings import *
# from Window import *
import os


class Menu():

    def __init__(self, window):
        self.window = window  # assigns window class attributes
        """Nested dictionary. Number 0 of dict equals to start button. Number 1 of dict equals to exit button."""

        self.buttons = {0: {},
                        1: {}}
        self.options = {0: {},
                        1: {}}
        self.background_surface = pygame.Surface((window_width, window_height))
        self.buttons_surface = pygame.Surface((window_width, window_height), pygame.SRCALPHA, 32)
        self.clicked_button = None
        self.clicked_option_button = None

    # check function. Debug
    def check_surfaces(self):
        print(self.background_surface)
        print(self.buttons_surface)

    def load__button_images(self):
        """Load button images. Start game button, exit button"""
        self.game_dir = os.path.dirname(os.getcwd())
        self.graphics_dir = r"\Grafika\Menu"

        # do zmiany. Sprobuj uzyc generatorow yield etc. Plus później automatyczne dopasowanie do rozdzielczosci
        self.menu_image = pygame.image.load(fr"{self.game_dir}{self.graphics_dir}\temp_menu.png").convert_alpha()
        self.menu_image = pygame.transform.scale(self.menu_image, (window_width, window_height))
        # load functional buttons and get rect size from them

        # load button images and get rect size from them
        self.start_image = pygame.image.load(fr"{self.game_dir}{self.graphics_dir}\start.png").convert_alpha()
        # get rectangle object of an image
        self.start_image_rect = self.start_image.get_rect()
        self.start_image = pygame.transform.scale(self.start_image, (int(self.start_image_rect.width * scaling_width),
                                                                     int(
                                                                         self.start_image_rect.height * scaling_height)))
        # get rectangle object of a scaled image
        self.start_image_rect = self.start_image.get_rect()
        # add image with corresponding rectangle object to dictionary
        self.buttons[0][self.start_image] = self.start_image_rect

        self.exit_image = pygame.image.load(fr"{self.game_dir}{self.graphics_dir}\exit.png").convert_alpha()
        # get rectangle object of an image
        self.exit_image_rect = self.exit_image.get_rect()
        self.exit_image = pygame.transform.scale(self.exit_image, (int(self.exit_image_rect.width * scaling_width),
                                                                   int(self.exit_image_rect.height * scaling_height)))
        # get rectangle object of a scaled image
        self.exit_image_rect = self.exit_image.get_rect()
        # add image with corresponding rectangle object to dictionary
        self.buttons[1][self.exit_image] = self.exit_image_rect

    def load_option_buttons(self):
        """Load images of option buttons. Fullscreen button and sound button"""
        self.sound_image = pygame.image.load(
            os.path.abspath(fr"{self.game_dir}{self.graphics_dir}\dzwiek.png")).convert_alpha()
        # get rectangle object of an image
        self.sound_image_rect = self.sound_image.get_rect()
        self.sound_image = pygame.transform.scale(self.sound_image, (int(self.sound_image_rect.width * scaling_width),
                                                                     int(
                                                                         self.sound_image_rect.height * scaling_height)))
        # get rectangle object of scaled image
        self.sound_image_rect = self.sound_image.get_rect()
        # add button 0 to dictionary
        self.options[0][self.sound_image] = self.sound_image_rect

        self.fullscreen_image = pygame.image.load(fr"{self.game_dir}{self.graphics_dir}\full.png").convert_alpha()
        # get rectangle object of scaled image
        self.fullscreen_image_rect = self.fullscreen_image.get_rect()
        self.fullscreen_image = pygame.transform.scale(self.fullscreen_image,
                                                       (int(self.fullscreen_image_rect.width * scaling_width),
                                                        int(self.fullscreen_image_rect.height * scaling_height)))
        # get rectangle object of scaled image
        self.fullscreen_image_rect = self.fullscreen_image.get_rect()
        # add button 0 to dictionary
        self.options[1][self.fullscreen_image] = self.fullscreen_image_rect

    def render_background(self):
        # blit background image to background surface
        self.background_surface.blit(self.menu_image, (0, 0))

    """method renders buttons from dictionary self.buttons in which there are information about rect from image and 
    image coordinates. """

    def render_buttons(self):
        """Function responsible for scaling the distance between buttons"""
        height = self.start_image_rect.height
        width = self.start_image_rect.width

        """First loop gets number and nested dictionary. Second loop renders buttons"""
        for i, button_dict in self.buttons.items():
            for key in button_dict:
                self.buttons_surface.blit(key, (window_width / 2 - width / 2, height))
                self.buttons[i][key].x = window_width / 2 - width / 2
                self.buttons[i][key].y = height
                height += self.buttons[i][key].height + window_height / 10

        """Render option buttons"""
        height = self.fullscreen_image_rect.height
        width = self.fullscreen_image_rect.width
        n = 1

        for i, button_dict in self.options.items():
            for key in button_dict:
                self.buttons_surface.blit(key, ((window_width - width) - width * n, window_height - height))
                self.options[i][key].x = (window_width - width) - width * n
                self.options[i][key].y = window_height - height
                n += 1
                width += self.options[i][key].width / 10

    def button_event_listener(self, click_coordinates):
        """Event listener"""
        """First loop gets number and nested dictionary."""
        for i, button_dict in self.buttons.items():
            """Iterates through individual button and associate it with button id (i). If clicked coordinates equals
            to right coordinates of buttons it prints message with button id and button object"""
            for button in button_dict:
                if self.buttons[i][button].x < click_coordinates[0] < self.buttons[i][button].x + self.buttons[i][
                    button].width:
                    if self.buttons[i][button].y < click_coordinates[1] < self.buttons[i][button].y + self.buttons[i][
                        button].height:
                        self.clicked_button = i
                        print(f"You have clicked {button} button with number {i}")

        """Iterates through individual button and associate it with button id (i). If clicked coordinates equals
        to right coordinates of buttons it prints message with button id and button object"""
        for i, button_dict in self.options.items():
            for button in button_dict:
                if self.options[i][button].x < click_coordinates[0] < self.options[i][button].x + self.options[i][
                    button].width:
                    if self.options[i][button].y < click_coordinates[1] < self.options[i][button].y + self.options[i][
                        button].height:
                        self.clicked_option_button = i
                        print(f"You have clicked {button} option button with number {i}")
        self.button_handler() #launch button handler. Function button_handler() below.

    def button_handler(self):
        """buttons for start game and exit"""
        #if there is no value do nothing
        if self.clicked_button is None:
            pass
        #start game button. You need to add function to make it work
        elif self.clicked_button == 0:
            pass
        #exit button function. It just changes the mainloop to false.
        elif self.clicked_button == 1:
            print("Clicked exit button")
            self.window.run = False

        """buttons for fullscreen and sound"""
        #if there is no value, do nothing
        if self.clicked_option_button is None:
            pass
        #if clicked print clicked sound button. Making in progress
        elif self.clicked_option_button == 0:
            print("clicked sound button")
        #toggle fullscreen or not
        elif self.clicked_option_button == 1:
            if self.window.fullscreen:
                self.window.screen = pygame.display.set_mode((window_width, window_height))
                self.window.fullscreen = False
                self.clicked_option_button = None
            else:
                self.window.screen = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
                self.window.fullscreen = True
                self.clicked_option_button = None
            print("clicked fullscreen mode")
