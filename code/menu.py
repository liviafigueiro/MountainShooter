#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png') #carregar imagem
        self.rect = self.surf.get_rect(left=0, top=0) #criar retangulo


    def run(self, ):
        pygame.mixer.music.load('./asset/Menu.mp3')  # carregar a musica
        pygame.mixer.music.play(-1)  # fazer a musica tocar, -1 deixa ela tocando infinita
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # colocar imagem no retangulo
            self.menu_text(55,"Mountain",COLOR_ORANGE,((WIN_WIDTH/2),70))
            self.menu_text(55, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 110))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20,MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200+25*i))
                #vai percorrer cada frase da lista e a cada posição somar 30 * o num da posição


            pygame.display.flip() #atualizar imagem na tela

            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #close window
                    quit() #end pygame

    def menu_text(self, text_size: int, text:str, text_color:tuple, text_center_pos:tuple):
        text_font: Font = pygame.font.SysFont('Lucinda Sans Typewriter', text_size) #diz qual fonte utilizar
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()#faz a fonte virar uma imagem
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)#criar um retangulo para a imagem
        self.window.blit(source=text_surf, dest=text_rect)#atualizar