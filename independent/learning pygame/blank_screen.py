import pygame #importing pygame

pygame.init() #initializing pygame
screen = pygame.display.set_mode((800, 400)) #creating a screen

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    #draw all our elements
    # update everithing
    pygame.display.update()
    