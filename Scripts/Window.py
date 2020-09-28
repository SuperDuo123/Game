import pygame
from Menu import *
from Map import *
from handle_keys import *
from Unit import *
from Player import Player
import numpy


class Window():
    def __init__(self, window_width, window_height, fullscreen):
        #initialize pygame, menu classes
        pygame.init()
        self.player = Player()

        # self.army = []
        self.menu = Menu(self) #tosses window class attributes and functions to Menu class
        # booleans to keep track which surfaces to blit
        self.blit_menu = False
        self.blit_map = False
        self.create_u = False

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

    def create_unit(self):
        if self.create_u == True:
            # self.army.append(Elf(self))
            self.player.army.append(Elf(self, self.player))
            self.player.display_units()
            
        #print(self.army)
        
        self.create_u = False

    

    
    def load_map(self):
        # create map instance, load generated map on top on the menu
        self.blit_menu = False
        self.blit_map = True
        self.map = Map(self, 15) #tosses window class attributes and functions to Map class
        self.map.load_tile_types()
        self.map.generate()

    def load_keys(self):
        self.keyboard_mouse = Handle_keys(self, self.player)
        #self.keyboard_mouse = Handle_keys(self, self.menu)


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
            self.create_unit()
            
            #managing which surfaces to blit
            if self.blit_menu == True:
                #menu background blitting
                self.screen.blit(self.menu.background_surface, (0, 0))
                self.screen.blit(self.menu.buttons_surface, (0, 0))

            if self.blit_map == True:
                #menu background blitting
                self.screen.fill((0,0,0)) #deletes different surfaces
                self.screen.blit(self.map.surface, (self.map.map_location_x, self.map.map_location_y))
                for unit in self.player.army:
                    self.screen.blit(unit.render, (unit.x_location, unit.y_location))
                    if unit.highlight == True:
                        pygame.draw.rect(self.screen, (255, 0, 0), unit.rectangle, 1)
                        #print("selected")
                    #print(unit.selected)

            #render army
                
                

            

            #event loop
            self.keyboard_mouse.handle()

            pygame.display.update()











        