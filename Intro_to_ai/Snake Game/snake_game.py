import pygame
import random
from che3ck_differcence import is_in_range
from run_snake_game import give_direction
import csv

pygame.init()

screen = pygame.display.set_mode((630, 630))
background = pygame.image.load(
    "/Users/atharvmendhe/Documents/Python_VS_Code/Intro_to_ai/image.png?resize=630%2C631&ssl=1.png"
)

black = (0, 0, 0)
red = (255, 0, 0)
clock = pygame.time.Clock()

starting_snake_X_coordinate = 315.5
starting_snake_Y_coordinate = 472.5
coordinates_change = 31.5

# store_to_csv = []


def snake(snake_coordinates_list):
    for x in snake_coordinates_list:
        pygame.draw.rect(screen, black, [x[0], x[1], 31.5, 31.5])


snake_coordinates_list = []

possible_coordinates_for_food = []
X = 31.5
Y = 31.5
while X < 630:
    while Y < 630:
        possible_coordinates_for_food.append([X, Y])
        Y += 31.5
    X += 31.5
    Y = 31.5


foodx, foody = random.choice(possible_coordinates_for_food)

X_change = 0
Y_change = 0
running = True
length_of_snake = 1
direction_of_head = None

k = 0
l = 3
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    snake_head = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                X_change = 0
                Y_change = 31
                direction_of_head = "down"

            if event.key == pygame.K_UP:
                X_change = 0
                Y_change = -31
                direction_of_head = "up"

            if event.key == pygame.K_RIGHT:
                Y_change = 0
                X_change = 31
                direction_of_head = "right"

            if event.key == pygame.K_LEFT:
                Y_change = 0
                X_change = -31
                direction_of_head = "left"

    starting_snake_X_coordinate += X_change
    starting_snake_Y_coordinate += Y_change

    snake_head.append(starting_snake_X_coordinate)
    snake_head.append(starting_snake_Y_coordinate)
    snake_coordinates_list.append(snake_head)

    # store_to_csv.append((snake_head, [foodx, foody]))

    pygame.draw.rect(screen, red, [foodx, foody, 31, 31])
    if is_in_range(snake_head[0], foodx) and is_in_range(snake_head[1], foody):
        print(l)
        length_of_snake += 1
        foodx, foody = random.choice(possible_coordinates_for_food)
        if length_of_snake % 2 != 0 and l < 9:
            l += 1

    if (
        snake_head[0] <= 0
        or snake_head[0] >= 630
        or snake_head[1] <= 0
        or snake_head[1] >= 630
    ):
        running = False
        print("GAME OVER")

    if len(snake_coordinates_list) > length_of_snake:
        del snake_coordinates_list[0]
    if len(snake_coordinates_list) > 1:
        for coordinates in snake_coordinates_list[:-1]:
            if snake_head[0] == coordinates[0] and snake_head[1] == coordinates[1]:
                running = False
                print("GAME OVER")
    give_direction(snake_head[0], snake_head[1], foodx, foody, direction_of_head)
    snake(snake_coordinates_list)
    k += 1
    clock.tick(l)
    pygame.display.update()


# with open("snake_data.csv", "w", newline="") as file:
#     writer = csv.writer(file)

#     writer.writerow(["headx", "heady", "foodx", "foody"])
#     for list in store_to_csv:
#         writer.writerow([list[0][0], list[0][1], list[1][0], list[1][1]])
