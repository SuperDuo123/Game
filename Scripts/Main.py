from Window import Window
from settings import *
# launch program from this file



def main():
    app = Window(window_width,window_height,0)
    # window initialization
    app.window_init()
    # load menu images and render menu background
    app.load_menu()
    app.load_keys()
    # mainloop
    app.mainloop()


if __name__ == "__main__":
    main()

#oof
