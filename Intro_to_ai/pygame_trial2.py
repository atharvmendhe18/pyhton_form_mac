import pygame
import random
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (50, 153, 213)
green = (0, 255, 0)

dis_width = 600
dis_height = 400
clock = pygame.time.Clock()
 
dis = pygame.display.set_mode((dis_width, dis_height))

snake_block = 10
snake_speed = 15


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 10

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
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
 
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        print(snake_List)
        our_snake(snake_block, snake_List)
 
    
        pygame.display.update()

        
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()        
gameLoop()
