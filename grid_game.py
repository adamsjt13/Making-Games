"""
Pygame base template for opening window
http://programarcadegames.com
"""

import pygame
import random
import time

# initialize game engine
pygame.init()

# define colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

# set up display screen
size = (255,285)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

# score output
# initialize score
score = 0
# font selection
font = pygame.font.SysFont('Calibri',25,True,False)

# loop until user clicks close
done = False

# manage screen update rate
clock = pygame.time.Clock()

# set width, height, and margin for grid blocks
width = 20
height = 20
margin = 5

# initialize grid array
grid = [[0 for x in range(10)] for y in range(10)]

# set default color for squares
color = WHITE

# function for converting coordinates to grid row, column
def convert_grid_coord(x,y):
    """
    This function takes in x and y coordinates and
    converts it to the row and column of box clicked
    """
    # define default row and column if black space is clicked
    row, column = 999, 999
    # start and end coords of squares
    start = list(range(4,230,25))
    end = list(range(24,255,25))
    # check to see if mouse click is in valid square
    for i in range(len(start)):
        if x > start[i] and x < end[i]:
            column = i 
        if y > start[i] and y < end[i]:
            row = i 
    return [row, column]

# function to randomly generate green boxes every 5 secs
def generate_boxes():
    """
    This function will be used to random color boxes green
    so the user can click them for points
    """
    # generate between 3 and 10 boxes
    num_boxes = random.randint(3,10)
    for i in range(num_boxes):
        x = random.randint(0,9)
        y = random.randint(0,9)
        grid[x][y] = 1

# start timer
start = time.time()

# game length (sec)
game_time = 10
remaining_time = 10

# ------- Main Loop --------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            # get coords of mouse click
            mouseX, mouseY = event.pos
            # convert to row/column coord
            grid_coord = convert_grid_coord(mouseX,mouseY)
            # set grid vector to equal 1 at mouse click location
            try:
                if grid[grid_coord[0]][grid_coord[1]] == 1:
                    grid[grid_coord[0]][grid_coord[1]] = 0
                    score += 1
##                # print row and column of click to console
##                print("Row: ", grid_coord[0] + 1, " ", "Column: ",
##                      grid_coord[1] + 1, sep = "")
            except IndexError:
                continue       
    # set screen to white
    screen.fill(BLACK)

    if remaining_time > 0:
        # ---- drawing code
        for column in range(10):
            # create new boxes with margin between them
            new_x = column * width + column * margin
            for row in range(10):
                new_y = row * height + row * margin
                # draw green square if grid value == 1
                if grid[row][column] == 1:
                    # add margin to initial box so not at origin
                    pygame.draw.rect(screen, GREEN, [new_x+margin,new_y+margin,
                                                 height,width])
                else:
                    pygame.draw.rect(screen, color, [new_x+margin,new_y+margin,
                                                 height,width])
                    
        # ---- print score
        # render text
        text = font.render("Score: " + str(score), True, GREEN)
        # put image on screen
        screen.blit(text, [0,255])

        # check timer for game and print out
        elapsed_time = round(time.time() - start, 1)
        remaining_time = game_time - round(elapsed_time, 0)
        
        # ---- print time
        # render text
        text = font.render("Time: " + str(remaining_time), True, GREEN)
        # put image on screen
        screen.blit(text, [100,255])
        
        # ---- update screen
        pygame.display.flip()

        # limit to 60 fps
        clock.tick(60)

        # only generate new boxes every 3 sec
        if elapsed_time % 3 == 0:
            # initialize grid array
            grid = [[0 for x in range(10)] for y in range(10)]
            generate_boxes()
    else:
        # ---- end game screen
        screen.fill(BLACK)
        # render game over text
        text = font.render("GAME OVER!!", True, GREEN)
        # put image on screen
        screen.blit(text, [65,130])
        # render final score text
        text = font.render("Score: " + str(score), True, GREEN)
        # put image on screen
        screen.blit(text, [85,155])
        # ---- update screen
        pygame.display.flip()

        
        
# close the window and quit
pygame.quit()


    
