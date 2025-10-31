import pygame, sys
from pygame.locals import *
from abc import ABC, abstractmethod
import random
import math
import time
import subprocess
pygame.init()
pygame.display.set_caption('Revenge of the Snowmen')

clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 32, bold=True, italic=True)

WINDOW_SIZE = (1280, 720)
#WIDTH=1280
#HEIGHT=720
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
display = pygame.Surface((300, 200))
# Charger l'image de sprite sheet
bg = pygame.image.load("images/fond/bg.png")
x_bg=0
bg_WIDTH=1280
sprite_sheet = pygame.image.load('images/personnages/player_animer.png')
snowman_sheet = pygame.image.load('images/personnages/snowmanfonte.png') #image d'animation demort des snowman
#importation de toutes les images pour le fond de mort
losse1=pygame.image.load("images/fond/loose1.png").convert_alpha()
losse2=pygame.image.load("images/fond/loose2.png").convert_alpha()
losse3=pygame.image.load("images/fond/loose3.png").convert_alpha()
losse4=pygame.image.load("images/fond/loose4.png").convert_alpha()
losse5=pygame.image.load("images/fond/loose5.png").convert_alpha()
losse6=pygame.image.load("images/fond/loose6.png").convert_alpha()
losse7=pygame.image.load("images/fond/loose7.png").convert_alpha()
losse8=pygame.image.load("images/fond/loose8.png").convert_alpha()
start1=pygame.image.load("images/fond/Start1.png").convert_alpha()
start2=pygame.image.load("images/fond/Start2.png").convert_alpha()
start3=pygame.image.load("images/fond/Start3.png").convert_alpha()
start4=pygame.image.load("images/fond/Start4.png").convert_alpha()
win1=pygame.image.load("images/fond/win1.png").convert_alpha()
win2=pygame.image.load("images/fond/win2.png").convert_alpha()
win3=pygame.image.load("images/fond/win3.png").convert_alpha()
win4=pygame.image.load("images/fond/win4.png").convert_alpha()

next1=pygame.image.load("images/fond/next1.png").convert_alpha()
next2=pygame.image.load("images/fond/next2.png").convert_alpha()
next3=pygame.image.load("images/fond/next3.png").convert_alpha()
next4=pygame.image.load("images/fond/next4.png").convert_alpha()

danger_image = pygame.image.load('images/panneaux/danger.png').convert_alpha()
mat_image = pygame.image.load('images/panneaux/mat.png').convert_alpha()
bas_image = pygame.image.load('images/panneaux/bas.png').convert_alpha()
tp_image = pygame.image.load('images/panneaux/tp_p.png').convert_alpha()
tp = pygame.image.load('images/autres/tp.png').convert_alpha()
apart = pygame.image.load('images/habitations/appartement.png').convert_alpha()
apart_alu = pygame.image.load('images/habitations/appartementalu.png').convert_alpha()
ville = pygame.image.load('images/panneaux/tatooine.png').convert_alpha()
mur = pygame.image.load('images/habitations/mur.png').convert_alpha()
feu_r = pygame.image.load('images/panneaux/feu_r.png').convert_alpha()
feu_o = pygame.image.load('images/panneaux/feu_o.png').convert_alpha()
feu_v = pygame.image.load('images/panneaux/feu_v.png').convert_alpha()
feu_e = pygame.image.load('images/panneaux/feu_e.png').convert_alpha()
yoda = pygame.image.load('images/personnages/yoda2.png').convert_alpha()
# Découper les frames de 16x24 à partir de la sprite sheet
frame_width = 16
frame_height = 23
# Découper les frames de 32x46 à partir de la snowman sheet
frame_width_snowman = 32
frame_height_snowman = 46


player_images = []
snowman_images = []

m_alume=0
a_un_alu=0
a_deux_alu=0
for i in range(10):
    frame = sprite_sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
    player_images.append(frame)

for i in range(4):
    #####print(i)
    frame = snowman_sheet.subsurface(pygame.Rect(i * frame_width_snowman, 0, frame_width_snowman, frame_height_snowman))
    snowman_images.append(frame)
#player_image.set_colorkey((255, 255, 255))

#display.blit(bg, (0,0))
#screen.blit(bg, (0, 0))
grass_image = pygame.image.load('images/autres/grass_snow.png')
grass_image_all = pygame.image.load('images/autres/grass_snowall.png')
grass_image_2 = pygame.image.load('images/autres/grass_snow2.png')
grass_image_hd = pygame.image.load('images/autres/grass_snowhd.png')
grass_image_bd = pygame.image.load('images/autres/grass_snowbd.png')
grass_image_d = pygame.image.load('images/autres/grass_snowmd.png')
grass_image_g = pygame.image.load('images/autres/grass_snowmg.png')
grass_image_dg = pygame.image.load('images/autres/grass_snowdg.png')
grass_image_bg = pygame.image.load('images/autres/grass_snowbg.png')
grass_image_hg=pygame.image.load('images/autres/grass_snowhg.png')
grass_image_gdh=pygame.image.load('images/autres/grass_snowgdh.png')
grass_image_bdh=pygame.image.load('images/autres/grass_snowbdh.png')
grass_image_bgh=pygame.image.load('images/autres/grass_snowbgh.png')
piquesb=pygame.image.load('images/autres/piquesb.png')
boss=pygame.image.load("images/personnages/boss2.png").convert_alpha()
TILE_SIZE = grass_image.get_width()
dirt_image = pygame.image.load('images/autres/dirt3.png')
cadeau_image = pygame.image.load("images/autres/gift_type1.png").convert_alpha()
cadeau_open = pygame.image.load("images/autres/gift_type2.png").convert_alpha()
pique_image=pygame.image.load("images/autres/piques.png").convert_alpha()
coeur=pygame.image.load("images/autres/coeur.png").convert_alpha()
maison=pygame.image.load("images/habitations/maison.png").convert_alpha()
maison_alu=pygame.image.load("images/habitations/maisonalu.png").convert_alpha()
interdit=pygame.image.load("images/panneaux/interdit.png").convert_alpha()
haut=pygame.image.load("images/panneaux/haut.png").convert_alpha()
droite=pygame.image.load("images/panneaux/droite.png").convert_alpha()
cadeau_paneau=pygame.image.load("images/panneaux/panneau_c.png").convert_alpha()
go_paneau=pygame.image.load("images/panneaux/panneau_go.png").convert_alpha()
snowvador_=pygame.image.load("images/autres/attention).png").convert_alpha()
snowvador = pygame.transform.smoothscale(snowvador_, (165,16))
music_files = ["sons/musique1.mp3", "sons/boss.mp3", "sons/door.mp3", "sons/ialwayscomeback.mp3"]
current_song_index = 0
pygame.mixer.music.load(music_files[current_song_index])
pygame.mixer.music.play(-1)
pygame.mixer.init
nombre_cadeaux=0
vies=3
WHITE = (255, 255, 255)
#BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
game_map = [
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0tt','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','3','3','3','3','3','3','3','3','3','3','3','3','3','3','3','3','3','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','4','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','0','0','0','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','6','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','3','3','3','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2',],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1',],
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

