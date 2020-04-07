import pygame
import neat
import time
import os
import random

BG_IMG = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "matrixbg.jpg")),(500,800))

class Background:
    def draw(self, win):
        win.blit(BG_IMG, (0,0))
