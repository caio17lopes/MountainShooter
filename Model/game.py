#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
from Model.Menu import Menu
class Game:
    def __init__(self):
        pg.init()
        window = pg.display.set_mode(size=(600,400))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run
            pass
            
            #check for all events
            # for event in pg.event.get():
            #     if event.type ==pg.QUIT:
            #         pg.quit()# close window
            #         quit() # end game