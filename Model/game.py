#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
class Game:
    def __init__(self):
        self.window = None

    def run(self, ):
        print('Setup Start')
        pg.init()
        window = pg.display.set_mode(size=(600,400))
        print('Setup End')

        print('Loop Start')
        while True:
            #check for all events
            for event in pg.event.get():
                if event.type ==pg.QUIT:
                    pg.quit()# close window
                    quit() # end game