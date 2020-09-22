import pygame
from Unit import *

class Handle_keys:
    def __init__(self, window):
        self.window = window
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
                            for unit in self.window.army:
                                if unit.rectangle.x < mouse_coords[0] and unit.rectangle.x + unit.rectangle.width > mouse_coords[0]:
                                    if unit.rectangle.y < mouse_coords[1] and unit.rectangle.y + unit.rectangle.width > mouse_coords[1]:
                                        self.select = True
                                # else:
                                #     unit.selected = False
                                
                                if unit.selected:
                                    unit.move(mouse_coords)
                                    unit.selected = False

                                if self.select == True:
                                    unit.selected = True
                                    self.select = False
                            #######################################################################################    
                                
                                
                                


                            #unit select
                            #unit move
                        #self.menu.button_handler()
                        print()

                    if event.button == 2: #Middle Mouse Button Click
                        pass

                    if event.button == 3: #Right Mouse Button Click
                        pass
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


                """Activates when keyboard key is pressed"""
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        if self.window.blit_map:
                            self.window.map.map_location_y += 40
                            for unit in self.window.army:
                                unit.y_location += 40
                            

                    if event.key == pygame.K_s:
                        if self.window.blit_map:
                            self.window.map.map_location_y -= 40
                            for unit in self.window.army:
                                unit.y_location -= 40

                            
                    if event.key == pygame.K_a:
                        if self.window.blit_map:
                            self.window.map.map_location_x += 40
                            for unit in self.window.army:
                                unit.x_location += 40
                            

                    if event.key == pygame.K_d:
                        if self.window.blit_map:
                            self.window.map.map_location_x -= 40
                            for unit in self.window.army:
                                unit.x_location -= 40
                            