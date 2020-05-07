import pygame
import neat
import time
import os
import random
from Bird import Bird
from Pipe import Pipe
from Base import Base
from Background import Background

pygame.font.init()

WIN_WIDTH = 500
WIN_HEIGHT = 800

GEN = 0

STAT_FONT = pygame.font.SysFont("comicsans",50)

def draw_window(win, birds, pipes, base,score, gen, bg):
    #win.blit(BG_IMG, (0,0)) #blit means draw

    bg.draw(win)
    for pipe in pipes:
        pipe.draw(win)
    
    text = STAT_FONT.render("Score: " + str(score),1,(255,255,255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    text = STAT_FONT.render("Gen: " + str(gen),1,(255,255,255))
    win.blit(text, (10, 10))

    base.draw(win)

    for bird in birds:
        bird.draw(win)
    pygame.display.update()

def main(genomes, config):
    global GEN
    GEN +=1
    nets = []
    ge = []
    birds = []

    #set up the neural netwrok genomes
    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(230,350))
        g.fitness = 0
        ge.append(g)

    base = Base(730)
    pipes = [Pipe(450)]
    bg = Background()
    win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    clock = pygame.time.Clock()

    score = 0

    run = True
    while run:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        pipe_ind = 0 #pipe index
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1
        else:
            run = False #if there is not bird left, then quit running
            break

        for x, bird in enumerate(birds):
            bird.move()
            ge[x].fitness += 0.1 #make sure the bird stay alive every 20 secs stay alive will gain 1 fitness point
            output = nets[x].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom))) #activate output with inputs

            if output[0] > 0.5:
                bird.jump()

        add_pipe = False
        rem =[] 
        for pipe in pipes:
            for x, bird in enumerate(birds):
                #if the bird collides with the pipe
                if pipe.collide(bird):
                    #every time the bird hits the pipe, we remove 1 fitness point from the bird
                    ge[x].fitness -= 1
                    birds.pop(x) #once it hits, remove the failing birds and anything associated with it
                    nets.pop(x)
                    ge.pop(x)

                #if the bird passed the pipe
                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed =True
                    add_pipe = True

            if pipe.x + pipe.PIPE_TOP.get_width() < 0 :
                rem.append(pipe)
            pipe.move()
        
        if add_pipe:
                score += 1
                for g in ge:
                    g.fitness += 5 #pass through pipes will gain 5 to fitness score
                pipes.append(Pipe(700))
        for r in rem:
            pipes.remove(r)
         
         #if the bird hits the ground, remove bird
        for x,bird in enumerate(birds):
            if bird.y + bird.img.get_height() >= 730 or bird.y < 0 :
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)
        base.move()
        draw_window(win,birds, pipes, base, score, GEN,bg)

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,neat.DefaultStagnation,
                                config_path) #define all the properties in Neat that we use
    
    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main,50)

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt") #load the config file
    run(config_path)
