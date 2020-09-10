import pygame


class Window():
    def __init__(self, window_width, window_height, fullscreen):
        pygame.init()
        self.window_width = window_width
        self.window_height = window_height
        self.fullscreen = fullscreen
        self.window_init()
        self.mainloop()

    def window_init(self):
        #FULLSCREEN maximizes the window without fitting the resolution
        #pygame.FULLSCREEN fit the resolution as well as maximizing
        if self.fullscreen:
            pygame.display.set_mode((self.window_width, self.window_height), pygame.FULLSCREEN)
        else:
            pygame.display.set_mode((self.window_width, self.window_height))

    def mainloop(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False


app = Window(400, 400, 0)




        