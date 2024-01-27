import pygame
import random

pygame.init()

# global variable
width = 1000
heigth = 680
screen = pygame.display.set_mode((width, heigth))
fps = 60
clock = pygame.time.Clock()

# images
background = pygame.image.load("assets/images/background.png").convert_alpha()
base = pygame.image.load("assets/images/road.png").convert_alpha()
basketball = pygame.image.load("assets/images/basketball.png").convert_alpha()
pole = pygame.image.load("assets/images/pole.png").convert_alpha()
basket = pygame.image.load("assets/images/basket.png").convert_alpha()

# sound

# colors
red = (255, 0, 0)
black = (0, 0, 0)


def getPoleY(baseY):
    return random.randrange(148, baseY - 294)


def ScreenText(text, color, x, y, size, style, bold=False, itallic=False):
    font = pygame.font.SysFont(style, size, bold=bold, italic=itallic)
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, (x, y))


def random_basket(poleY, baseY):
    return random.randrange(poleY - 10, baseY - 215)


def get_heighest_score():
    with open("highest score.txt", "r") as f:
        return f.read()


def moving_base(baseX, baseY, base):
    screen.blit(base, (baseX, baseY))
    screen.blit(base, (baseX + width, baseY))


def collision(poleX, poleY, ballX, ballY):
    if ballX >= poleX - 42 and ballX <= poleX - 42 + 134 and ballY > poleY:
        return True
    elif ballY < -10:
        return True
    return False


def main():
    gameOn = True
    baseX = 0
    baseY = heigth - 120
    ballX = 96
    ballY = baseY - 123
    gravity = 10
    bouncing = 25
    poleX = 700
    poleY = getPoleY(baseY)
    baseX_vel = 0
    poleX_vel = 0
    score = 0
    speed = 0
    gameOver = False
    basketY = random_basket(poleY, baseY)
    basket_score = 0
    speed_accelerating = False
    gameSpeed = 0

    try:
        highest_score = int(get_heighest_score())
    except:
        highest_score = 0

    while gameOn:
        # taking event
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                gameOn = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if gameOver == False:
                        gameSpeed = 0.001
                        bouncing = 25
                        speed = 5
                        baseX_vel = int(speed)
                        poleX_vel = int(speed)
        basketX = poleX + 54
        screen.blit(background, (0, 0))
        moving_base(baseX, baseY, base)
        screen.blit(pole, (poleX, poleY))
        screen.blit(basket, (basketX, basketY))
        screen.blit(basketball, (ballX, ballY))

        # bouncing
        ballY -= bouncing
        bouncing -= 1
        ballY += gravity
        if ballY > baseY - 20:
            bouncing = 25
            speed = 5
            baseX_vel = int(speed)
            poleX_vel = int(speed)

            # moving pole
        poleX += -poleX_vel
        if poleX < -100:
            poleX = width + 10
            poleY = getPoleY(baseY)

        # moving base
        baseX += -baseX_vel
        if baseX <= -width:
            baseX = 0

        # collision of basketball
        gameOver = collision(poleX, poleY, ballX, ballY)
        if gameOver:
            ScreenText("Game Over", red, 200, 100, 60, "Arial", bold=True)
            speed = 0
            bouncing = 0
            gravity = 0
            baseX_vel = 0
            poleX_vel = 0
            score = 0
            basket_score = 0
            gameOver = True
        # ball into the basket
        else:
            if (
                ballX + basketball.get_width() >= basketX
                and ballX <= basketX + basket.get_width()
                and ballY > basketY
                and ballY <= basketY + basket.get_height()
            ):
                basket_score += 100

        # accelerating
        speed += gameSpeed
        # speeding riup score
        score += int(speed)
        # display score
        ScreenText(f"Score {score}", black, 10, 40, size=20, style="Calibri")
        ScreenText(
            f"basket_score {basket_score}", black, 10, 10, size=20, style="Calibri"
        )

        # checking highest score

        if highest_score < score:
            highest_score = score

        with open("highest score.txt", "w") as f:
            f.write(str(highest_score))

        ScreenText(
            f"Highest score {highest_score}",
            red,
            width - 200,
            10,
            size=14,
            style="Calibri",
        )

        pygame.display.update()
        clock.tick(fps)


if __name__ == "__main__":
    main()
