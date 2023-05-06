import pygame
import math


WIN = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Planet Simulation in Python")

WHITE = (255, 255, 255)

class Planet():
    def __init__(self, x, y, radius, mass):
        pass
    
    def draw(self, win):
        pass


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    WIN.fill(WHITE)
