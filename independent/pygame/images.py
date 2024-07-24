#importing pygame
import pygame 
from sys import exit

pygame.init() #initializing pygame
#secend step creating display surface (screen)
screen = pygame.display.set_mode((800, 400)) #creating a screen
#title of our page
pygame.display.set_caption("runner")
##FPS
clock = pygame.time.Clock() # this doesnt do anything by its own



#==========================================================
# create surface
#==========================================================
test_surface = pygame.Surface((100, 200))
test_surface.fill("red")

while True:
    # quit the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # when we call this we are doing the opposit of pygame.init()
            # we have to write this so the while loop stops too
            exit() # this will close the while loop too
    
    # ================================================
    # to display images we need surface in pygame there are 2 types of surfaces
    # 1. display surface -- THE GAME WINDOW
    # 2. regular surface -- somthing imported, rendered text or plain color 
    #    we need to put this on a display surface for it to be visible
    # ================================================
    screen.blit(test_surface, (0,0)) #blit -- block image transfer.|| we place surfaces on display surfaces with this
    
    
    
    
    # ================================================
    
    
    
    
    
    
    #draw all our elements
    # update everithing
    pygame.display.update()
    # call the clock function
    # this will limit the frames per second to 60 fps. 
    # this helps us to maintain a consistent frame rate
    # if we don't call this, our program will run at the maximum possible speed.
    clock.tick(60) 
    
    