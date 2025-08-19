#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
import pygame as pg 
class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/Menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        
        pg.mixer_music.load('./assets/menu.mp3')
        pg.mixer_music.play(-1)# -1 deixa a musica tocando por tempo indefinido 
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            pygame.display.flip()

            #check for all events
            for event in pg.event.get():
                if event.type ==pg.QUIT:
                    pg.quit()# close window
                    quit() # end game
        
    def menu_text(sekf, text_size: int, text: str, text_color: tuple, text_center_pos:tuple,):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewrite", size=text_size)
        text_surf: Surface = text_font.render(text,antialias :True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center = text_center_pos)
        self.window.blit(source = text_surf, dest=text_rect)