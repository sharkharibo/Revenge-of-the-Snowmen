import pygame, sys
from pygame.locals import *
from abc import ABC, abstractmethod
import random
import math
import time
import subprocess
pygame.init()
pygame.display.set_caption('Pygame Window')

clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 30)
WINDOW_SIZE = (1280, 720)
WIDTH=1280
HEIGHT=720
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
display = pygame.Surface((300, 200))
black=(0,0,0)
RED=(255,0,0)
# Charger l'image de sprite sheet
bg = pygame.image.load("fond.png").convert_alpha()

sprite_sheet = pygame.image.load('player_animer.png')
lose=pygame.image.load("lose.gif").convert_alpha()
danger_image = pygame.image.load('danger.png').convert_alpha()
mat_image = pygame.image.load('mat.png').convert_alpha()
bas_image = pygame.image.load('bas.png').convert_alpha()
tp_image = pygame.image.load('tp.png').convert_alpha()
apart = pygame.image.load('appartement.png').convert_alpha()
apart_alu = pygame.image.load('appartementalu.png').convert_alpha()
ville = pygame.image.load('tatooine.png').convert_alpha()
# Découper les frames de 16x16 à partir de la sprite sheet

frame_width = 16
frame_height = 23
player_images = []

m_alume=0
a_un_alu=0
a_deux_alu=0
for i in range(10):  # Si tu as 3 frames
    frame = sprite_sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
    player_images.append(frame)


#player_image.set_colorkey((255, 255, 255))

display.blit(bg, (0,0))
screen.blit(bg, (0, 0))
grass_image = pygame.image.load('grass_snow.png')
TILE_SIZE = grass_image.get_width()

dirt_image = pygame.image.load('dirt3.png')
cadeau_image = pygame.image.load("gift_type1.png").convert_alpha()
cadeau_open = pygame.image.load("gift_type2.png").convert_alpha()
pique_image=pygame.image.load("piques.png").convert_alpha()
coeur=pygame.image.load("coeur.png").convert_alpha()
maison=pygame.image.load("maison.png").convert_alpha()
maison_alu=pygame.image.load("maisonalu.png").convert_alpha()
interdit=pygame.image.load("interdit.png").convert_alpha()
haut=pygame.image.load("haut.png").convert_alpha()
droite=pygame.image.load("droite.png").convert_alpha()
nombre_cadeaux=0
vies=3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

