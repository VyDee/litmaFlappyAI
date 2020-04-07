import pygame
import neat
import time
import os
import random

pipe_scale = (100, 500)

PIPE_IMG = [pygame.transform.scale(pygame.image.load(os.path.join("imgs", "litpipet.png")),pipe_scale),
            pygame.transform.scale(pygame.image.load(os.path.join("imgs", "litpipeb.png")),pipe_scale)]

class Pipe:
    GAP = 200
    VEL = 5
    
    #--top and bottom: where is the top and bottom of the pipe will be drawn
    #--PIPE_TOP and PIPE_BOTTOM: get image for top and bottom pipe, pipe top is to flip the pipe upside down
    #--passed: if the bird is already passed by the pipe
    #--set_height: determine where the top and bottom of our pipe and how tall top verse bottm and the middle gap
    def __init__(self,x):
        self.x = x
        self.height = 0

        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = PIPE_IMG[0]
        self.PIPE_BOTTOM = PIPE_IMG[1]

        self.passed = False
        self.set_height()
    
    def set_height(self):
        self.height = random.randrange(50,450) #450 #where we want the top of our pipe to be on the screen
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP
    
    def move(self):
        self.x -= self.VEL
    
    def draw(self,win):
        win.blit(self.PIPE_TOP, (self.x,self.top))
        win.blit(self.PIPE_BOTTOM,(self.x,self.bottom))
    
    def collide (self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x -bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        if t_point or b_point: #ask if they are not none or if we are colliding
            return True

        return False