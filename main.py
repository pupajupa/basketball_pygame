import pygame

pygame.init()

# global variable
width = 1000
heigth = 680
screen = pygame.display.set_mode((width, heigth))

background = pygame.image.load("assets/images/background.png")
base = pygame.image.load("assets/images/road.png")
basketball = pygame.image.load("assets/images/basketball.png")


def main():
    gameOn = True
    baseX = 0
    baseY = heigth - 120
    ballX = 100
    ballY = baseY - 120
    gravity = 10
    bouncing = 25

    while gameOn:
        # taking event
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                gameOn = False
        screen.blit(background, (0, 0))
        screen.blit(base, (baseX, baseY))
        screen.blit(basketball, (ballX, ballY))

        # bouncing
        ballY -= bouncing
        bouncing -= 1
        ballY += gravity
        if ballY > baseY - 20:
            bouncing = 25

        pygame.display.update()


if __name__ == "__main__":
    main()
