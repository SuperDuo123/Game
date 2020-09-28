from Window import *
import pygame
import random
import math
import os
from Player import *
class Unit:

    def __init__(self, window):
        
        self.window = window

        self.selected = False        
        self.range_of_view = 0
        self.x_location = random.randint(30,400)
        self.y_location = random.randint(30,400)
        self.highlight = False       
        print(f"X = {self.x_location}, Y = {self.y_location}")

    def unit_interact(self, mouse_coords, value):
        #print(value)
        if self.rectangle.x < mouse_coords[0] and self.rectangle.x + self.rectangle.width > mouse_coords[0]:
            if self.rectangle.y < mouse_coords[1] and self.rectangle.y + self.rectangle.height > mouse_coords[1]:
                print(value)
                self.selected = True

        if self.highlight:
            #self.attack_unit(value, mouse_coords)
            self.move(mouse_coords)
            


        self.highlight_unit(mouse_coords)          

    def highlight_unit(self, mouse_coords):
        if self.selected == True:
            self.highlight = True        

    def move(self, mouse_coords):
  
        if self.highlight:
            if mouse_coords[0] % 40 == 0 and mouse_coords[1] % 40 == 0:
                self.x_location = mouse_coords[0]
                self.y_location = mouse_coords[1]
            else:
                self.x_location = int(40 * math.floor(mouse_coords[0]/40))
                self.y_location = int(40 * math.floor(mouse_coords[1]/40))
        self.highlight = False
        self.selected = False


    def attack_unit(self, value):
        attack_coords = pygame.mouse.get_pos()
        print(attack_coords)
        print("Value", value)
        #if attack_coords
        print("ATTACK!")

    def show_health(self, unit):
        print(unit.hp)

        

    def recruit(self):
        pass

    def select_unit(self):
        self.highlight = True



class Elf(Unit):
    def __init__(self, window, player):
        super().__init__(self)
        self.player = player
        self.hp = 400
        self.attack = random.randint(4,20)
        self.armor = 10
        self.speed = 90
        self.attack_range = 0
        self.accuracy = 0
        self.game_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        self.unit_path = "/Grafika/elf.png"
        self.load_image()


    def attack(self):
        pass

    def load_image(self):
        self.image = pygame.image.load(self.game_dir + self.unit_path)

    @property
    def render(self):
        return self.image

    @property
    def rectangle(self):
        return self.image.get_rect(topleft = (self.x_location, self.y_location))
