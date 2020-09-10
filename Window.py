import pygame


class Window():
    def __init__(self, window_width, window_height, fullscreen):
        pygame.init()
        self.window_width = window_width
        self.window_height = window_height
        self.fullscreen = fullscreen
        self.window_init()

    def window_init(self):
        pygame.display.set_mode((self.window_width, self.window_height), display=self.fullscreen)


app = Window(400, 400, 0)




        