game_map = [
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','0','0','0','0','1','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','2','0','0','0','1','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','0','0','0','2','1','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','0','0','0','0','1','0','0','0','0','2','2','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','0','0','1','1','1','1','1','1','1','2','0','0','0','1','0','0','0','0','1','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','1','1','0','0','1','1','1','1','0','0','1','0','0','0','0','1','0','0','0','0','1','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','1','1','0','0','0','1','1','1','1','0','0','1','0','0','0','0','1','0','0','0','0','1','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','1','1','0','0','0','0','1','1','1','1','0','0','1','0','0','0','2','1','0','0','0','0','1','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','0','0','0','0','0','0','0','0','0','0','2','1','1','0','0','0','0','2','1','1','1','1','0','0','1','0','0','0','0','1','0','0','0','0','1','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','1','0','0','0','0','0','0','0','0','0','2','1','1','0','0','0','0','2','1','1','1','1','1','0','0','1','2','0','0','0','1','0','0','0','0','1','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0','0','0','2','1','1','0','0','0','0','2','1','1','1','1','1','1','0','0','1','0','0','0','0','1','0','0','0','0','1','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','1','1','0','0','0','0','0','0','0','2','1','1','0','0','0','0','2','1','1','1','1','0','0','0','0','0','1','0','0','0','0','1','0','0','0','0','1','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','0','0','0','0','0','0','2','1','1','0','0','0','0','2','1','1','1','1','1','0','0','0','0','0','1','0','0','0','2','1','0','0','0','0','1','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','0','0','2','0','0','0','1','0','0','0','0','2','2','1','1','1','1','1','1','0','0','0','0','0','1','2','0','0','0','1','0','0','0','0','1','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','3','3','1','1','1','1','1','0','0','1','3','3','3','1','0','0','0','2','1','1','1','1','1','1','1','1','0','0','1','0','0','1','0','0','0','0','1','0','0','0','0','1','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['2','0','0','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','0','0','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','0','0','1','1','1','1','0','0','0','2','1','1','1','1','1','1','1','1','1','0','2','1','0','0','1','0','2','0','0','1','0','0','0','0','1','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['1','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','1','0','0','1','0','0','0','0','0','2','1','1','1','1','1','1','1','1','1','1','0','0','1','0','0','1','0','0','0','0','1','0','0','0','0','1','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['1','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','1','1','0','0','1','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','0','0','1','0','0','1','0','0','0','2','1','0','0','0','0','1','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['1','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','1','1','1','0','0','1','1','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','2','0','1','0','0','1','0','0','0','0','1','0','0','0','0','1','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['1','3','3','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','1','1','1','1','0','0','1','1','2','0','0','0','0','0','1','1','1','1','1','1','1','1','1','0','0','1','0','0','1','0','0','0','0','1','0','0','0','0','1','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','1','1','1','2','0','0','0','0','0','1','1','1','1','1','1','1','1','0','0','1','0','0','1','0','2','0','0','1','0','0','0','0','1','3','3','3','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','1','1','1','1','2','0','0','0','0','0','1','1','1','1','1','1','1','0','2','1','0','0','1','0','0','0','0','1','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','1','1','1','1','1','2','0','0','0','0','0','1','1','1','1','1','1','0','0','1','0','0','1','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','1','1','1','1','1','1','2','0','0','0','0','0','0','0','0','0','0','0','0','1','0','0','1','0','0','0','2','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','2','0','0','0','0','2','2','2','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','1','1','1','1','1','1','1','2','0','0','0','0','0','0','0','0','0','2','0','1','0','0','1','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','1','0','0','0','0','1','1','1','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','1','1','1','1','1','1','1','1','2','0','0','0','0','0','0','0','0','0','0','1','0','0','1','2','0','0','0','1','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','1','0','0','0','0','1','1','1','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','1','1','1','1','1','1','1','1','1','2','0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','1','0','0','0','0','1','0','0','0','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','3','3','3','3','3','3','3','3','3','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','3','3','1','3','3','3','3','1','1','1','3','3','3','3','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','3','3','1','1','1','1','1','1','1','1','1','1','2','0','0','0','0','0','0','0','2','1','3','0','0','0','0','0','2','1','3','3','3','3','1','3','3','3','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2',],
]

class Collision:
    def collision_test(rect, tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def move(rect, movement, tiles):
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        rect.x += movement[0]
        hit_list = Collision.collision_test(rect, tiles)
        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True
        rect.y += movement[1]
        hit_list = Collision.collision_test(rect, tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            elif movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
        return rect, collision_types


class Personnage:
    def __init__(self, x, y, images):
        self.images = images  # Liste d'images pour l'animation
        self.image = self.images[0]  # Image initiale (première image)
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.movement = [0, 0]
        self.y_momentum = 0
        self.air_timer = 0
        self.animation_frame = 0  # Variable pour suivre l'index de l'image d'animation
        self.frame_time = 0  # Variable pour contrôler la durée de chaque frame
        self.facing_left = False  # Variable pour savoir si le personnage regarde à gauche

    def update(self, keys, tiles):
        self.movement = [0, 0]

        # Gestion du mouvement horizontal
        if keys[K_RIGHT]:
            self.movement[0] += 2
            self.animate('right')  # Animer à droite
        elif keys[K_LEFT]:
            self.movement[0] -= 2
            self.animate('left')  # Animer à gauche
        else:
            self.animation_frame = 0  # Reste sur la première image si aucun mouvement horizontal

        # Gestion du mouvement vertical (gravité)
        self.movement[1] += self.y_momentum
        self.y_momentum += 0.2
        if self.y_momentum > 3:
            self.y_momentum = 3
        self.rect, collisions = Collision.move(self.rect, self.movement, tiles)

        if collisions['bottom'] or collisions['top']:
            self.y_momentum = 0
            self.air_timer = 0
        else:
            self.air_timer += 1

    def animate(self, direction):
        """Animer le personnage en fonction du mouvement."""
        if direction == 'right':
            # Si on va à droite, alterner les images de droite
            if self.frame_time % 10 == 0:  # Contrôle du temps entre les frames
                self.animation_frame += 1
                if self.animation_frame >= len(self.images):  # Si on atteint la fin des frames
                    self.animation_frame = 0
            self.facing_left = False  # Le personnage fait face à droite
        elif direction == 'left':
            # Si on va à gauche, alterner les images de gauche
            if self.frame_time % 10 == 0:
                self.animation_frame += 1
                if self.animation_frame >= len(self.images):
                    self.animation_frame = 0
            self.facing_left = True  # Le personnage fait face à gauche

        # Mettre à jour l'image du personnage
        self.image = self.images[self.animation_frame]
        
        # Si le personnage se déplace vers la gauche, inverser l'image horizontalement
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)

        self.frame_time += 1  # Incrémenter le temps entre les frames

    def jump(self):
        if self.air_timer < 6:
            self.y_momentum = -5

    def draw(self, surface, camera):
        surface.blit(self.image, (self.rect.x - camera.offset.x, self.rect.y - camera.offset.y))




class Camera:
    def __init__(self, player):
        self.player = player
        self.offset = pygame.math.Vector2(0, 0)
        self.offset_float = pygame.math.Vector2(0, 0)
        self.DISPLAY_W, self.DISPLAY_H = 300, 200
        self.CONST = pygame.math.Vector2(-self.DISPLAY_W / 2 + player.rect.w / 2, -self.DISPLAY_H / 2 + player.rect.h / 2)

    def setmethod(self, method):
        self.method = method

    def scroll(self):
        self.method.scroll()


class CamScroll(ABC):
    def __init__(self, camera, player):
        self.camera = camera
        self.player = player


    def scroll(self):
        pass


class Follow(CamScroll):
    def scroll(self):
        # Taille du niveau
        map_width = len(game_map[0]) * TILE_SIZE
        map_height = len(game_map) * TILE_SIZE

        # Suivi du joueur avec limites
        self.camera.offset_float.x = max(0, min(self.player.rect.x - self.camera.DISPLAY_W // 2,map_width - self.camera.DISPLAY_W))
        self.camera.offset_float.y = max(0, min(self.player.rect.y - self.camera.DISPLAY_H // 2,map_height - self.camera.DISPLAY_H))


        # Mise à jour de l'offset
        self.camera.offset.x, self.camera.offset.y = int(self.camera.offset_float.x), int(self.camera.offset_float.y)

class Cadeau:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = pygame.Rect(x, y, image.get_width(), image.get_height())

    def draw(self, surface, camera):
        """Affiche le cadeau à l'écran, en tenant compte de la caméra."""
        surface.blit(self.image, (self.rect.x - camera.offset.x, self.rect.y - camera.offset.y))

    def check_collision(self, player):
        return self.rect.colliderect(player.rect)

class Canon:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 6
        self.projectiles = []
        # Charger l'image du bonhomme de neige et définir le rectangle de collision
        self.image = pygame.image.load("snowman.png").convert_alpha()
        self.rect = pygame.Rect(x - self.image.get_width() / 2, y - self.image.get_height() / 2, self.image.get_width(), self.image.get_height())

    def tirer(self):
        # Tirer avec un angle entre 45° et 60° pour avoir une trajectoire en cloche vers la gauche
        angle = random.uniform(45, 60)  # Angle entre 45° et 60° (vers la gauche)
        radian_angle = math.radians(angle)
        velocity_x = -self.speed * math.cos(radian_angle)  # Vitesse horizontale vers la gauche
        velocity_y = -self.speed * math.sin(radian_angle)  # Vitesse verticale vers le haut
        projectile = Projectile(self.x, self.y, velocity_x, velocity_y)
        self.projectiles.append(projectile)

    def update(self):
        for projectile in self.projectiles:
            projectile.update()
        # Mettre à jour la position du rectangle
        self.rect.x = self.x - self.image.get_width() / 2
        self.rect.y = self.y - self.image.get_height() / 2

    def draw(self, display, camera):
        # Calculer les coordonnées ajustées en fonction de la caméra
        adjusted_x = self.x - camera.offset.x
        adjusted_y = self.y - camera.offset.y
        
        # Dessiner le bonhomme de neige à la position ajustée
        display.blit(self.image, (adjusted_x - self.image.get_width() / 2, adjusted_y - self.image.get_height() / 2))
        
        # Dessiner les projectiles
        for projectile in self.projectiles:
            projectile.draw(display, camera)

    def check_collision(self, player):
        """Vérifie si le canon entre en collision avec le joueur."""
        return self.rect.colliderect(player.rect)

# Classe Projectile
class Projectile:
    def __init__(self, x, y, velocity_x, velocity_y):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x  # Vitesse horizontale (vers la gauche)
        self.velocity_y = velocity_y  # Vitesse verticale (vers le haut au début)
        self.rect = pygame.Rect(self.x, self.y, 8, 8)  # Rectangle pour le projectile

    def update(self):
        # Mise à jour de la position en fonction de la vitesse
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.rect.topleft = (self.x, self.y)

        # Gravité : affecte la vitesse verticale pour simuler la chute
        self.velocity_y += 0.5  # Augmenter la gravité pour une chute plus rapide

    def draw(self, screen, camera):
        # Dessiner le projectile en tenant compte de la caméra
        adjusted_x = self.x - camera.offset.x
        adjusted_y = self.y - camera.offset.y
        pygame.draw.circle(screen, WHITE, (int(adjusted_x), int(adjusted_y)), 4)

    def check_collision(self, player):
        """Vérifie si le projectile entre en collision avec le joueur."""
        return self.rect.colliderect(player.rect)



class Tire:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.projectiles = []  # Liste pour stocker les projectiles sous forme de dictionnaires

    def shoot(self):
        """Tire une balle jaune quand la touche T est pressée."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_t]:  # Si la touche T est pressée
            # Ajouter un projectile à la liste (au moment du tir, à la position du joueur)
            self.projectiles.append({'x': self.x, 'y': self.y, 'velocity_x': 5, 'velocity_y': 0})

        # Mise à jour des projectiles
        for projectile in self.projectiles[:]:
            projectile['x'] += projectile['velocity_x']  # Déplacer horizontalement

            # Vérification si la balle est hors de l'écran
            if projectile['x'] < 0 or projectile['x'] > 800:  # Si hors écran en largeur
                self.projectiles.remove(projectile)

            # Vérification si la balle touche un canon
            for canon in canons:
                if pygame.Rect(projectile['x'], projectile['y'], 8, 8).colliderect(canon.rect):
                    self.projectiles.remove(projectile)

    def draw(self, screen, camera):
        """Dessine les projectiles à l'écran."""
        for projectile in self.projectiles:
            adjusted_x = projectile['x'] - camera.offset.x
            adjusted_y = projectile['y'] - camera.offset.y
            pygame.draw.circle(screen, (255, 255, 0), (int(adjusted_x), int(adjusted_y)), 4)  # Balle jaune
class Tire:
    def __init__(self):
        self.projectiles = []  # Liste pour stocker les projectiles

    def tirer(self, joueur):
        """Crée un projectile aux coordonnées du joueur."""
        self.projectiles.append({'x': joueur.rect.centerx, 'y': joueur.rect.centery, 'vx': 6, 'vy': 0})

    def update(self, camera, canons):
        """Met à jour les projectiles et gère leurs collisions."""
        for projectile in self.projectiles[:]:  # Utilisation d'une copie pour itération sûre
            # Mise à jour des coordonnées
            projectile['x'] += projectile['vx']
            projectile['y'] += projectile['vy']

            # Vérifie si le projectile sort de l'écran visible
            if (projectile['x'] < camera.offset.x or
                    projectile['x'] > camera.offset.x + camera.DISPLAY_W or
                    projectile['y'] < camera.offset.y or
                    projectile['y'] > camera.offset.y + camera.DISPLAY_H):
                self.projectiles.remove(projectile)
                continue

            # Vérifie la collision avec les canons
            for canon in canons[:]:  # Copie pour éviter la modification simultanée
                if canon.rect.collidepoint(projectile['x'], projectile['y']):
                    canons.remove(canon)  # Supprime le canon
                    self.projectiles.remove(projectile)  # Supprime le projectile
                    break

    def draw(self, display, camera):
        """Dessine les projectiles sur l'écran."""
        for projectile in self.projectiles:
            adjusted_x = projectile['x'] - camera.offset.x
            adjusted_y = projectile['y'] - camera.offset.y
            pygame.draw.circle(display, (255, 255, 0), (int(adjusted_x), int(adjusted_y)), 5)


player = Personnage(50, 50, player_images)
camera = Camera(player)
camera.setmethod(Follow(camera, player))
balls = []
tire = Tire()
# Définir les cadeaux en dehors de la boucle principale
cadeaux = [Cadeau(50, 255, cadeau_image), Cadeau(340, 255, cadeau_image),Cadeau(300, 255, cadeau_image), Cadeau(265, 255, cadeau_image),Cadeau(592, 239, cadeau_image),Cadeau(208, 463, cadeau_image),Cadeau(1120, 400, cadeau_image),Cadeau(1010, 400, cadeau_image)]
# Liste pour stocker plusieurs canons
canons = [Canon(645, 273), Canon(200, 256), Canon(1492, 225),Canon(1084, 400),Canon(2154, 400)]
en_cour=True
perdu=False
while en_cour == True:
    if vies > 0:
        display.blit(bg, (0,30))
        # Déplacer la caméra
        camera.scroll()
        tile_rects = []
        y = 0
        for row in game_map:
            x = 0
            for tile in row:
                if tile == '1':
                    display.blit(dirt_image, (x * TILE_SIZE - camera.offset.x, y * TILE_SIZE - camera.offset.y))
                if tile == '2':
                    display.blit(grass_image, (x * TILE_SIZE - camera.offset.x, y * TILE_SIZE - camera.offset.y))
                if tile != '0':
                    tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                if tile == '3':
                    display.blit(pique_image, (x * TILE_SIZE - camera.offset.x, y * TILE_SIZE - camera.offset.y))

                x += 1
            y += 1
        x_ = int(player.rect.x) // 16
        y_ = int(player.rect.y) // 16
        print('Position joueur (x_, y_): ', x_, y_, player.rect.x,player.rect.y+16)
        display.blit(danger_image, (480 - camera.offset.x, 240 - camera.offset.y))
        display.blit(mat_image, (480 - camera.offset.x, 256 - camera.offset.y))
        display.blit(mat_image, (528 - camera.offset.x, 256 - camera.offset.y))
        display.blit(bas_image, (528 - camera.offset.x, 240 - camera.offset.y))
        display.blit(tp_image, (44 - camera.offset.x, 450 - camera.offset.y))
        display.blit(danger_image, (960 - camera.offset.x, 337 - camera.offset.y))
        display.blit(mat_image, (960 - camera.offset.x, 353 - camera.offset.y))
        display.blit(danger_image, (1328 - camera.offset.x, 245 - camera.offset.y))
        display.blit(ville, (2102 - camera.offset.x, 416 - camera.offset.y))
        display.blit(maison, (2242 - camera.offset.x, 295 - camera.offset.y))
        display.blit(apart, (2418 - camera.offset.x, 136 - camera.offset.y))
        display.blit(apart, (2570 - camera.offset.x, 136 - camera.offset.y))
        display.blit(interdit, (2016 - camera.offset.x, 49 - camera.offset.y))
        display.blit(mat_image, (2016 - camera.offset.x, 65 - camera.offset.y))
        display.blit(bas_image, (1792 - camera.offset.x, 225 - camera.offset.y))
        display.blit(mat_image, (1792 - camera.offset.x, 241 - camera.offset.y))
        display.blit(haut, (1862 - camera.offset.x, 449 - camera.offset.y))
        display.blit(mat_image, (1862 - camera.offset.x, 465 - camera.offset.y))
        display.blit(ville, (92 - camera.offset.x, 240 - camera.offset.y))
        display.blit(droite, (98 - camera.offset.x, 226 - camera.offset.y))
        


        if x_==147 and y_==26:
            m_alume=1
        if x_==157 and y_==26:            
            a_un_alu=1
        if x_==167 and y_==26:
            a_deux_alu=1
        if m_alume==1:
            display.blit(maison_alu, (2242 - camera.offset.x, 295 - camera.offset.y))
        if a_un_alu==1:
            display.blit(apart_alu, (2418 - camera.offset.x, 136 - camera.offset.y))
        if a_deux_alu==1:
            display.blit(apart_alu, (2570 - camera.offset.x, 136 - camera.offset.y))

        # Vérifier que l'indice est dans les limites
        keys = pygame.key.get_pressed()
        player.update(keys, tile_rects)

        # Limites de la carte
        player.rect.clamp_ip(pygame.Rect(0, 0, len(game_map[0]) * TILE_SIZE, len(game_map) * TILE_SIZE))

        # Événements
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    player.jump()
            
            if event.type == KEYDOWN and event.key == K_t:
                tire.tirer(player)


        
        # Gestion des cadeaux
        for cadeau in cadeaux[:]:
            cadeau.draw(display, camera)
            if cadeau.check_collision(player):
                print("Collision avec cadeau!")
                nombre_cadeaux += 1
                cadeaux.remove(cadeau)

        # Gestion des canons
        for canon in canons[:]:  # Utiliser une copie de la liste pour éviter les problèmes lors de la suppression
            if random.random() < 0.02:
                canon.tirer()
            # Vérifier la collision entre le joueur et le canon
            if canon.check_collision(player):
                print("Collision avec le canon !")
                canons.remove(canon)
                vies -= 1
            # Mise à jour et dessin des projectiles
            for projectile in canon.projectiles[:]:  # Utiliser une copie de la liste pour permettre la suppression
                projectile.update()
                if projectile.check_collision(player):
                    print("Le joueur a été touché par un projectile !")
                    vies -= 1
                    canon.projectiles.remove(projectile)  # Supprimer le projectile après la collision
                else:
                    projectile.draw(display, camera)
            # Mise à jour et dessin du canon
            canon.update()
            canon.draw(display, camera)
        tire.update(camera, canons)
        tire.draw(display, camera)
        player.draw(display, camera)

        # Mise à jour de l'écran
        surf = pygame.transform.scale(display, WINDOW_SIZE)
        screen.blit(surf, (0, 0))

        # Afficher le texte des cadeaux collectés
        nb_cadeaux = font.render(f'Cadeaux collectés: {nombre_cadeaux} sur 8', True, (0, 0, 0))
        screen.blit(nb_cadeaux, (10, 10))
        
        coeur_reduit = pygame.transform.scale(coeur, (50, 50))
        screen.blit(coeur_reduit, (1220, 2))
        nb_coeur = font.render(f'x{vies}', True, (0, 0, 0))
        piques = [(1, 19), (2, 19),(30, 27),(31, 27),(32, 27),(33, 27),(34, 27),(35, 27),(36, 27),(37, 27),(38, 27), 
                  (39, 27), (61, 27), (62, 27),(64, 27), (65, 27), (66, 27), (71, 27), (72, 27), (73, 27),(74, 27),
                  (84, 14), (85, 14), (94, 14), (95, 14), (96, 14),(113, 26), (121, 27), (122, 28), (123, 27), (124, 27),
                  (126, 27), (127, 27), (128, 27), (91, 27), (92, 27),(126, 20), (127, 20), (128, 20),(67,27)]
        
        # Vérifiez les coordonnées
        if (x_, y_) in piques:
            vies = 0

        screen.blit(nb_coeur, (1232, 2))
        if x_ == 2 and y_ == 28:  # Position de téléportation de départ
            print('Téléportation en cours...')
            x_ = 5  # Nouvelle position X en cases
            y_ = 10  # Nouvelle position Y en cases
            player.rect.x = x_ * TILE_SIZE
            player.rect.y = y_ * TILE_SIZE
            print('tp en cour')

        if a_deux_alu == 1:
            if nb_cadeaux==8:
                distribue = font.render('Tous les cadeaux sont livrés', True, (255, 255, 255))
                screen.blit(distribue, (40, 10))
            else:
                distribue_pas = font.render('Tous les cadeaux ne sont pas livrés', True, (255, 255, 255))
                screen.blit(distribue_pas, (40, 10))

        # Mise à jour de l'affichage
        pygame.display.flip()
        display.fill((146, 244, 255))

        pygame.display.update()
        clock.tick(60)

    if vies == 0:
        en_cour = False
        time.sleep(0.5)
        perdu = True



# Définir les régions cliquables pour "Rejouer" et "Quitter"
START_REGION = pygame.Rect(517, 125, 759 - 517, 179 - 125)
LEAVE_REGION = pygame.Rect(1116, 675, 1280 - 1116, 720 - 675)

while perdu:
    for event in pygame.event.get():
        # Si l'utilisateur ferme la fenêtre
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Afficher l'image de fin de jeu
    screen.blit(lose, (0, 0))

    # Obtenir la position de la souris
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Vérifier si la souris est dans la région de démarrage
    if START_REGION.collidepoint(mouse_x, mouse_y):
        if pygame.mouse.get_pressed()[0]:
            subprocess.run(["python", "v20.py"])
            pygame.quit()
            sys.exit()
    # Vérifier si la souris est dans la région de quitter
    if LEAVE_REGION.collidepoint(mouse_x, mouse_y):
        if pygame.mouse.get_pressed()[0]:  # Si l'utilisateur clique
            pygame.quit()
            sys.exit()

    pygame.display.update()  # Mettre à jour l'affichage

    # Limiter la vitesse de la boucle
    clock.tick(60)