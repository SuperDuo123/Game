import pygame
from settings import *
from pygame import surface, display, rect


class Tile():
    
    def __init__(self, tile_id_x, tile_id_y, tile_pos_x, tile_pos_y, tile_type, tile_coat, tile_image, tile_set):
        self.id_x = tile_id_x              # id in tile array
        self.id_y = tile_id_y
        self.pos_x = tile_pos_x            # position in pixels
        self.pos_y = tile_pos_y
        self.type = tile_type              # etc grass, water, city
        self.coat = tile_coat              # 0 - no coat, 1 - dark fog (unknown terrain), 2 - war fog (???)
        self.image = tile_image            # image of given tile, eg picture of grass, used in Map class to make a map surface
        self.is_set = tile_set             # if a tile can be overwritten or not
        if "water" in self.type or "mountain" in self.type:     # checks if you can pass through the tile
            self.movement = 0
        else:
            self.movement = 1
