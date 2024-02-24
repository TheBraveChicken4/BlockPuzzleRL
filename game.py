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


block_width, block_height = 100, 50
block_rects = [pygame.Rect(300, 200, block_width, block_height), 
               pygame.Rect(400, 200, block_width, block_height)]
dragging = False
offset_x, offset_y = 0, 0
WHITE = (255, 255, 255)


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
    #
    pygame.draw.line(window, (128, 128, 128), (0, 600), (600, 600), 1)
    pygame.draw.line(window, (128, 128, 128), (0, 700), (600, 700), 1)


# class blrock:

#     brick_size = 25
#     colors = {"Purple": (142, 60, 205), "Blue": (0, 0, 255), 
#               "Green": (0, 255, 0), "Yellow": (255, 255, 0), 
#               "Orange": (255, 140, 0), "Red": (255, 0, 0)}

#     #Add the name for each shape so we can call it later
#     shape = ["single", "2_horizontal", "3_horizontal", "4_horizontal", "5_horizontal"
#               "2_vertical", "3_vertical", "4_vertical", "5_vertical",
#               "small_corner_left", "small_corner_right", "big_corner_left", "big_corner_right"
#               "z_shape_left", "z_shape_right", "lightning", "lightning_flipped",
#               "2x2", "3x3", "triangle", "trinangle_90", "triangle_180", "triangle_270"]
    


#     def __init__(self, color):
#         self.color = color
#         self.shape = self.shape[random.randint(0, len(self.shape) - 1)]


   

# Setup the game loop variables
running = True

# Main game loop
while running:  

    '''
        My current issue is that when I have multiple blocks with different x and y values, and I want them to stay connected
        they are both getting set to the same position of the mouse and therefore covering each other.
        #TODO: Figure out how to keep the distance between the blocks but still be able to move them
    '''


    test = 0
    #Track all the events that happen in the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #This code checks to see if the mouse is cliking on the block and updating the position of the block accordingly
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for block_rect in block_rects:
                    if block_rect.collidepoint(event.pos):
                        dragging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = block_rect.x - mouse_x + test
                        offset_y = block_rect.y - mouse_y
                        test += 50
                        break
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                mouse_x, mouse_y = event.pos
                for block_rect in block_rects:
                    block_rect.x = mouse_x + offset_x
                    block_rect.y = mouse_y + offset_y


    window.fill((35, 35, 200))  

    for block_rect in block_rects:
        pygame.draw.rect(window, WHITE, block_rect)
        print(block_rect, " Done")

    draw_grid()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()