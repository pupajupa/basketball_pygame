import pygame

pygame.init()

#global variable 
width = 750
heigth = 550
screen = pygame.display.set_mode((width,heigth))
gameOn = True

while gameOn:
    #taking event
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameOn=False
