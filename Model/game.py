#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
from Model.Menu import Menu
from Model.Comst import WIN_WIDTH , WIN_HEIGHT


class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(WIN_WIDTH,WIN_HEIGHT ))

    def run(self):
        
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            
