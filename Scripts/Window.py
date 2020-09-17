import pygame
from Menu import *
from Map import *


class Window():
    def __init__(self, window_width, window_height, fullscreen):
        #initialize pygame, menu classes
        pygame.init()

        self.menu = Menu(self) #tosses window class attributes and functions to Menu class

        # booleans to keep track which surfaces to blit
        self.blit_menu = False
        self.blit_map = False

        # window initialization parameters
        self.window_width = window_width
        self.window_height = window_height
        self.fullscreen = fullscreen
        self.sound = sound

    def load_menu(self):
        #load menu images and render menu background
        self.blit_map = False
        self.blit_menu = True
        self.menu.load_button_images()
        self.menu.load_option_buttons()
        self.menu.render_background()
        self.menu.render_buttons()
    
    def load_map(self):
        # create map instance, load generated map on top on the menu
        self.blit_menu = False
        self.blit_map = True
        self.map = Map(self, 15) #tosses window class attributes and functions to Map class
        self.map.load_tile_types()
        self.map.generate()


    def window_init(self):
        #FULLSCREEN maximizes the window without fitting the resolution
        #pygame.FULLSCREEN fit the resolution as well as maximizing
        if self.fullscreen:
            self.screen = pygame.display.set_mode((self.window_width, self.window_height), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.window_width, self.window_height))

    def mainloop(self):

        self.run = True
        while self.run:

            #managing which surfaces to blit
            if self.blit_menu == True:
                #menu background blitting
                self.screen.blit(self.menu.background_surface, (0, 0))
                self.screen.blit(self.menu.buttons_surface, (0, 0))

            if self.blit_map == True:
                #menu background blitting
                self.screen.fill((0,0,0)) #deletes different surfaces
                self.screen.blit(self.map.surface, (self.map.map_location_x, self.map.map_location_y))

            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    """Left Mouse Button is associated with id. 1 of event.button. It's in-built function of pygame."""
                    if event.button == 1: #Left Mouse Button Click
                        if self.blit_menu == True:
                            self.menu.button_event_listener(pygame.mouse.get_pos())
                        #self.menu.button_handler()
                        print(pygame.mouse.get_pos())

                    if event.button == 2: #Middle Mouse Button Click
                        pass

                    if event.button == 3: #Right Mouse Button Click
                        pass
                    if event.button == 4: #Scroll Up
                        pass
                    if event.button == 5: #Scroll Down
                        pass
                """Activates when keyboard key is released"""
                if event.type == pygame.KEYUP:
                    """Escape button for calling in-game Menu"""
                    if event.key == pygame.K_ESCAPE:
                        print("ESC Clicked")
                        self.run = False

                """Activates when keyboard key is pressed"""
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.map.map_location_y += 40
                    if event.key == pygame.K_s:
                        self.map.map_location_y -= 40
                    if event.key == pygame.K_a:
                        self.map.map_location_x += 40
                    if event.key == pygame.K_d:
                        self.map.map_location_x -= 40



            pygame.display.update()











        