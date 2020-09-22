from Window import *
import pygame
import random
import math
import os
class Unit:

    def __init__(self, window):
        self.window = window
        
        self.attack_range = 0
        self.accuracy = 0
        self.range_of_view = 0
        self.x_location = random.randint(30,400)
        self.y_location = random.randint(30,400)
        self.highlight = False       
        print(f"X = {self.x_location}, Y = {self.y_location}")

    def move(self, mouse_coords):
        if self.highlight:
            if mouse_coords[0] % 40 == 0 and mouse_coords[1] % 40 == 0:
                self.x_location = mouse_coords[0]
                self.y_location = mouse_coords[1]
            else:
                self.x_location = int(40 * math.floor(mouse_coords[0]/40))
                self.y_location = int(40 * math.floor(mouse_coords[1]/40))
        
        

    def attack_unit(self):
        pass

    def recruit(self):
        pass

    def select_unit(self):
        self.highlight = True



class Elf(Unit):
    def __init__(self, window):
        super().__init__(self)
        self.hp = 400
        self.attack = 20
        self.armor = 10
        self.speed = 90
        self.game_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        self.unit_path = "/Grafika/elf.png"
        self.load_image()

    def load_image(self):
        self.image = pygame.image.load(self.game_dir + self.unit_path)

    @property
    def render(self):
        return self.image

    @property
    def rectangle(self):
        return self.image.get_rect(topleft = (self.x_location, self.y_location))
