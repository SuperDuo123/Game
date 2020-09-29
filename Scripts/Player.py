import pygame



class Player:
    def __init__(self):
        self.army = []
        self.turn = False
        self.chosen_unit_id = None
        self.attacked_unit_id = None   

    def display_units(self):
    	print(self.army)

    def display_chosen_units(self):
    	print(f"Chosen unit: {self.chosen_unit_id}")
    	print(f"Attacked unit: {self.attacked_unit_id}")

    def show_units_hp(self, unit):
    	return unit.hp
        