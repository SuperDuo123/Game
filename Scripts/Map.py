import pygame
import numpy as np
from settings import *
from Window import *
from Tile import *
from pygame import surface, display, rect

map_size_test = 5
print(map_size_test)

class Map():

    def __init__(self, map_size):
        self.size = map_size
        self.map_array = np.chararray((self.size, self.size))
        self.tile_array = [[], []]
        self.surface = pygame.Surface((tile_size*self.size , tile_size*self.size))
        self.tile_types = {}
        #print(self.map_array)
        self.load_tile_types()
        self.generate()
        print(self.map_array)
    
    def load_tile_types(self):              # loades all tile background images
        self.border_image1 = pygame.image.load("../Grafika/Krajobraz/Brzegi/brzeg.png").convert_alpha()
        # forest
        self.forest_image1 = pygame.image.load("../Grafika/Krajobraz/Las/las1.png").convert_alpha()
        self.forest_image2 = pygame.image.load("../Grafika/Krajobraz/Las/las2.png").convert_alpha()
        self.forest_image3 = pygame.image.load("../Grafika/Krajobraz/Las/las3.png").convert_alpha()
        # mountains
        self.mountain_image1 = pygame.image.load("../Grafika/Krajobraz/Gory/gory1.png").convert_alpha()
        self.mountain_image2 = pygame.image.load("../Grafika/Krajobraz/Gory/gory2.png").convert_alpha()
        # grass
        self.grass_image1 = pygame.image.load("../Grafika/Krajobraz/Trawa/trawa1.png").convert_alpha()
        self.grass_image2 = pygame.image.load("../Grafika/Krajobraz/Trawa/trawa2.png").convert_alpha()

    def generate(self):           # generates map using given tiles and map size
        for i in range(0, self.size):
            for j in range(0, self.size):
                if i==0 or i==self.size-1 or j==0 or j==self.size-1: # generates map outline           (TO DO)
                    self.map_array[i, j] = 'X'
                    self.tile_array[i, j] = Tile(i, j, i*tile_size, j*tile_size, 0, 0, self.border_image1) 
                else:
                    self.map_array[i, j] = 'O'
                    self.tile_array[i, j] = Tile(i, j, i*tile_size, j*tile_size, 0, 0, self.grass_image1) 
                self.surface.blit(tile_array[i, j].image, (tile_array[i, j].pos_x, tile_array[i, j].pos_y))

Map(map_size_test)