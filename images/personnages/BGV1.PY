import pygame, sys
from pygame.locals import *
import subprocess
import random
pygame.init()

pygame.display.set_caption('Pygame Window')
clock = pygame.time.Clock()
WINDOW_SIZE = (1280, 720)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

START_REGION = pygame.Rect(519, 124, 232, 53)
LEAVE_REGION = pygame.Rect(1116, 675, 146, 33)

# Liste des coordonnées des carrés
YELLOW_SQUARES = [
    (371, 39, 15, 15),
    (632, 92, 16, 22),
    (893, 38, 16, 16),
    (861, 506, 10, 10),
    (910, 517, 10, 11),
    (954, 507, 10, 9),
]
BLUE_SQUARES = [
    (567, 92, 582, 108),
    (834, 65, 849, 81),
]
GREEN_SQUARES = [
    (430, 65, 447, 81),
    (697, 92, 713, 108),
]
RED_SQUARES = [
    (501, 87, 516, 103),
    (763, 87, 778, 103),
    (883, 452, 893, 462),
    (931, 452, 942, 462),
    (844, 550, 854, 560),
    (910, 556, 920, 556),
    (970, 550, 979, 560),
]

class Game:
    def __init__(self):
        self.running = True
        self.bg = pygame.image.load('START.png').convert()
        self.bg.set_colorkey((0, 0, 0))
        self.display_time = 0  # Temps pour afficher les carrés

    def start_game(self):
        print("Game started!")
        subprocess.run(["python", "v18.py"])
        pygame.quit()
        sys.exit()

    def close_game(self):
        self.running = False
        print("Game closed!")

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if START_REGION.collidepoint(mouse_x, mouse_y):
                if pygame.mouse.get_pressed()[0]:
                    self.start_game()
            if LEAVE_REGION.collidepoint(mouse_x, mouse_y):
                if pygame.mouse.get_pressed()[0]:
                    self.close_game()

            screen.fill((0, 0, 0))
            screen.blit(self.bg, (0, 0))

            # Choisir une couleur et dessiner les carrés
            nb = random.randint(0, 3)
            self.display_time = pygame.time.get_ticks()  # Obtient le temps actuel en millisecondes

            if nb == 1:
                for lampe_jaunes in YELLOW_SQUARES:
                    pygame.draw.rect(screen, (255, 255, 0), lampe_jaunes)
            elif nb == 2:
                for lampe_vertes in GREEN_SQUARES:
                    pygame.draw.rect(screen, (0, 255, 0), lampe_vertes)
            elif nb == 3:
                for lampe_rouges in RED_SQUARES:
                    pygame.draw.rect(screen, (255, 0, 0), lampe_rouges)
            else:
                for lampe_bleus in BLUE_SQUARES:
                    pygame.draw.rect(screen, (0, 0, 255), lampe_bleus)

            pygame.display.update()
            clock.tick(60)

        pygame.quit()
        sys.exit()


game = Game()
game.run()