class Snowman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 6
        self.projectiles = []
        # Charger l'image du bonhomme de neige et définir le rectangle de collision
        self.images=snowman_images
        self.image=self.images[0]
        self.rect = pygame.Rect(x - self.image.get_width() / 2, y - self.image.get_height() / 2, self.image.get_width(), self.image.get_height())
        self.animation_frame = 0  # Variable pour suivre l'index de l'image d'animation
        self.frame_time = 0  # Variable pour contrôler la durée de chaque frame
        self.reduire=False


    def tirer(self,direction_tire):
        # Tirer avec un angle entre 45° et 60° pour avoir une trajectoire en cloche vers la gauche
        angle = random.uniform(15, 30)  # Angle entre 45° et 60° (vers la gauche)
        radian_angle = math.radians(angle)
        self.speed= random.randint(1,4)
        #velocity_x = -self.speed * math.cos(radian_angle)  # Vitesse horizontale vers la gauche
        #velocity_y = (-self.speed/3)  * math.sin(radian_angle)  # Vitesse verticale vers le haut
        velocity_x= random.randint(-6,-4)* math.cos(radian_angle)
        velocity_y= random.randint(-4,-2)* math.sin(radian_angle)
        ####print('x',velocity_x,'y',velocity_y)
        projectile = Projectile(self.x, self.y, direction_tire * velocity_x, velocity_y)

        self.projectiles.append(projectile)

    def update(self):
        for projectile in self.projectiles:
            projectile.update()
        # Mettre à jour la position du rectangle
        self.rect.x = self.x - self.image.get_width() / 2
        self.rect.y = self.y - self.image.get_height() / 2

    def draw(self, display, camera):
        if self.reduire==True:
            if self.frame_time % 10 == 0:  # Contrôle du temps entre les frames
                self.animation_frame += 1
                if self.animation_frame >= len(self.images)-1:  # Si on atteint la fin des frames
                    self.reduire=False
                    snowmen.remove(snowman)
            self.frame_time += 1  # Incrémenter le temps entre les frames
        self.image = self.images[self.animation_frame]
        # Calculer les coordonnées ajustées en fonction de la caméra
        adjusted_x = self.x - camera.offset.x
        adjusted_y = self.y - camera.offset.y
        
        # Dessiner le bonhomme de neige à la position ajustée
        display.blit(self.image, (adjusted_x - self.image.get_width() / 2, adjusted_y - self.image.get_height() / 2))
        
        # Dessiner les projectiles
        for projectile in self.projectiles:
            projectile.draw(display, camera)

    def check_collision(self, player):
        """Vérifie si le snowman entre en collision avec le joueur."""
        return self.rect.colliderect(player.rect)
    def toucher(self):
        self.reduire=True

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
        pygame.draw.circle(screen, BLUE, (int(adjusted_x), int(adjusted_y)), 4)

    def check_collision(self, player):
        """Vérifie si le projectile entre en collision avec le joueur."""
        return self.rect.colliderect(player.rect)
    
    def check_collision_2(self,tiles):
        """Vérifie si le projectile entre en collision avec la map."""
        return self.rect.colliderect(tiles)

class Tire:
    def __init__(self):
        self.projectiles = []  # Liste pour stocker les projectiles  
        self.vie_boss=4
    def tirer(self, joueur,direction_):
        """Crée un projectile aux coordonnées du joueur."""
        self.projectiles.append({'x': joueur.rect.centerx, 'y': joueur.rect.centery, 'vx': 6*direction_, 'vy': 0})

    def update(self, camera, snowmen,boss_):
        """Met à jour les projectiles et gère leurs collisions."""
        ######print(self.vie_boss)
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
            elif len(boss_)==0:
                self.projectiles.remove(projectile)
            else:
                # Vérifie la collision avec les snowmen
                for snowman in snowmen[:]:  # Copie pour éviter la modification simultanée
                    if snowman.rect.collidepoint(projectile['x'], projectile['y']):
                        snowman.toucher()
                        #snowmen.remove(snowman)  # Supprime le snowman
                        self.projectiles.remove(projectile)  # Supprime le projectile
                # Vérifie la collision avec le boss
                if boss.rect.collidepoint(projectile['x'], projectile['y']):
                    if boss.health > 0:
                        boss.health -= 1  # Réduire la santé du boss
                    if boss.health <= 0:
                         boss_.remove(boss)  # Supprime le boss si sa santé est à zéro
                         pygame.mixer.music.pause()
                         son = pygame.mixer.Sound("sons/ialwayscomeback.mp3")
                         son.set_volume(1.0)
                         son.play()
                    self.projectiles.remove(projectile)  # Supprime le projectile




    def draw(self, display, camera):
            """Dessine les projectiles sur l'écran."""
            for projectile in self.projectiles:
                adjusted_x = projectile['x'] - camera.offset.x
                adjusted_y = projectile['y'] - camera.offset.y
                pygame.draw.circle(display, (255, 255, 0), (int(adjusted_x), int(adjusted_y)), 5)

