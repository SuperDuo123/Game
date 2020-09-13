import pygame
from Menu import *


class Window():
    def __init__(self, window_width, window_height, fullscreen):
        #initialize pygame, menu classes
        pygame.init()

        self.menu = Menu(self) #tosses window class attributes and functions to Menu class

        #window initialization parameters
        self.window_width = window_width
        self.window_height = window_height
        self.fullscreen = fullscreen
        self.sound = sound
        self.window_init()
        # load menu images and render menu background
        self.load_menu()
        # mainloop
        self.mainloop()

    def load_menu(self):
        #load menu images and render menu background
        self.menu.load_button_images()
        self.menu.load_option_buttons()
        self.menu.render_background()
        self.menu.render_buttons()


        
        

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
            #menu background blitting
            self.screen.blit(self.menu.background_surface, (0, 0))
            self.screen.blit(self.menu.buttons_surface, (0, 0))

            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    """Left Mouse Button is associated with id. 1 of event.button. It's in-built function of pygame."""
                    if event.button == 1: #Left Mouse Button Click
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

                """Activates when keyboard key is pressed"""
                if event.type == pygame.KEYDOWN:
                    pass
            pygame.display.update()











        