import pygame
import time
import random

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 512
dis_height = 512

pygame.init()
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Bart')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# bart use picture

melon = pygame.image.load('melon.png').convert_alpha()
malcom = pygame.image.load('malcom.jpg').convert_alpha()
subaru = pygame.image.load('subaru.png').convert_alpha()
wtf = pygame.image.load('wtf.png').convert_alpha()
wtf = pygame.transform.smoothscale(wtf, (40, 40))
melon = pygame.transform.smoothscale(melon, (40, 40))
subaru = pygame.transform.smoothscale(subaru, (40, 40))


def our_snake(snake_block, snake_list):
    for x in snake_list:
        #pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
        dis.blit(wtf, (x[0], x[1]))


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def message2(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 2])

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    enemy_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    enemy_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    redScreen = 0
    while not game_over:

        while game_close == True:
            dis.fill(black)
            dis.blit(malcom, (0, 0))
            message("You Lost!", red)
            message2("Press C-Play Again or Q-Quit", red)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        if redScreen > 1:
            redScreen = redScreen - 1
            dis.fill(red)
        else:
            dis.fill(blue)

        dis.blit(melon, (foodx, foody))
        #move enemy towards the food
        if enemy_y > foody: enemy_y = enemy_y - 1
        elif enemy_y < foody: enemy_y = enemy_y + 1

        if enemy_x > foodx: enemy_x = enemy_x - 1
        elif enemy_x < foodx: enemy_x = enemy_x + 1

        dis.blit(subaru, (enemy_x, enemy_y))
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)
        pygame.display.update()

        if abs(x1 - foodx) < 10 and abs(y1 - foody) < 10:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            redScreen = 30
            dis.fill(red)

        # enemy touched you
        if abs(x1 - enemy_x) < 10 and abs(y1 - enemy_y) < 10:
            game_close = True;

        # enemy touched food
        if abs(foodx - enemy_x) < 10 and abs(foody- enemy_y) < 10:
            game_close = True;
        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
