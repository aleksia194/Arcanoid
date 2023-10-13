import pygame
from random import *

WIDTH = 800
HEIGHT = 700
FPS = 120
pygame.init()

SPEED = 0
deviation = 0

gamemode = 1
ballmode = 1

brick_w = 100
kol_brick_to_line = WIDTH // brick_w


def kontur():
    pygame.draw.rect(sc, (128, 0, 128), (0, 0, WIDTH, HEIGHT), 10)


def random_color():
    a = randint(50, 255)
    b = randint(50, 255)
    c = randint(50, 255)
    return (a, b, c)


line = 10
score = 0

brick_list = []
color_list = []


def new_brick1():
    global brick_list, color_list, line
    brick_list = []
    color_list = []
    for j in range(10):
        for i in range(8):
            brick = pygame.Rect(100 * i, 25 * j, 100, 25)
            brick_list.append(brick)
            color_list.append(random_color())


ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_x_speed = 0
ball_y_speed = 0

right_line_distance = WIDTH - 100

dx, dy = -1, 1

ball_x_speed += random()


def rikoshet():
    global gamemode, ballmode, ball_y, ball_x, dx, dy, ball_x_speed, ball_y_speed

    if platform.colliderect(ball):
        dy = 1
        if SPEED > 1:
            pass

    if ball.collidelist(brick_list) != -1:
        dy = -1

    if ball_y <= 6:
        dy = -1

    if ball_y > HEIGHT + 100:
        # running = False
        ballmode = 1
        ball_y_speed = 0

        ball_x, ball_y = platform.x + 50, platform.y - 6
        gamemode = 1

        print("louse")

    if ball_x <= 6:
        dx = 1

    if ball_x >= WIDTH - 6:
        dx = -1
    return dx, dy


sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 26)
font_big = pygame.font.SysFont("Arial", 50)

start_txt = font.render("новая игра", 1, (255, 255, 0))
start_rect = pygame.Rect(10, 10, 150, 50)
start_rect.center = start_txt.get_rect(x=(WIDTH // 2) - 50, y=(HEIGHT // 3) - 150).center

next_txt = font.render("продолжить", 1, (255, 255, 0))
next_rect = pygame.Rect(10, 10, 150, 50)
next_rect.center = start_txt.get_rect(x=(WIDTH // 2) - 50, y=(HEIGHT // 3)).center

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if ballmode == 1 and gamemode == 2:
                    ballmode = 2
                    ball_y_speed = -5
                    ball_x_speed = 5
                    ball_x, ball_y = platform.x + 50, platform.y - 6

                if start_rect.collidepoint(event.pos) and gamemode == 1 or gamemode == 3:
                    line = 2
                    score = 0
                    ballmode = 1
                    gamemode = 2
                    new_brick1()

                if next_rect.collidepoint(event.pos) and gamemode == 1 or gamemode == 3:
                    line += 1
                    ballmode = 1
                    gamemode = 2
                    new_brick1()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gamemode = 1

    sc.fill((0, 0, 0))

    mouse = pygame.mouse.get_pos()

    if gamemode == 1:
        kontur()
        pygame.draw.rect(sc, (128, 0, 128), start_rect)
        pygame.draw.rect(sc, (100, 0, 100), start_rect, 15)
        pygame.draw.rect(sc, (80, 0, 80), start_rect, 10)
        pygame.draw.rect(sc, (60, 0, 60), start_rect, 5)
        pygame.draw.rect(sc, (0, 0, 0), start_rect, 1)
        sc.blit(start_txt, [(WIDTH // 2) - 50, (HEIGHT // 3) - 153])
    elif gamemode == 2:
        kontur()
        platform = pygame.draw.rect(sc, (255, 255, 255), (mouse[0] - 50, 630, 100, 15))

        ball_x += ball_x_speed * dx
        ball_y += ball_y_speed * dy

        if ballmode == 1:
            ball = pygame.draw.circle(sc, (200, 200, 200), (platform.x + 50, platform.y - 6), 6)
        elif ballmode == 2:
            SPEED = 5

            ball = pygame.draw.circle(sc, (200, 200, 200), (ball_x, ball_y), 6)
        dx, dy = rikoshet()

        rikoshet()
        if ball.collidelist(brick_list) != -1:
            num = ball.collidelist(brick_list)
            del brick_list[num]
            del color_list[num]
            score += randint(100, 1000)

        for i in brick_list:
            pygame.draw.rect(sc, color_list[brick_list.index(i)], i)
            pygame.draw.rect(sc, (255, 255, 255), i, 1)

        if len(brick_list) == 0:
            gamemode = 3
            ball_x_speed = 0
            ball_y_speed = 0
        sc.blit(font.render(str(score), 1, (255, 255, 0)), [100, 600])
    elif gamemode == 3:
        kontur()
        pygame.draw.rect(sc, (128, 0, 128), start_rect)
        pygame.draw.rect(sc, (100, 0, 100), start_rect, 15)
        pygame.draw.rect(sc, (80, 0, 80), start_rect, 10)
        pygame.draw.rect(sc, (60, 0, 60), start_rect, 5)
        pygame.draw.rect(sc, (0, 0, 0), start_rect, 1)
        sc.blit(start_txt, [(WIDTH // 2) - 50, (HEIGHT // 3) - 153])

        pygame.draw.rect(sc, (128, 0, 128), next_rect)
        pygame.draw.rect(sc, (100, 0, 100), next_rect, 15)
        pygame.draw.rect(sc, (80, 0, 80), next_rect, 10)
        pygame.draw.rect(sc, (60, 0, 60), next_rect, 5)
        pygame.draw.rect(sc, (0, 0, 0), next_rect, 1)
        sc.blit(next_txt, [(WIDTH // 2) - 58, (HEIGHT // 3) - 4])

        pygame.draw.rect(sc, (128, 0, 128), (250, 300, 300, 150), 4)
        sc.blit(font_big.render(" вы выйграли!", 1, (255, 255, 0)), [(WIDTH // 3), (HEIGHT // 2)])
        pygame.draw.rect(sc, (128, 0, 128), (150, 450, 500, 50), 4)
        sc.blit(font.render(str(score), 1, (255, 255, 0)), [155, 460])
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
