import pygame
from Menu import Menu


class Window():
    def __init__(self, window_width, window_height, fullscreen):
        #initialize pygame, menu classes
        pygame.init()
        self.menu = Menu()

        #window initialization parameters
        self.window_width = window_width
        self.window_height = window_height
        self.fullscreen = fullscreen
        self.window_init()
        # load menu images and render menu background
        self.load_menu()
        # mainloop
        self.mainloop()

    def load_menu(self):
        #load menu images and render menu background
        self.menu.load_images()
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

        run = True
        while run:
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
                        print(pygame.mouse.get_pos())

                    if event.button == 2: #Middle Mouse Button Click
                        pass

                    if event.button == 3: #Right Mouse Button Click
                        pass
                    if event.button == 4: #Scroll Up
                        pass
                    if event.button == 5: #Scroll Down
                        pass



            pygame.display.update()








        