class Boss:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 6
        self.projectiles = []
        self.img = pygame.image.load("images/personnages/boss3.png").convert_alpha()
        self.rect = pygame.Rect(x - self.img.get_width() / 2, y - self.img.get_height() / 2, self.img.get_width(), self.img.get_height())
        self.dp = 0
        self.health = 4  # Vie du boss (exemple)
        self.max_health = 4
        self.compteur=0

    def draw_health_bar(self, display, camera):
        """Affiche la barre de vie du boss."""
        if self.compteur<300:
            self.compteur+=1
        if self.compteur>=300:
            bar_width = 50  # Largeur totale de la barre
            bar_height = 5  # Hauteur de la barre
            adjusted_x = self.rect.centerx - bar_width // 2 - camera.offset.x
            adjusted_y = self.rect.top - 10 - camera.offset.y

            # Dessiner le fond rouge de la barre (vie totale)
            pygame.draw.rect(display, (255, 0, 0), (adjusted_x, adjusted_y, bar_width, bar_height))

            # Dessiner la partie verte (vie restante)
            health_percentage = self.health / self.max_health
            pygame.draw.rect(display, (0, 255, 0), (adjusted_x, adjusted_y, bar_width * health_percentage, bar_height))


    def tirer(self):
        # Tirer avec un angle entre 45° et 60° pour avoir une trajectoire en cloche vers la gauche
        angle = random.uniform(45, 60)  # Angle entre 45° et 60° (vers la gauche)
        radian_angle = math.radians(angle)
        velocity_x = -self.speed * math.cos(radian_angle)  # Vitesse horizontale vers la gauche
        velocity_y = -self.speed * math.sin(radian_angle)  # Vitesse verticale vers le haut
        projectile = Projectile(self.x, self.y, velocity_x, velocity_y)
        self.projectiles.append(projectile)

    def update(self,x_,Level):
        for projectile in self.projectiles:
            projectile.update()
        # Mettre à jour la position du rectangle
        self.rect.x = self.x - self.img.get_width() / 2
        self.rect.y = self.y - self.img.get_height() / 2
        if self.x<478:
            self.x+=2.5

        elif x_>=129 or self.dp==1 and Level==2:
            self.x-=1
            ######print(self.x)
            #####print('JE PASSE LA')
            self.dp=1
        else:
            #####print('Je passe LAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
            self.x=2702
            self.y=425
        ######print('JE PASSE PAR ICI')


    def draw(self, display, camera):
        # Calculer les coordonnées ajustées en fonction de la caméra
        adjusted_x = self.x - camera.offset.x
        adjusted_y = self.y - camera.offset.y
        
        # Dessiner le bonhomme de neige à la position ajustée
        display.blit(self.img, (adjusted_x - self.img.get_width() / 2, adjusted_y - self.img.get_height() / 2))
        # Dessiner les projectiles
        for projectile in self.projectiles:
            projectile.draw(display, camera)
        ######print('JE PASSE PAR ICI')
    def check_collision(self, player):
        """Vérifie si le boss entre en collision avec le joueur."""
        return self.rect.colliderect(player.rect)
def level0():

    global player, camera, balls, tire, direction_, cadeaux, snowmen, boss_, vies, perdu, fonte, tp_, frame_time,nombre_cadeaux,wall_active,y_mur,Win,compteur_time,sonplay,musique_play,Level,m_alume,a_un_alu,a_deux_alu,game_map,piques,x_yoda
    player = Personnage(50, 50, player_images)
    camera = Camera(player)
    camera.setmethod(Follow(camera, player))
    balls = []
    tire = Tire()
    direction_ = 1
    # Définir les cadeaux en dehors de la boucle principale
    cadeaux = [Cadeau(206, 240, cadeau_image),Cadeau(2150, 128, cadeau_image)]
    # Liste pour stocker plusieurs snowmen
    snowmen = [Snowman(528, 282),Snowman(2450, 125)]
    boss_=[Boss(0, 2500)]
    vies = 3
    perdu = False
    fonte = False
    tp_ = False
    frame_time = 0
    nombre_cadeaux=0
    wall_active=True
    y_mur=226
    Win=False
    compteur_time=0
    sonplay=False
    musique_play=False
    m_alume=0
    a_un_alu=0
    a_deux_alu=0
    ####print('je reset')
    Level=0
    piques=[(44, 18), (45, 18), (114,7), (115,7),(116,7),(117,7),(118,7),(119,7),(120,7),(121,7),(122,7),(123,7)]
    x_yoda=500
