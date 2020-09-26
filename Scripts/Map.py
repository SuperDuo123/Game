import pygame
import numpy as np
from settings import *
from Tile import *
import os
import random
import re
from pygame import surface, display, rect

class Map():

    def __init__(self, window, map_size):
        self.game_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        self.size = map_size
        print("Rozmiar mapy: "+str(self.size))
        self.map_array = np.chararray((self.size+2, self.size+2))               # ASCII array, maybe matrix?    # +2 because of the map border
        self.tile_array = [[0 for x in range(self.size+2)] for y in range(self.size+2)]             # 2D tile array, consists of Tile classes
        self.surface = pygame.Surface((tile_size*(self.size+2) , tile_size*(self.size+2)))          # visible map surface
        self.tile_types = {}                # NOT USED - dictiontary for tile types
        self.map_location_x = 0             # top left corner's coordinates
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
        # dragon nests
        self.dragon_image1 = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Smocze\smocze1.png").convert_alpha()
        self.dragon_image2 = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Smocze\smocze2.png").convert_alpha()
        self.dragon_image3 = pygame.image.load(fr"{self.game_dir}\Grafika\Krajobraz\Smocze\smocze3.png").convert_alpha()

    def generate(self):           # generates map using given tiles and map size
        # setting random seed for generator
        random.seed()
        # loading generator data from generator.txt
        self.load_generator_data()
        # creating a map with all the tiles with is_set = false -> used for checking if a tile can be overwritten
        self.generate_empty()
        
        # this section generates water -> mountains -> and then forests, in this order
        # so that forests can be overwritten with mountains etc.                ????????
        # generating water
        self.generate_water()
        # generating dragon nests
        self.generate_dragon_nests()
        # generating mountains and forests
        self.generate_single_chance_terrain()
        # THE REST - BORDER AND GRASS
        self.generate_surface()
        print(self.map_array)
        # writing to a text file
        self.save(self.map_array, "map.txt")
    
    def load_generator_data(self):
        f = open(fr"{self.game_dir}\Config\generator.txt")
        # reading data line by line and looking for a number at the end
        # water info
        self.lake_number_min = int(re.search(r'\d+', f.readline()).group())
        self.lake_number_max = int(re.search(r'\d+', f.readline()).group())
        self.lake_xSize_min = int(re.search(r'\d+', f.readline()).group())-2          # lake boundaries are not counted during generating
        self.lake_xSize_max = int(re.search(r'\d+', f.readline()).group())-2
        self.lake_ySize_min = int(re.search(r'\d+', f.readline()).group())-2
        self.lake_ySize_max = int(re.search(r'\d+', f.readline()).group())-2
        # forest info
        self.forest_chance_min = int(re.search(r'\d+', f.readline()).group())
        self.forest_chance_max = int(re.search(r'\d+', f.readline()).group())
        #mountain info
        self.mountain_chance_min = int(re.search(r'\d+', f.readline()).group())
        self.mountain_chance_max = int(re.search(r'\d+', f.readline()).group())
        f.close()

    def generate_empty(self):
        # first loop that creates all the tiles with is_set = false and borders
        for i in range(0, self.size+2):               
            for j in range(0, self.size+2):
                if i==0 or i==self.size+1 or j==0 or j==self.size+1:        # generates map outline, overwrites everthing   (TO DO)
                    self.map_array[i][j] = 'B'
                    self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "border", 0, self.mountain_image2, True)
                else:                                 # generates grass if a tile is empty
                    self.map_array[i][j] = 'G'
                    t = random.randint(1, 2)            # selecting random forest tile (there are 3 forest tiles)
                    if t==1:
                        self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "grass", 0, self.grass_image1, False)
                    else:
                        self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "grass", 0, self.grass_image2, False)
        
    def generate_dragon_nests(self):
        # generates nests, one of each type, loops until it can spawn it
        is_set=False
        while is_set!=True:
            xPos = random.randint(1, self.size)         # random index of tile
            yPos = random.randint(1, self.size)
            if self.tile_array[xPos][yPos].is_set==False:
                self.map_array[xPos][yPos] = 'D'
                self.tile_array[xPos][yPos] = Tile(xPos, yPos, xPos*tile_size, yPos*tile_size, "dragon nest", 0, self.dragon_image1, True)
                is_set=True
        is_set=False
        while is_set!=True:
            xPos = random.randint(1, self.size)         # random index of tile
            yPos = random.randint(1, self.size)
            if self.tile_array[xPos][yPos].is_set==False:
                self.map_array[xPos][yPos] = 'D'
                self.tile_array[xPos][yPos] = Tile(xPos, yPos, xPos*tile_size, yPos*tile_size, "dragon nest", 0, self.dragon_image2, True)
                is_set=True
        is_set=False
        while is_set!=True:
            xPos = random.randint(1, self.size)         # random index of tile
            yPos = random.randint(1, self.size)
            if self.tile_array[xPos][yPos].is_set==False:
                self.map_array[xPos][yPos] = 'D'
                self.tile_array[xPos][yPos] = Tile(xPos, yPos, xPos*tile_size, yPos*tile_size, "dragon nest", 0, self.dragon_image3, True)
                is_set=True

    def generate_water(self):
        # generates k lakes
        for k in range (0, random.randint(self.lake_number_min, self.lake_number_max)):       # number of lakes
            xSize = random.randint(self.lake_xSize_min, self.lake_xSize_max)                # number of vertical size of water 
            ySize = random.randint(self.lake_ySize_min, self.lake_ySize_max)                # number of horizontal size of water 
            xPos = random.randint(1, self.size-xSize)         # random index of 1st (top left) tile of water (DOES NOT COUNT WATER BORDERS - alse below)
            yPos = random.randint(1, self.size-ySize)         #   ---||---        # NOT USED BUT REMEMBER: maybe add -1 because of right or down lake water border!
            #print("WODA: "+str(xSize)+" "+str(ySize)+" "+str(xPos)+" "+str(yPos))
            is_empty = True
            for i in range (xPos-1, xPos+xSize+1):              # checks if there is place to generate a lake, if there isn't, it skips tha lake completely
                for j in range (yPos-1, yPos+ySize+1):          # -1 and +1 because or the lake border!
                    if self.tile_array[i][j].is_set==True:
                        is_empty = False
            if is_empty==True:
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
            else:
                print("Lake nr "+str(k+1)+" couldn't be generated!")
    
    ### NOT USED ###
    def generate_forests(self):
        for k in range (0, random.randint(self.forest_number_min, self.forest_number_max)):       # number of forests
            xSize = random.randint(self.forest_xSize_min, self.forest_xSize_max)                # number of vertical size of forest 
            ySize = random.randint(self.forest_ySize_min, self.forest_ySize_max)                # number of horizontal size of forest
            xPos = random.randint(1, self.size-xSize)         # random index of 1st (top left) tile of forest 
            yPos = random.randint(1, self.size-ySize)
            # forests don't have borders, so there is no need to check if all the tiles are empty before generating
            # just checking before each tile and if it's not empty -> just don't generate forest on that tile
            for i in range (xPos, xPos+xSize):
                for j in range (yPos, yPos+ySize):
                    if self.tile_array[i][j].is_set==False:
                        self.map_array[i][j] = 'F'
                        t = random.randint(1, 3)            # selecting random forest tile (there are 3 forest tiles)
                        if t==1:
                            self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "forest", 0, self.forest_image1, True)
                        elif t==2:
                            self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "forest", 0, self.forest_image2, True)
                        else:
                            self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "forest", 0, self.forest_image3, True)
    
    ### NOT USED ###
    def generate_mountains(self):
        # for each tile there is a chance of it being a mountain
        # mountains can't generate on water
        for i in range(0, self.size+2):               
            for j in range(0, self.size+2):
                chance = random.randint(1, 100)
                if self.tile_array[i][j].is_set==False and chance<=self.mountain_chance:
                    self.map_array[i][j] = 'M'
                    t = random.randint(1, 2)            # selecting random forest tile (there are 3 forest tiles)
                    if t==1:
                        self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "mountain", 0, self.mountain_image1, True)
                    else:
                        self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "mountain", 0, self.mountain_image2, True)
    
    def generate_single_chance_terrain(self):
        # generates terrain that takes only one tile and has its own spawn % chance
        forest_chance = random.randint(self.forest_chance_min, self.forest_chance_max)          # random spawn chance from between given values
        mountain_chance = random.randint(self.mountain_chance_min, self.mountain_chance_max)+forest_chance      # its cumulative
        for i in range(0, self.size+2):               
            for j in range(0, self.size+2):
                if self.tile_array[i][j].is_set==False:
                    chance = random.randint(1, 100)
                    if chance <= forest_chance:             # forest
                        self.map_array[i][j] = 'F'
                        t = random.randint(1, 3)            # selecting random forest tile (there are 3 forest tiles)
                        if t==1:
                            self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "forest", 0, self.forest_image1, True)
                        elif t==2:
                            self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "forest", 0, self.forest_image2, True)
                        else:
                            self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "forest", 0, self.forest_image3, True)
                    elif chance <= mountain_chance:          # mountain
                        self.map_array[i][j] = 'M'
                        t = random.randint(1, 2)            # selecting random forest tile (there are 3 forest tiles)
                        if t==1:
                            self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "mountain", 0, self.mountain_image1, True)
                        else:
                            self.tile_array[i][j] = Tile(i, j, i*tile_size, j*tile_size, "mountain", 0, self.mountain_image2, True)
                    else:               # remains grass
                        pass

    def generate_surface(self):
        #creates the surface of a whole map using images from all generated tiles in previous functions
        for i in range(0, self.size+2):               
            for j in range(0, self.size+2):
                self.surface.blit(self.tile_array[i][j].image, (self.tile_array[i][j].pos_x, self.tile_array[i][j].pos_y))

    def save(self, array, file_name):
        map_file = open(fr"{self.game_dir}\Maps\{file_name}", "w+")
        for i in range(0, self.size+2):               
            for j in range(0, self.size+2):
                map_file.write(str(self.map_array[i][j]))
            map_file.write("\n")