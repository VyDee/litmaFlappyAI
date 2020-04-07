import pygame
import neat
import time
import os
import random

bird_scale = (50,50)
x,y = bird_scale

BIRD_IMGS = [
    pygame.transform.scale(pygame.image.load(os.path.join("imgs", "litmand0.png")),bird_scale),
    pygame.transform.scale(pygame.image.load(os.path.join("imgs", "litmand0.png")),(x,y + 4)),
    pygame.transform.scale(pygame.image.load(os.path.join("imgs", "litmand0.png")),(x,y + 8)),
    pygame.transform.scale(pygame.image.load(os.path.join("imgs", "litmand0.png")),(x,y + 12)),
    pygame.transform.scale(pygame.image.load(os.path.join("imgs", "litmand0.png")),(x,y + 16)),
    pygame.transform.scale(pygame.image.load(os.path.join("imgs", "litmand0.png")),(x,y + 20)),
    pygame.transform.scale(pygame.image.load(os.path.join("imgs", "litmand0.png")),(x,y + 24)),
    pygame.transform.scale(pygame.image.load(os.path.join("imgs", "litmand0.png")),(x,y + 28)),
    pygame.transform.scale(pygame.image.load(os.path.join("imgs", "litmanu0.png")),bird_scale),
    pygame.transform.scale(pygame.image.load(os.path.join("imgs", "litmanu1.png")),(x+2,y)),
    pygame.transform.scale(pygame.image.load(os.path.join("imgs", "litmanu2.png")),(x+4,y)),
    pygame.transform.scale(pygame.image.load(os.path.join("imgs", "litmanu3.png")),(x+6,y)),
    pygame.transform.scale(pygame.image.load(os.path.join("imgs", "litmanu4.png")),(x+8,y)),
    pygame.transform.scale(pygame.image.load(os.path.join("imgs", "litmanu5.png")),(x+10,y)),
    pygame.transform.scale(pygame.image.load(os.path.join("imgs", "litmanu6.png")),(x+12,y)),
]

class Bird:

    #--max rotation: how the bird is gonna tilt its head up or down and how many degree
    #--rotaion velocity: how long we are gonna rotate on the frame everytime we move the bird
    #--animation time: how long we are gonna show each bird animation, how fast the bird is flapping
    #its wing in the frame           
    IMGS = BIRD_IMGS
    MAX_ROTATION = 0
    ROT_VEL = 20
    ANIMATION_TIME = 2

    #--init function
    #--tilt: start with the bird looking flat
    #--tick_count: use to figure when we jump, when we fall down
    #--velocity = 0 is because bird doesn't move
    #--img_count: we know what bird image we are using
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0 
        self.height = y
        self.img_count = 0
        self.img = self.IMGS[0]
        self.bird_jump = False
    
    #jump function
    #--velocity = -10.5 because the top left of the screen is (0,0)
    #since the bird position is below 0 on the screen:
        #if the bird goes up, it will have a negative velocity in y direction -- look up gravity for more info
        #if it goes down, it will have a positive velocity in y direction
        #if it goes right, it will be positive velocity in x direction
        #if it goes left, it will be negative velocity in x direction
    #--tick_count: keep track of where we last jump. We set to 0 because
    #we need to know when we change direction or velocity
    #-- height: where the bird jump from or move from
    def jump(self):
        self.bird_jump = True
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y
    
    #move function -- when we call every single frame to move the bird
    #--tick_count: a tick happens a frame went by
    #--d (displayment): how many pixels moving up or down a frame.
    #This is when we end up moving when we change the y position of the bird
        #vel * tick_count: based on velocity to calculate how many seconds we move
    def move(self):
        self.bird_jump = False
        self.tick_count += 1  

        d = self.vel*self.tick_count + 1.5*(self.tick_count**2)

        #if we are moving down to 16 pixels, we don't accelerate anymore
        #displacement will be set to 16
        if d >= 16:
            d = 16
        if d < 0:
            d -= 2
        self.y += d

        # if d < 0 or self.y < self.height + 50: #move upward
        #     if self.tilt < self.MAX_ROTATION:
        #         self.tilt = self.MAX_ROTATION
        # else:
        #     if self.tilt > -90:
        #         self.tilt -= self.ROT_VEL
    
    def draw(self, win):
        # if self.bird_jump:
        self.img_count += 1
        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*1:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMGS[2]
        elif self.img_count <self.ANIMATION_TIME*3:
            self.img = self.IMGS[3]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMGS[4]
        elif self.img_count < self.ANIMATION_TIME*5:
            self.img = self.IMGS[5]
        elif self.img_count <self.ANIMATION_TIME*6:
            self.img = self.IMGS[6]
        elif self.img_count <self.ANIMATION_TIME*7:
            self.img = self.IMGS[7]
        elif self.img_count <self.ANIMATION_TIME*8:
            self.img = self.IMGS[8]
        elif self.img_count < self.ANIMATION_TIME*9:
            self.img = self.IMGS[9]
        elif self.img_count < self.ANIMATION_TIME*10:
            self.img = self.IMGS[10]
        elif self.img_count <self.ANIMATION_TIME*10+1:
            self.img = self.IMGS[11]
        elif self.img_count <self.ANIMATION_TIME*12:
            self.img = self.IMGS[12]
        elif self.img_count <self.ANIMATION_TIME*13:
            self.img = self.IMGS[13]
        # elif self.img_count <self.ANIMATION_TIME* 14:
        #     self.img = self.IMGS[14]
        elif self.img_count == self.ANIMATION_TIME*13 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0
        # else:
        #     self.img = self.IMGS[0]
        
        # if self.tilt <= -80:
        #     self.img = self.IMGS[1]
        #     self.img_count = self.ANIMATION_TIME*2
    
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)
    
    #--get_mask: used on birds to get 2 dimension list representing the pixels
    def get_mask(self):
        return pygame.mask.from_surface(self.img)