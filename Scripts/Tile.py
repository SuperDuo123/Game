import pygame
from settings import *
from Window import *
from pygame import surface, display, rect


class Tile():
    
    def __init__(self, tile_id_x, tile_id_y, tile_pos_x, tile_pos_y, tile_type, tile_coat, tile_image):
        self.id_x = tile_id_x              # id in tile array
        self.id_y = tile_id_y
        self.pos_x = tile_pos_x            # position in pixels
        self.pos_y = tile_pos_y
        self.type = tile_type              # etc grass, water, city
        self.coat = tile_coat              # 0 - no coat, 1 - dark fog (unknown terrain), 2 - war fog (???)
        self.image = tile_image            # image of given tile, eg picture of grass, used in Map class to make a map surface
    
    #def load_image(self)
