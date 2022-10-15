'🟩'
'⬛'
'🟨'
import os
import time
import random
import keyboard


def initialize_grid(size, background="⬛"):
    grid = []
    for _ in range(size):
        grid.append(list(background*size))
    return grid


def initialize_snake_position_and_direction(size):
    random_position = [random.randint(1, size-2), random.randint(1, size-2)]
    return random_position


def valid_move(direction, new_direction):
    if new_direction == 'w' and direction[0] != 's':
        return True
    if new_direction == 's' and direction[0] != 'w':
        return True
    if new_direction == 'a' and direction[0] != 'd':
        return True
    if new_direction == 'd' and direction[0] != 'a':
        return True
    return False


def move_snake(snake_body_coordinates, direction):
    if direction == 'w':
        new_head_coordinates = snake_body_coordinates[-1].copy()
        new_head_coordinates[0] -= 1
        snake_body_coordinates.append(new_head_coordinates)
        snake_body_coordinates.pop(0)

    if direction == 's':
        new_head_coordinates = snake_body_coordinates[-1].copy()
        new_head_coordinates[0] += 1
        snake_body_coordinates.append(new_head_coordinates)
        snake_body_coordinates.pop(0)

    if direction == 'a':
        new_head_coordinates = snake_body_coordinates[-1].copy()
        new_head_coordinates[1] -= 1
        snake_body_coordinates.append(new_head_coordinates)
        snake_body_coordinates.pop(0)

    if direction == 'd':
        new_head_coordinates = snake_body_coordinates[-1].copy()
        new_head_coordinates[1] += 1
        snake_body_coordinates.append(new_head_coordinates)
        snake_body_coordinates.pop(0)


def get_snake_direction_from_user(direction):
    if keyboard.is_pressed('w'):
        if valid_move(direction=direction, new_direction='w'):
            direction[0] = 'w'

    if keyboard.is_pressed('s'):
        if valid_move(direction=direction, new_direction='w'):
            direction[0] = 's'

    if keyboard.is_pressed('a'):
        if valid_move(direction=direction, new_direction='w'):
            direction[0] = 'a'

    if keyboard.is_pressed('d'):
        if valid_move(direction=direction, new_direction='w'):
            direction[0] = 'd'
            
    if keyboard.is_pressed('q'):
        quit()


def display_grid(grid, snake_body_coordinates, snake="🟩", background="⬛"):
    #os.system("cls")
    row = 0
    grid_display = ''
    while row < len(grid):
        column = 0
        while column < len(grid):
            if [row, column] in snake_body_coordinates:
                grid_display += snake
            else:
                grid_display += background
            column += 1
        row += 1
        grid_display += "\n"
    print(grid_display)
    time.sleep(0.1)


if __name__ == "__main__":
    grid_size = 20
    direction = ["s"]
    grid = initialize_grid(size=grid_size)
    snake_body_coordinates = [[10,2], [10, 3], [10, 4]]

    while True:
        get_snake_direction_from_user(direction=direction)
        move_snake(snake_body_coordinates=snake_body_coordinates, direction=direction[-1])
        display_grid(grid=grid, snake_body_coordinates=snake_body_coordinates)
        print("outside:", direction)
