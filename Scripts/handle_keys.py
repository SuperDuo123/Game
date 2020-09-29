import pygame
from Unit import *

class Handle_keys:
    def __init__(self, window, player):
        self.window = window
        self.player = player
        self.select = False
        #self.menu = menu        
        #print("Atrybut handle_keys", self.menu)
    def handle(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    """Left Mouse Button is associated with id. 1 of event.button. It's in-built function of pygame."""
                    if event.button == 1: #Left Mouse Button Click
                        mouse_coords = pygame.mouse.get_pos()
                        if self.window.blit_menu == True:
                            self.window.menu.button_event_listener(mouse_coords)
                        print(mouse_coords)

                        if self.window.blit_map == True:
                            """moving unit"""
                            
                            for chosen_unit_id, unit in enumerate(self.player.army):
                                unit.unit_interact(mouse_coords, chosen_unit_id)



                    if event.button == 2: #Middle Mouse Button Click
                        pass

                    if event.button == 3: #Right Mouse Button Click

                        for attacked_unit_id, unit in enumerate(self.player.army):
                            # if unit.selected:
                            unit.attack_unit(attacked_unit_id)


                    if event.button == 4: #Scroll Up
                        pass
                    if event.button == 5: #Scroll Down
                        pass

                """Activates when keyboard key is released"""
                if event.type == pygame.KEYUP:
                    """Escape button for calling in-game Menu"""
                    if event.key == pygame.K_ESCAPE:
                        print("ESC Clicked")
                        self.window.run = False
                    
                    if event.key == pygame.K_p:
                        print("New unit created")
                        self.window.create_u = True
                    #Check stats and other unit coordinates
                    if event.key == pygame.K_h:
                        for unit_id, unit in enumerate(self.player.army):
                            print(f"HP of unit {unit_id}: {self.player.show_units_hp(unit)}")
                        self.player.display_chosen_units()




                """Activates when keyboard key is pressed"""
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        if self.window.blit_map:
                            self.window.map.map_location_y += 40
                            for unit in self.player.army:
                                unit.y_location += 40
                               
                            

                    if event.key == pygame.K_s:
                        if self.window.blit_map:
                            self.window.map.map_location_y -= 40
                            for unit in self.player.army:
                                unit.y_location -= 40
                              

                            
                    if event.key == pygame.K_a:
                        if self.window.blit_map:
                            self.window.map.map_location_x += 40
                            for unit in self.player.army:
                                unit.x_location += 40
                               
                            

                    if event.key == pygame.K_d:
                        if self.window.blit_map:
                            self.window.map.map_location_x -= 40
                            for unit in self.player.army:
                                unit.x_location -= 40
