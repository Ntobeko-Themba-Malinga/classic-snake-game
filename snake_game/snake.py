import os
import time
import random
import keyboard


def initialize_grid(size, background="⬛"):
    grid = []
    for _ in range(size):
        grid.append(list(background*size))
    return grid


def initialize_snake_position_and_direction(grid_size):
    random_position = [random.randint(1, grid_size-2), random.randint(1, grid_size-2)]
    return random_position


def valid_move(direction, new_direction):
    if new_direction == 'w' and direction != 's':
        return True
    
    if new_direction == 's' and direction != 'w':
        return True

    if new_direction == 'a' and direction != 'd':
        return True

    if new_direction == 'd' and direction != 'a':
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
        if valid_move(direction=direction[0], new_direction='w'):
            direction[0] = 'w'

    if keyboard.is_pressed('s'):
        if valid_move(direction=direction[0], new_direction='s'):
            direction[0] = 's'

    if keyboard.is_pressed('a'):
        if valid_move(direction=direction[0], new_direction='a'):
            direction[0] = 'a'

    if keyboard.is_pressed('d'):
        if valid_move(direction=direction[0], new_direction='d'):
            direction[0] = 'd'
            
    if keyboard.is_pressed('q'):
        quit()


def food_spawn(grid_size, snake_body_coordinates, food_coordinate):
    if food_coordinate == []:
        food_coordinate = [random.randint(1, grid_size-2), random.randint(1, grid_size-2)]
        while food_coordinate in snake_body_coordinates:
            food_coordinate = [random.randint(1, grid_size-2), random.randint(1, grid_size-2)]
        return food_coordinate
    return food_coordinate


def food_collision(snake_body_coordinates, food_coordinate):
    if snake_body_coordinates[-1] == food_coordinate:
        food_coordinate = []
        added_snake_body = snake_body_coordinates[0]
        snake_body_coordinates.insert(0, added_snake_body)
    return food_coordinate


def check_loss(grid_size, snake_body_coordinates):
    copy_snake_body_coordinates = snake_body_coordinates[:]
    snake_head = copy_snake_body_coordinates.pop()
    if snake_head in copy_snake_body_coordinates:
        return True

    if snake_head[0] == -1 or snake_head[0] == grid_size or snake_head[1] == -1 or snake_head[1] == grid_size:
        return True
    return False


def display_grid(grid, snake_body_coordinates, food_coordinate, collision, snake="🟩", background="⬛", food="🟨"):
    if collision:
        print("Sorry, you lost!")
    else:
        os.system("cls")
        print(f"Score: {len(snake_body_coordinates)-3}")
        row = 0
        grid_display = ''
        while row < len(grid):
            column = 0
            while column < len(grid):
                if [row, column] in snake_body_coordinates:
                    grid_display += snake
                elif [row, column] == food_coordinate:
                    grid_display += food
                else:
                    grid_display += background
                column += 1
            row += 1
            grid_display += "\n"
        print(grid_display)


if __name__ == "__main__":
    grid_size = 20
    collision = False
    direction = ["s"]
    food = []
    grid = initialize_grid(size=grid_size)
    snake_body_coordinates = [[10,2], [10, 3], [10, 4]]

    while not collision:
        food = food_spawn(grid_size=grid_size, snake_body_coordinates=snake_body_coordinates, food_coordinate=food)
        get_snake_direction_from_user(direction=direction)
        move_snake(snake_body_coordinates=snake_body_coordinates, direction=direction[-1])
        food = food_collision(snake_body_coordinates=snake_body_coordinates, food_coordinate=food)
        collision = check_loss(grid_size, snake_body_coordinates=snake_body_coordinates)
        display_grid(
            grid=grid, 
            snake_body_coordinates=snake_body_coordinates, 
            food_coordinate=food,
            collision=collision
        )
        time.sleep(0.1)
