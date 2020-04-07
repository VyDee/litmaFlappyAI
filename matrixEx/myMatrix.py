import pygame, random
 
# Initialize the game engine
pygame.init()
 
black = [0, 0, 0]
green = [0,155,0]

# Set the height and width of the screen
X, Y = [700, 500]  # you will need the individual screen dimensions later
 
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("The Matrix Rain Effect")
screen.fill(black)

SIZE = 12  # a new SIZE parameter
row_height = SIZE * 1

font=pygame.font.Font(None, SIZE)
symbols = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@£#%&")  # create a list of strings

columns =[[],[],[]]
#column = []  # an empty column
y_pos = 0

done = False
while not done:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    for column in columns:
        # add new symbol #
        symbol = random.choice(symbols)  # pick one symbol
        column.append([symbol, y_pos])  # add symbol and position to column
        #columns[1].append([symbol, y_pos]) 
        y_pos += row_height  # change y_pos with the height of one symbol
    
    # start over #
    if y_pos > Y:
        y_pos = 0
        columns[0] = []
        columns[1] = []
        columns[2] = []

    for column in columns:
        # send to screen #
        for symbol, pos in columns[0]:  # run through the column
            surface = font.render(symbol, True, green)
            screen.blit(surface, [20, pos])
        for symbol, pos in columns[1]:  # run through the column
            surface = font.render(symbol, True, green)
            screen.blit(surface, [50, pos])
        for symbol, pos in columns[1]:  # run through the column
            surface = font.render(symbol, True, green)
            screen.blit(surface, [80, pos])
    
    pygame.time.wait(1000)
    pygame.display.flip()

pygame.quit()
