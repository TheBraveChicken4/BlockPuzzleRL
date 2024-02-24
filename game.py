import pygame
import random

# Set up the Pygame display variables
WIDTH = 600
HEIGHT = 800

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Set the title of the window
pygame.display.set_caption('Block Puzzle')

# draw grid and make the lines 50 % of the opacity alpha
def draw_grid():

    rows = 9 # Amount of lines per side
    columns = 9 # Amount of lines per side
    block_dimensions = 50

    # Draw the grid width lines for a 400 x 400 grid in the middle of the screen
    # Vertical Lines
    for i in range(0, rows):
        pygame.draw.line(window, (128, 128, 128), (100, (i * 50) + 100), (500, (i * 50) + 100))

    # Horizontal Lines
    for i in range(0, columns):
        pygame.draw.line(window, (128, 128, 128), ((i * 50) + 100, 100), ((i * 50) + 100, 500))

    #Draw selection queue
    pygame.draw.line(window, (128, 128, 128), (0, 600), (600, 600), 1)
    pygame.draw.line(window, (128, 128, 128), (0, 700), (600, 700), 1)

    
# Setup the game loop variables
running = True

# The game loop
while running:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((35, 35, 200))
    draw_grid()
    pygame.display.update()
    clock.tick(60)

pygame.quit


# class block:

#     colors = {"Purple": (142, 60, 205), "Blue": (0, 0, 255), 
#               "Green": (0, 255, 0), "Yellow": (255, 255, 0), 
#               "Orange": (255, 140, 0), "Red": (255, 0, 0)}
    
#     shapes = 

#     def __init__(self):
#         self.color = color
#         self.shape = shape