def level1():
    global player, camera, balls, tire, direction_, cadeaux, snowmen, boss_, vies, perdu, fonte, tp_, frame_time,nombre_cadeaux,wall_active,y_mur,Win,compteur_time,sonplay,musique_play,Level,m_alume,a_un_alu,a_deux_alu,game_map,piques,next
    game_map = [
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0tt','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','4','0','4','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','4','0','0','0','0','0','0','b','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','6','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','4','0','4','0','0','0','4','0','0','4','0','0','4','0','4','0','2','2','2','2','2',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','4','0','4','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','4','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','4','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','6','0','4','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','4','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','4','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','b','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','6','0','0','4','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','4','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','4','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','3','3','3','3','3','3','3','3','3','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','3','3','3','3','3','3','3','3','3','3','3','3','3','3','3','3','3','3','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    ]
    player = Personnage(50, 50, player_images)
    camera = Camera(player)
    camera.setmethod(Follow(camera, player))
    balls = []
    tire = Tire()
    direction_ = 1
    # Définir les cadeaux en dehors de la boucle principale
    cadeaux = [Cadeau(384, 305, cadeau_image),Cadeau(1056, 128, cadeau_image),Cadeau(544, 272, cadeau_image),Cadeau(784, 272, cadeau_image)]
    # Liste pour stocker plusieurs snowmen
    snowmen = [Snowman(304, 218),Snowman(1150, 122+16)]
    boss_=[Boss(0, 100000)]
    vies = 3
    perdu = False
    fonte = False
    tp_ = False
    frame_time = 0
    nombre_cadeaux=0
    wall_active=True
    y_mur=226
    Win=False
    compteur_time=0
    sonplay=False
    musique_play=False
    Level=1
    m_alume=0
    a_un_alu=0
    a_deux_alu=0
    next=False
    ####print('je reset')
    piques = []
def level2():
    global player, camera, balls, tire, direction_, cadeaux, snowmen, boss_, vies, perdu, fonte, tp_, frame_time,nombre_cadeaux,wall_active,y_mur,Win,compteur_time,sonplay,musique_play,Level,m_alume,a_un_alu,a_deux_alu,game_map,piques,next,musique_mur,musique_mur_,play_mort
    game_map = [
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0tt','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','8','0','0','0','0','c','0','0','0','0','0','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','8','0','0','0','0','a','0','0','0','0','0','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','8','0','0','0','f','8','0','0','0','0','0','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','8','0','0','0','0','a','0','0','0','0','b','2','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','b','6','0','0','9','1','1','1','5','5','1','e','0','0','0','a','0','0','0','0','a','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','b','1','7','0','0','9','1','1','8','0','0','a','0','0','0','0','a','0','0','0','0','a','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','b','1','7','0','0','0','9','1','1','8','0','0','a','0','0','0','0','a','0','0','0','0','a','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','4','4','4','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','b','1','7','0','0','0','0','9','1','1','8','0','0','a','0','0','0','f','8','0','0','0','0','a','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','c','0','0','0','0','0','0','0','0','0','0','b','1','7','0','0','0','0','b','1','1','1','8','0','0','a','0','0','0','0','a','0','0','0','0','a','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','b','8','0','0','0','0','0','0','0','0','0','b','1','7','0','0','0','0','b','1','1','1','1','8','0','0','9','e','0','0','0','a','0','0','0','0','a','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','f','e','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','8','0','0','0','0','0','0','0','0','b','1','7','0','0','0','0','b','1','1','1','5','5','7','0','0','a','0','0','0','0','a','0','0','0','0','a','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['4','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','b','2','1','8','0','0','0','0','0','0','0','b','1','7','0','0','0','0','b','1','1','1','8','0','0','0','0','0','a','0','0','0','0','a','0','0','0','0','a','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','4','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','b','1','1','1','8','0','0','0','0','0','0','b','5','7','0','0','0','0','b','1','1','1','1','8','0','0','0','0','0','a','0','0','0','f','8','0','0','0','0','a','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','8','0','0','2','0','0','0','a','0','0','0','0','b','2','1','1','1','1','1','8','0','0','0','0','0','9','e','0','0','0','a','0','0','0','0','a','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','4','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','b','3','3','1','1','1','1','8','0','0','9','3','3','3','7','0','0','0','b','1','1','1','1','1','1','1','8','0','0','c','0','0','a','0','0','0','0','a','0','0','0','0','a','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['6','0','0','b','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','6','0','0','4','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','b','1','1','1','1','1','1','1','8','0','0','9','5','5','7','0','0','0','b','1','1','1','1','1','1','1','1','8','0','f','8','0','0','a','0','4','0','0','a','0','0','0','0','a','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['8','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','b','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','6','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','b','1','1','1','1','1','1','1','1','8','0','0','a','0','0','0','0','0','b','1','1','1','1','1','1','1','1','1','8','0','0','a','0','0','a','0','0','0','0','a','0','0','0','0','a','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['8','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','6','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','b','1','1','1','1','1','1','1','1','1','8','0','0','a','0','0','0','0','0','d','5','1','1','1','1','1','1','1','1','8','0','0','a','0','0','a','0','0','0','f','8','0','0','0','0','a','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['8','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','b','1','1','1','1','1','1','1','1','1','1','8','0','0','9','6','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','e','0','a','0','0','a','0','0','0','0','a','0','0','0','0','a','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['1','3','3','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','b','1','1','1','1','1','1','1','1','1','1','1','8','0','0','9','1','6','0','0','0','0','0','d','1','1','1','1','1','1','1','8','0','0','a','0','0','a','0','0','0','0','a','0','0','0','0','a','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','2','6','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','b','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','9','1','1','6','0','0','0','0','0','d','1','1','1','1','1','1','8','0','0','a','0','0','a','0','4','0','0','a','0','0','0','0','d','g','g','g','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','6','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','b','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','9','1','1','1','6','0','0','0','0','0','d','1','1','1','1','1','8','0','f','8','0','0','a','0','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','7','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','b','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','9','1','1','1','1','6','0','0','0','0','0','d','5','5','5','5','7','0','0','a','0','0','a','0','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','4','4','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','9','1','1','1','1','1','6','0','0','0','0','0','0','0','0','0','0','0','0','a','0','0','a','0','0','0','f','8','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','4','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','c','0','0','0','b','2','2','2','6','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','9','1','1','1','1','1','1','6','0','0','0','0','0','0','0','0','0','4','0','a','0','0','a','0','0','0','0','a','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','a','0','0','0','9','1','1','1','8','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','9','1','1','1','1','1','1','1','6','0','0','0','0','0','0','0','0','0','0','a','0','0','d','e','0','0','0','a','0','0','0','4','6','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','a','0','0','0','9','1','1','1','8','0','0','0','9','1','1','1','1','1','1','1','1','1','1','1','1','1','1','8','0','0','9','1','1','1','1','1','1','1','1','6','0','0','0','0','0','0','0','0','0','a','0','0','0','0','0','0','0','a','0','0','0','9','a','0','0','0','b','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','3','3','3','3','3','3','3','3','3','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','3','3','1','3','3','3','1','1','1','8','1','3','3','3','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','3','3','9','1','1','1','1','1','1','1','1','1','6','0','0','0','0','0','0','0','b','1','3','0','0','0','0','0','b','1','3','3','3','1','1','3','3','3','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','2','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1',],
        ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','2','2','2','2','2','2','2','1','1','1','2','2','2','2','2','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1',],
    ]
    player = Personnage(50, 50, player_images)
    camera = Camera(player)
    camera.setmethod(Follow(camera, player))
    balls = []
    tire = Tire()
    direction_ = 1
    # Définir les cadeaux en dehors de la boucle principale
    cadeaux = [Cadeau(50, 255, cadeau_image), Cadeau(340, 255, cadeau_image),Cadeau(0, 191, cadeau_image), Cadeau(190, 127, cadeau_image),Cadeau(592, 239, cadeau_image),Cadeau(208, 463, cadeau_image),Cadeau(1120, 400, cadeau_image),Cadeau(1010, 400, cadeau_image)]
    # Liste pour stocker plusieurs snowmen
    snowmen = [Snowman(700, 267),Snowman(200, 250), Snowman(1500, 219),Snowman(1100, 394)]
    boss_=[Boss(0, 250)]
    vies = 3
    perdu = False
    fonte = False
    tp_ = False
    frame_time = 0
    nombre_cadeaux=0
    wall_active=True
    y_mur=226
    Win=False
    compteur_time=0
    sonplay=False
    musique_play=False
    Level=2
    m_alume=0
    a_un_alu=0
    a_deux_alu=0
    next=False
    musique_mur=True
    musique_mur_=True
    play_mort=True
    ####print('je reset')
    piques = [(1, 19), (2, 19),(30, 27),(31, 27),(32, 27),(33, 27),(34, 27),(35, 27),(36, 27),(37, 27),(38, 27), 
                    (39, 27), (61, 27), (62, 27),(64, 27), (65, 27), (66, 27), (71, 27), (72, 27), (73, 27),(74, 27),
                    (84, 14), (85, 14), (94, 14), (95, 14), (96, 14),(113, 26), (121, 27), (122, 28), (123, 27), (124, 27),
                    (126, 27), (127, 27), (128, 27), (91, 27), (92, 27),(126, 20), (127, 20), (128, 20),(67,27)]
y_mur=226
player = Personnage(50, 50, player_images)
camera = Camera(player)
camera.setmethod(Follow(camera, player))
balls = []
tire = Tire()
direction_=1
# Définir les cadeaux en dehors de la boucle principale
cadeaux = [Cadeau(206, 240, cadeau_image),Cadeau(2150, 128, cadeau_image)]
# Liste pour stocker plusieurs snowmen
snowmen = [Snowman(528, 282),Snowman(2450, 125)]
boss_=[Boss(0, 2500)]
run=True
perdu=False
fonte=False
tp_=False
frame_time=0
# Variable pour alterner les images
start_screen = True  # Utilisée pour image sart game
wall_active=True
Win=False
next=False
compteur_time=0
sonplay=False
musique_play=False
Level=0
piques=[(44, 18), (45, 18), (114,7), (115,7),(116,7),(117,7),(118,7),(119,7),(120,7),(121,7),(122,7),(123,7)]
x_yoda=500
musique_mur=True
musique_mur_=True
play_mort=True
while run == True:
    clock.tick(60)
        
    if vies > 0 and start_screen==False and Win==False and next==False:
        
        display.blit(bg, (x_bg,0- camera.offset.y))
        if x_bg==-1*bg_WIDTH:
            x_bg=0
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
                if tile == '4':
                    display.blit(grass_image_all, (x * TILE_SIZE - camera.offset.x, y * TILE_SIZE - camera.offset.y))
                if tile == '5':
                    display.blit(grass_image_2, (x * TILE_SIZE - camera.offset.x, y * TILE_SIZE - camera.offset.y))
                if tile == '6':
                    display.blit(grass_image_hd, (x * TILE_SIZE - camera.offset.x, y * TILE_SIZE - camera.offset.y))
                if tile == '7':
                    display.blit(grass_image_bd, (x * TILE_SIZE - camera.offset.x, y * TILE_SIZE - camera.offset.y))
                if tile == '8':
                    display.blit(grass_image_d, (x * TILE_SIZE - camera.offset.x, y * TILE_SIZE - camera.offset.y))
                if tile == '9':
                    display.blit(grass_image_g, (x * TILE_SIZE - camera.offset.x, y * TILE_SIZE - camera.offset.y))
                if tile == 'a':
                    display.blit(grass_image_dg, (x * TILE_SIZE - camera.offset.x, y * TILE_SIZE - camera.offset.y))
                if tile == 'b':
                    display.blit(grass_image_hg, (x * TILE_SIZE - camera.offset.x, y * TILE_SIZE - camera.offset.y))
                if tile == 'c':
                    display.blit(grass_image_gdh, (x * TILE_SIZE - camera.offset.x, y * TILE_SIZE - camera.offset.y))
                if tile == 'd':
                    display.blit(grass_image_bg, (x * TILE_SIZE - camera.offset.x, y * TILE_SIZE - camera.offset.y))
                if tile == 'e':
                    display.blit(grass_image_bdh, (x * TILE_SIZE - camera.offset.x, y * TILE_SIZE - camera.offset.y))
                if tile == 'f':
                    display.blit(grass_image_bgh, (x * TILE_SIZE - camera.offset.x, y * TILE_SIZE - camera.offset.y))
                if tile == 'g':
                    display.blit(piquesb, (x * TILE_SIZE - camera.offset.x, y * TILE_SIZE - camera.offset.y))    
                if tile != '0':
                    tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                if tile == '3':
                    display.blit(pique_image, (x * TILE_SIZE - camera.offset.x, y * TILE_SIZE - camera.offset.y))
                x += 1
            y += 1                   
        x_ = int(player.rect.x) // 16
        y_ = int(player.rect.y) // 16
        ##print('Position joueur (x_, y_): ', x_, y_, player.rect.x,player.rect.y)
        x_bg=-x_
        ######print(x_bg)
        #print(x_,y_)
        if Level==0:
            display.blit(tp, (1120 - camera.offset.x, 271 - camera.offset.y))
            display.blit(tp, (2646 - camera.offset.x, 110 - camera.offset.y))
            display.blit(mat_image, (2000 - camera.offset.x, 129 - camera.offset.y))
            display.blit(danger_image, (2000 - camera.offset.x, 113 - camera.offset.y))
            display.blit(mat_image, (2300 - camera.offset.x, 129 - camera.offset.y))
            if frame_time < 10:
                display.blit(droite, (2300 - camera.offset.x, 113 - camera.offset.y))
            elif frame_time > 10 and frame_time < 20 :
                display.blit(bas_image, (2300 - camera.offset.x, 113 - camera.offset.y))
            elif frame_time > 20 and frame_time < 30:
                display.blit(danger_image, (2300 - camera.offset.x, 113 - camera.offset.y))
            elif frame_time > 30:
                display.blit(haut, (2300 - camera.offset.x, 113 - camera.offset.y))
                frame_time = 0
            frame_time += 1
        if Level==1:
            display.blit(tp, (1440 - camera.offset.x, 129 - camera.offset.y))
        if Level==2:
            display.blit(danger_image, (480 - camera.offset.x, 240 - camera.offset.y))
            display.blit(mat_image, (480 - camera.offset.x, 256 - camera.offset.y))
            display.blit(mat_image, (528 - camera.offset.x, 256 - camera.offset.y))
            if tp_==False:
                display.blit(bas_image, (528 - camera.offset.x, 240 - camera.offset.y))
            elif tp_==True:
                display.blit(droite, (528 - camera.offset.x, 240 - camera.offset.y))
            display.blit(tp_image, (100 - camera.offset.x, 450 - camera.offset.y))
            display.blit(tp, (44 - camera.offset.x, 450 - camera.offset.y))
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




            #gestion du mur qui bloque le passage a la suite du jeu
            if nombre_cadeaux<8:
                display.blit(mur, (1200 - camera.offset.x, 226 - camera.offset.y))
                display.blit(cadeau_paneau, (1080 - camera.offset.x, 384 - camera.offset.y))
                display.blit(feu_r, (1080 - camera.offset.x, 366 - camera.offset.y))
            elif nombre_cadeaux==8:
                if y_mur<720:
                    #####print(y_mur)
                    y_mur+=1
                    display.blit(mur, (1200 - camera.offset.x, y_mur - camera.offset.y))
                    display.blit(feu_o, (1080 - camera.offset.x, 366 - camera.offset.y))
                    if musique_mur == True:
                        musique_mur=False
                        actuel = pygame.mixer.music.get_pos()
                        current_song_index = 2
                        pygame.mixer.music.load(music_files[current_song_index])
                        pygame.mixer.music.play(-1)
                        
                if y_mur>400:
                    wall_active=False
                    display.blit(feu_v, (1080 - camera.offset.x, 366 - camera.offset.y))
                    if musique_mur_ == True:
                        musique_mur_=False
                        current_song_index = 0
                        pygame.mixer.music.load(music_files[current_song_index])
                        print('actuel', actuel)
                        pygame.mixer.music.play(start=actuel/1000)
                display.blit(go_paneau, (1080 - camera.offset.x, 384 - camera.offset.y))
                print(actuel)

                if actuel>6480:
                    actuel = actuel - 6480

            if x_==74 and wall_active==True:
                x_ -= 5  # Nouvelle position X en cases
                y_ -= 1  # Nouvelle position Y en cases
                player.rect.x = x_ * TILE_SIZE
                player.rect.y = y_ * TILE_SIZE  
            


            if x_==147:
                m_alume=1
                nombre_cadeaux=6
            if x_==157:            
                a_un_alu=1
                nombre_cadeaux=3
            if x_==167:
                a_deux_alu=2
                
            if m_alume==1:
                display.blit(maison_alu, (2242 - camera.offset.x, 295 - camera.offset.y))
            if a_un_alu==1:
                display.blit(apart_alu, (2418 - camera.offset.x, 136 - camera.offset.y))
            if a_deux_alu==2:
                display.blit(apart_alu, (2570 - camera.offset.x, 136 - camera.offset.y))
                y_=20
                time.sleep(0.25)
                Win=True

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
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    player.jump()  # Le joueur saute
                elif event.key == K_LEFT:
                    direction_ = -1  # Gauche
                    x_yoda -= 1
                elif event.key == K_RIGHT:
                    direction_ = 1  # Droite
                    x_yoda += 1
                elif event.key == K_t:
                    tire.tirer(player, direction_)
                    son = pygame.mixer.Sound("sons/laser.mp3")
                    son.set_volume(1.0)
                    son.play()
        ####print(x_yoda)
        
        # Gestion des cadeaux
        for cadeau in cadeaux[:]:
            cadeau.draw(display, camera)
            if cadeau.check_collision(player):
                #####print("Collision avec cadeau!")
                nombre_cadeaux += 1
                son = pygame.mixer.Sound("sons/coin.mp3")
                son.set_volume(1.0)
                son.play()
                cadeaux.remove(cadeau)

        # Gestion des snowmen
        for snowman in snowmen[:]:  # Utiliser une copie de la liste pour éviter les problèmes lors de la suppression

            if player.rect.x > snowman.rect.x:
                direction_tire = -1
            elif player.rect.x <= snowman.rect.x:
                direction_tire = 1
            ####print(direction_tire)

            ####print(type(player.rect.x))
            ####print(snowman.rect.x)
            if random.randint(1,45) == 2:
                snowman.tirer(direction_tire)
            # Vérifier la collision entre le joueur et le snowman
            if snowman.check_collision(player):
                #####print("Collision avec le snowman !")
                snowman_x = snowman.x
                snowman_y = snowman.y
                snowmen.remove(snowman)
                # Réduire les vies
                vies -= 1


        
            # Mise à jour et dessin des projectiles
            for projectile in snowman.projectiles[:]:  # Utiliser une copie de la liste pour permettre la suppression
                projectile.update()
                if projectile.check_collision(player):
                    #####print("Le joueur a été touché par un projectile !")
                    if Level>0:
                        vies -= 1
                    snowman.projectiles.remove(projectile)  # Supprimer le projectile après la collision
            for tiles in tile_rects:
                for projectile in snowman.projectiles[:]:
                     if projectile.check_collision_2(tiles):
                         snowman.projectiles.remove(projectile)

            # Mise à jour et dessin du snowman
            snowman.update()
            snowman.draw(display, camera)


        
        # Gestion du boss_
        
        for boss in boss_[:]:  # Utiliser une copie de la liste pour éviter les problèmes lors de la suppression
            if random.random() < 0.02:
                boss.tirer()
            # Vérifier la collision entre le joueur et le boss
            if boss.check_collision(player):
                #####print("Collision avec le boss !")
                son = pygame.mixer.Sound("sons/ialwayscomeback.mp3")
                son.set_volume(1.0)
                son.play()
                boss_.remove(boss)
                vies = 0
            # Mise à jour et dessin des projectiles
            for projectile in boss.projectiles[:]:  # Utiliser une copie de la liste pour permettre la suppression
                projectile.update()
                if projectile.check_collision(player):
                    #####print("Le joueur a été touché par un projectile !")
                    vies -= 1
                    boss.projectiles.remove(projectile)  # Supprimer le projectile après la collision
                else:
                    projectile.draw(display, camera)
            for tiles in tile_rects:
                for projectile in boss.projectiles[:]:
                     if projectile.check_collision_2(tiles):
                         boss.projectiles.remove(projectile)
            # Mise à jour et dessin du boss
            boss.update(x_,Level)
            boss.draw(display, camera)
            boss.draw_health_bar(display, camera)
            ######print('je passe la')

        tire.update(camera, snowmen,boss_)
        tire.draw(display, camera)
        player.draw(display, camera)

        # Mise à jour de l'écran
        surf = pygame.transform.scale(display, WINDOW_SIZE)
        screen.blit(surf, (0, 0))

        # Afficher le texte des cadeaux collectés
        cadeau_reduit = pygame.transform.scale(cadeau_image, (50, 50))
        screen.blit(cadeau_reduit, (10, 10))
        nb_cadeaux = font.render(f'x{nombre_cadeaux}', True, (0, 0, 0))
        screen.blit(nb_cadeaux, (20, 24))
        
        coeur_reduit = pygame.transform.scale(coeur, (50, 50))
        screen.blit(coeur_reduit, (1220, 2))
        nb_coeur = font.render(f'x{vies}', True, (0, 0, 0))
        if Level==0:
            ap = font.render(f'Learning (Level 0)', True, (0, 0, 0))
            screen.blit(ap, (500, 20))
            yoda_ = pygame.transform.scale(yoda, (100, 100))
            screen.blit(yoda_, (1, 100))
            if x_>=0 and x_<=15:
                cadeau_p = font.render(f'Cadeaux prendre tu dois', True, (0, 0, 0))
                cadeau_p2 = font.render(f'Tous besoin tu auras', True, (0, 0, 0))
                screen.blit(cadeau_p, (100, 100))
                screen.blit(cadeau_p2, (100, 125))
            
            if x_>=23 and x_<=33 and len(snowmen)==1:
                tuto_enemie = font.render(f'Tirer sur ennemi tu dois', True, (0, 0, 0))
                tuto_enemie_ = font.render(f' Touche "T" tu dois presser', True, (0, 0, 0))
                screen.blit(tuto_enemie, (100, 100))
                screen.blit(tuto_enemie_, (100, 125))
            if x_>=42 and x_<=47:
                saut_ = font.render(f'Sauter dessus, danger tu dois.', True, (0, 0, 0))
                saut__ = font.render(f' Prudence, tu agiras.', True, (0, 0, 0))
                screen.blit(saut__, (100, 125))
                screen.blit(saut_, (100, 100))
            if x_>=64 and x_<70:
                porte = font.render(f'Téléporteur porte prendre tu dois.', True, (0, 0, 0))
                screen.blit(porte, (100, 100))
                if x_ == 69:
                    son = pygame.mixer.Sound("sons/tp.mp3")
                    son.set_volume(1.0)
                    son.play()
                    x_ = 125
                    y_=0
                    player.rect.x = x_ * TILE_SIZE
                    player.rect.y = y_ * TILE_SIZE
            if x_ > 125:
                fin_ = font.render(f' Ton entrainement est fini', True, (0, 0, 0))
                screen.blit(fin_, (100, 100))
                prud = font.render(f' Prudence tu feras.', True, (0, 0, 0))
                screen.blit(prud, (100, 125))
                pan = font.render(f' Paneaux sur ton chemin tu suiveras', True, (0, 0, 0))
                screen.blit(pan, (100, 150))
                snow = font.render(f' Snowvador battre tu dois', True, (0, 0, 0))
                screen.blit(snow, (100, 175))

                if x_>=165:
                    son = pygame.mixer.Sound("sons/tp.mp3")
                    son.set_volume(1.0)
                    son.play()
                    next=True
                    #level1()
        if Level==1:
            ap = font.render(f'Warm UP (Level 1)', True, (0, 0, 0))
            screen.blit(ap, (500, 20))
            if x_==90:
                son = pygame.mixer.Sound("sons/tp.mp3")
                son.set_volume(1.0)
                son.play()
                next=True
            if y_==28:
                vies=0
        # Vérifiez les coordonnées
        if (x_, y_) in piques:
            vies = 0
        screen.blit(nb_coeur, (1232, 2))
        if x_ == 2 and y_ == 28 and Level==2:  # Position de téléportation de départ
            #####print('Téléportation en cours...')
            x_ = 5  # Nouvelle position X en cases
            y_ = 10  # Nouvelle position Y en cases
            player.rect.x = x_ * TILE_SIZE
            player.rect.y = y_ * TILE_SIZE
            son = pygame.mixer.Sound("sons/tp.mp3")
            son.set_volume(1.0)
            son.play()
            #####print('tp en cour')
            tp_=True
        '''
        if x_ == 17:  # Position de téléportation de départ
            position_=True
            #####print('je pass la')
        '''
        if Level==2:
            ap = font.render(f" The ultimate battle (Level 2)", True, (0, 0, 0))
            screen.blit(ap, (500, 20))
            if x_ >= 125:
                if sonplay==False:
                    sonplay=True
                    actuel = pygame.mixer.music.get_pos()
                    # User clicked the "next" button, go to the next song in the list
                    current_song_index += 1
                    pygame.mixer.music.load(music_files[current_song_index])
                    pygame.mixer.music.play()
                position__=True
                if x_<=130:
                    screen.blit(snowvador_, (300, 100))
                #####print('je pass la')
        
            


        # Mise à jour de l'affichage
        pygame.display.flip()
        display.fill((146, 244, 255))

        #pygame.display.update()
        #clock.tick(120)

    elif vies<=0:
        if musique_play==False:
            musique_play=True
            current_song_index = 0
            pygame.mixer.music.load(music_files[current_song_index])
            pygame.mixer.music.play(-1)
        #####print(vies)
        START_REGION = pygame.Rect(517, 125, 759 - 517, 179 - 125)
        LEAVE_REGION = pygame.Rect(1116, 675, 1280 - 1116, 720 - 675)
        frame_time+=1
        # Logique pour afficher les images
        if frame_time == 10:  # Chaque 60 frames
            screen.blit(losse1, (0, 0))  # Affiche l'image 'lose'
        elif frame_time ==20:
            screen.blit(losse2, (0, 0))  # Affiche l'image 'lose'
        elif frame_time ==30:
            screen.blit(losse3, (0, 0))  # Affiche l'image 'lose'
        elif frame_time ==40:
            screen.blit(losse4, (0, 0))  # Affiche l'image 'lose'
        elif frame_time ==50:
            screen.blit(losse5, (0, 0))  # Affiche l'image 'lose'
        elif frame_time ==60:
            screen.blit(losse6, (0, 0))  # Affiche l'image 'lose'
        elif frame_time ==70:
            screen.blit(losse7, (0, 0))  # Affiche l'image 'lose'
        elif frame_time ==80:
            screen.blit(losse8, (0, 0))  # Affiche l'image 'lose'
            frame_time=0


        mouse_x, mouse_y = pygame.mouse.get_pos()
        if START_REGION.collidepoint(mouse_x, mouse_y):
                if pygame.mouse.get_pressed()[0]:
                    if Level==0:
                        level0()
                    elif Level==1:
                        level1()
                    else:
                        level2()
        if LEAVE_REGION.collidepoint(mouse_x, mouse_y):
                if pygame.mouse.get_pressed()[0]:  # Si l'utilisateur clique
                    pygame.quit()
                    sys.exit()
        for event in pygame.event.get():
        # Si l'utilisateur ferme la fenêtre
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    if start_screen==True:
        START_REGION = pygame.Rect(517, 125, 759 - 517, 179 - 125)
        LEAVE_REGION = pygame.Rect(1116, 675, 1280 - 1116, 720 - 675)
        frame_time+=1
        # Logique pour afficher les images
        if frame_time == 10:  # Chaque 60 frames
            screen.blit(start1, (0, 0))  # Affiche l'image 'start'
        elif frame_time ==20:
            screen.blit(start2, (0, 0))  # Affiche l'image 'start'
        elif frame_time ==30:
            screen.blit(start3, (0, 0))  # Affiche l'image 'start'
        elif frame_time ==40:
            screen.blit(start4, (0, 0))  # Affiche l'image 'start'
            frame_time=0
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if START_REGION.collidepoint(mouse_x, mouse_y):
                if pygame.mouse.get_pressed()[0]:
                    start_screen=False
        if LEAVE_REGION.collidepoint(mouse_x, mouse_y):
                if pygame.mouse.get_pressed()[0]:  # Si l'utilisateur clique
                    pygame.quit()
                    sys.exit()
        for event in pygame.event.get():
        # Si l'utilisateur ferme la fenêtre
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    if Win==True:
                
        if musique_play==False:
            musique_play=True
            current_song_index = 0
            pygame.mixer.music.load(music_files[current_song_index])
            pygame.mixer.music.play(-1)
        ####print(Win)
        START_REGION = pygame.Rect(517, 125, 759 - 517, 179 - 125)
        LEAVE_REGION = pygame.Rect(1116, 675, 1280 - 1116, 720 - 675)
        frame_time+=1
        # Logique pour afficher les images
        if frame_time == 10:  # Chaque 60 frames
            screen.blit(win1, (0, 0))  # Affiche l'image 'start'
        elif frame_time ==20:
            screen.blit(win2, (0, 0))  # Affiche l'image 'start'
        elif frame_time ==30:
            screen.blit(win3, (0, 0))  # Affiche l'image 'start'
        elif frame_time ==40:
            screen.blit(win4, (0, 0))  # Affiche l'image 'start'
            frame_time=0
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if START_REGION.collidepoint(mouse_x, mouse_y):
                if pygame.mouse.get_pressed()[0]:
                    Win=False
                    level1()
                    
        if LEAVE_REGION.collidepoint(mouse_x, mouse_y):
                if pygame.mouse.get_pressed()[0]:  # Si l'utilisateur clique
                    pygame.quit()
                    sys.exit()
        for event in pygame.event.get():
        # Si l'utilisateur ferme la fenêtre
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    if next==True:
        ####print(Win)
        START_REGION = pygame.Rect(517, 125, 759 - 517, 179 - 125)
        LEAVE_REGION = pygame.Rect(1116, 675, 1280 - 1116, 720 - 675)
        frame_time+=1
        # Logique pour afficher les images
        if frame_time == 10:  # Chaque 60 frames
            screen.blit(next1, (0, 0))  # Affiche l'image 'start'
        elif frame_time ==20:
            screen.blit(next2, (0, 0))  # Affiche l'image 'start'
        elif frame_time ==30:
            screen.blit(next3, (0, 0))  # Affiche l'image 'start'
        elif frame_time ==40:
            screen.blit(next4, (0, 0))  # Affiche l'image 'start'
            frame_time=0
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if START_REGION.collidepoint(mouse_x, mouse_y):
                if pygame.mouse.get_pressed()[0]:
                    next=False
                    if Level==0:
                        level1()
                    elif Level==1:
                        level2()
                    
        if LEAVE_REGION.collidepoint(mouse_x, mouse_y):
                if pygame.mouse.get_pressed()[0]:  # Si l'utilisateur clique
                    pygame.quit()
                    sys.exit()
        for event in pygame.event.get():
        # Si l'utilisateur ferme la fenêtre
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            

    pygame.display.update()  # Mettre à jour l'affichage







