import pygame
import numpy as np
from settings import *
#from Window import *
from Tile import *
import os
import random
from pygame import surface, display, rect

map_size_test = 5
print(map_size_test)

class Map():

    def __init__(self, window, map_size):
        self.game_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        self.size = map_size
        print("Rozmiar mapy: "+str(self.size))
        self.map_array = np.chararray((self.size+2, self.size+2))                   # +2 because of the map border
        self.tile_array = [[0 for x in range(self.size+2)] for y in range(self.size+2)]
        self.surface = pygame.Surface((tile_size*(self.size+2) , tile_size*(self.size+2)))
        self.tile_types = {}
        self.map_location_x = 0
        self.map_location_y = 0
        
    
    def load_tile_types(self):              # loades all tile background images
        self.border_image1 = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Brzegi\brzeg.png").convert_alpha()
        # forest
        self.forest_image1 = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Las\las1.png").convert_alpha()
        self.forest_image2 = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Las\las2.png").convert_alpha()
        self.forest_image3 = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Las\las3.png").convert_alpha()
        # mountains
        self.mountain_image1 = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Gory\gory1.png").convert_alpha()
        self.mountain_image2 = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Gory\gory2.png").convert_alpha()
        # grass
        self.grass_image1 = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Trawa\trawa1.png").convert_alpha()
        self.grass_image2 = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Trawa\trawa2.png").convert_alpha()
        # water
        self.water_image1 = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Woda\woda1.png").convert_alpha()
        self.water_image2 = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Woda\woda2.png").convert_alpha()
        self.water_image3 = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Woda\woda3.png").convert_alpha()
        self.water_image4 = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Woda\woda4.png").convert_alpha()
        self.water_image_up = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Woda\plaza1.png").convert_alpha()
        self.water_image_down = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Woda\plaza2.png").convert_alpha()
        self.water_image_left = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Woda\plaza4.png").convert_alpha()
        self.water_image_right = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Woda\plaza3.png").convert_alpha()
        self.water_image_up_left = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Woda\rogplaza1.png").convert_alpha()
        self.water_image_up_right = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Woda\rogplaza2.png").convert_alpha()
        self.water_image_down_left = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Woda\rogplaza4.png").convert_alpha()
        self.water_image_down_right = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Woda\rogplaza3.png").convert_alpha()

    def generate(self):           # generates map using given tiles and map size
        random.seed()
        # first loop that creates all the tiles with is_set = false
        for i in range(0, self.size+2):               
            for j in range(0, self.size+2):
                self.map_array[i][j] = 'X'
                self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, 0, 0, self.grass_image1, False)
        
        # this section generates forests -> mountains -> and then water, in this order
        # so that forests can be overwritten with mountains etc.                ????????

        # WATER
        for k in range (0, random.randint(1, 2)):       # !number of lakes
            xSize = random.randint(1, 2)                # !change upper bound to variable       number of vertical size of water 
            ySize = random.randint(1, 3)                # !change upper bound to variable       number of horizontal size of water 
            xPos = random.randint(1, self.size-xSize)         # random index of 1st (top left) tile of water     (DOES NOT COUNT WATER BORDERS) below also
            yPos = random.randint(1, self.size-ySize)         #   ---||---        # NOT USED BUT REMEMBER: maybe add -1 because of right or down lake water border!
            print("WODA: "+str(xSize)+" "+str(ySize)+" "+str(xPos)+" "+str(yPos))
            for i in range (xPos, xPos+xSize):
                for j in range (yPos, yPos+ySize):
                    self.map_array[i][j] = 'W'
                    t = random.randint(1, 4)            # selecting random water tile (there are 4 water tiles)
                    if t==1:
                        self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "water", 0, self.water_image1, True)
                    elif t==2:
                        self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "water", 0, self.water_image2, True)
                    elif t==3:
                        self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "water", 0, self.water_image3, True)
                    else:
                        self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "water", 0, self.water_image4, True)
            # WATER BORDER
            for i in range (1, self.size+1):
                for j in range (1, self.size+1):
                    if self.tile_array[i][j].type!="water" and self.tile_array[i][j].type!="water border" and self.tile_array[i+1][j].type=="water":
                        self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "water border", 0, self.water_image_left, True)
                    if self.tile_array[i][j].type!="water" and self.tile_array[i][j].type!="water border" and self.tile_array[i-1][j].type=="water":
                        self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "water border", 0, self.water_image_right, True)
                    if self.tile_array[i][j].type!="water" and self.tile_array[i][j].type!="water border" and self.tile_array[i][j+1].type=="water":
                        self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "water border", 0, self.water_image_up, True)
                    if self.tile_array[i][j].type!="water" and self.tile_array[i][j].type!="water border" and self.tile_array[i][j-1].type=="water":
                        self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "water border", 0, self.water_image_down, True)
                    if self.tile_array[i][j].type!="water" and self.tile_array[i][j].type!="water border" and self.tile_array[i+1][j+1].type=="water":
                        self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "water border", 0, self.water_image_up_left, True)
                    if self.tile_array[i][j].type!="water" and self.tile_array[i][j].type!="water border" and self.tile_array[i+1][j-1].type=="water":
                        self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "water border", 0, self.water_image_down_left, True)
                    if self.tile_array[i][j].type!="water" and self.tile_array[i][j].type!="water border" and self.tile_array[i-1][j+1].type=="water":
                        self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "water border", 0, self.water_image_up_right, True)
                    if self.tile_array[i][j].type!="water" and self.tile_array[i][j].type!="water border" and self.tile_array[i-1][j-1].type=="water":
                        self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "water border", 0, self.water_image_down_right, True)
            # !!BUG!! when intercepting of 2 lakes -> TO DO

        # THE REST - BORDER AND GRASS
        for i in range(0, self.size+2):               # creates tiles with given parameters
            for j in range(0, self.size+2):
                if i==0 or i==self.size+1 or j==0 or j==self.size+1:        # generates map outline, overwrites everthing         (TO DO)
                    self.map_array[i][j] = 'B'
                    self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "border", 0, self.border_image1, True)
                else:                                 # generates grass if a tile is empty
                    if self.tile_array[i][j].is_set==False:
                        self.map_array[i][j] = 'G'
                        self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "grass", 0, self.grass_image1, True)
                    pass 
                self.surface.blit(self.tile_array[i][j].image, (self.tile_array[i][j].pos_x, self.tile_array[i][j].pos_y))  #creates the surface of a whole map using images from all generated tiles
        print(self.map_array)
    