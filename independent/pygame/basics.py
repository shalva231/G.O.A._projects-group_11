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

while True:
    # quit the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # when we call this we are doing the opposit of pygame.init()
            # we have to write this so the while loop stops too
            exit() # this will close the while loop too
            
    
    
    
    
    #draw all our elements
    # update everithing
    pygame.display.update()
    # call the clock function
    # this will limit the frames per second to 60 fps. 
    # this helps us to maintain a consistent frame rate
    # if we don't call this, our program will run at the maximum possible speed.
    clock.tick(60) 
    
    