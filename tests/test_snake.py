import unittest
import sys
from snake_game import snake


class TestSnakeGame(unittest.TestCase):
    def setUp(self):
        self.grid_size = 20
        self.snake_body_coordinates_w_s = [
            [4, 4],
            [4, 5],
            [4, 6]
        ]
        self.snake_body_coordinates_a_d = [
            [4, 4],
            [5, 4],
            [6, 4]
        ]
        self.snake_body_coordinates_with_collission = [
            [4, 4],
            [5, 4],
            [6, 4],
            [5, 4]
        ]

    def test_initialize_grid(self):
        grid = snake.initialize_grid(size=self.grid_size)
        self.assertEqual(len(grid), self.grid_size)
        self.assertEqual(len(grid[0]), self.grid_size)

    def test_initialize_snake_position_and_direction(self):
        position = snake.initialize_snake_position_and_direction(self.grid_size)
        self.assertIsInstance(position, list)
        self.assertEqual(len(position), 2)
        self.assertGreaterEqual(position[0], 1)
        self.assertLessEqual(position[1], self.grid_size-2)

    def test_valid_move_w_pressed(self):
        output = snake.valid_move(direction='s', new_direction='w')
        output2 = snake.valid_move(direction='a', new_direction='w')
        output3 = snake.valid_move(direction='d', new_direction='w')
        output4 = snake.valid_move(direction='w', new_direction='w')
        self.assertFalse(output)
        self.assertTrue(output2)
        self.assertTrue(output3)
        self.assertTrue(output4)

    def test_valid_move_s_pressed(self):
        output = snake.valid_move(direction='w', new_direction='s')
        output2 = snake.valid_move(direction='a', new_direction='s')
        output3 = snake.valid_move(direction='d', new_direction='s')
        output4 = snake.valid_move(direction='s', new_direction='s')
        self.assertFalse(output)
        self.assertTrue(output2)
        self.assertTrue(output3)
        self.assertTrue(output4)

    def test_valid_move_a_pressed(self):
        output = snake.valid_move(direction='d', new_direction='a')
        output2 = snake.valid_move(direction='a', new_direction='a')
        output3 = snake.valid_move(direction='w', new_direction='a')
        output4 = snake.valid_move(direction='s', new_direction='a')
        self.assertFalse(output)
        self.assertTrue(output2)
        self.assertTrue(output3)
        self.assertTrue(output4)

    def test_valid_move_d_pressed(self):
        output = snake.valid_move(direction='a', new_direction='d')
        output2 = snake.valid_move(direction='d', new_direction='d')
        output3 = snake.valid_move(direction='w', new_direction='d')
        output4 = snake.valid_move(direction='s', new_direction='d')
        self.assertFalse(output)
        self.assertTrue(output2)
        self.assertTrue(output3)
        self.assertTrue(output4)

    def test_move_snake_w_direction(self):
        snake.move_snake(self.snake_body_coordinates_w_s, 'w')
        self.assertEqual(len(self.snake_body_coordinates_w_s), 3)
        self.assertNotEqual(self.snake_body_coordinates_w_s[0], [4, 4])
        self.assertEqual(self.snake_body_coordinates_w_s[0], [4, 5])
        self.assertEqual(self.snake_body_coordinates_w_s[-1], [3, 6])

    def test_move_snake_s_direction(self):
        snake.move_snake(self.snake_body_coordinates_w_s, 's')
        self.assertEqual(len(self.snake_body_coordinates_w_s), 3)
        self.assertNotEqual(self.snake_body_coordinates_w_s[0], [4, 4])
        self.assertEqual(self.snake_body_coordinates_w_s[0], [4, 5])
        self.assertEqual(self.snake_body_coordinates_w_s[-1], [5, 6])

    def test_move_snake_a_direction(self):
        snake.move_snake(self.snake_body_coordinates_a_d, 'a')
        self.assertEqual(len(self.snake_body_coordinates_a_d), 3)
        self.assertNotEqual(self.snake_body_coordinates_a_d[0], [4, 4])
        self.assertEqual(self.snake_body_coordinates_a_d[0], [5, 4])
        self.assertEqual(self.snake_body_coordinates_a_d[-1], [6, 3])

    def test_move_snake_d_direction(self):
        snake.move_snake(self.snake_body_coordinates_a_d, 'd')
        self.assertEqual(len(self.snake_body_coordinates_a_d), 3)
        self.assertNotEqual(self.snake_body_coordinates_a_d[0], [4, 4])
        self.assertEqual(self.snake_body_coordinates_a_d[0], [5, 4])
        self.assertEqual(self.snake_body_coordinates_a_d[-1], [6, 5])

    def test_food_spawn(self):
        for _ in range(1000):
            food_coordinate = []
            food_coordinate = snake.food_spawn(
                grid_size=self.grid_size, 
                snake_body_coordinates=self.snake_body_coordinates_a_d, 
                food_coordinate=food_coordinate
            )
            self.assertIsInstance(food_coordinate, list)
            self.assertEqual(len(food_coordinate), 2)
            self.assertNotIn(food_coordinate, self.snake_body_coordinates_a_d)

    def test_food_collision_with_collision(self):
        food_coordinate = [6, 4]
        snake_length = len(self.snake_body_coordinates_a_d)
        food_coordinate = snake.food_collision(
            snake_body_coordinates=self.snake_body_coordinates_a_d,
            food_coordinate=food_coordinate
        )
        self.assertEqual(len(self.snake_body_coordinates_a_d), snake_length+1)
        self.assertEqual(food_coordinate, [])

    def test_food_collision_without_collision(self):
        food_coordinate = [6, 6]
        snake_length = len(self.snake_body_coordinates_a_d)
        food_coordinate = snake.food_collision(
            snake_body_coordinates=self.snake_body_coordinates_a_d,
            food_coordinate=food_coordinate
        )
        self.assertNotEqual(len(self.snake_body_coordinates_a_d), snake_length+1)
        self.assertEqual(len(self.snake_body_coordinates_a_d), snake_length)
        self.assertEqual(food_coordinate, [6, 6])

    def check_loss_without_lose_condition(self):
        status = snake.check_loss(self.snake_body_coordinates_a_d)
        self.assertFalse(status)

    def check_loss_with_lose_condition(self):
        status = snake.check_loss(self.snake_body_coordinates_a_d)
        self.assertTrue(status)

    def test_display_grid(self):
        sys.stdout = open("tests/display_grid.txt", "w")
        grid = snake.initialize_grid(size=4, background="1")
        snake_body_coordinates = [[0,0], [0,1], [0,2]]
        snake.display_grid(
            grid=grid, 
            snake_body_coordinates=snake_body_coordinates,
            food_coordinate=[0,3],
            collision=False,
            snake="0",
            background="1",
            food="#"
        )
        snake.display_grid(
            grid=grid, 
            snake_body_coordinates=snake_body_coordinates,
            food_coordinate=[0,3],
            collision=True,
            snake="0",
            background="1",
            food="#"
        )
        sys.stdout.close()

        with open("tests/display_grid.txt", "r") as f:
            self.assertEqual(f.read(), "Score: 0\n000#\n1111\n1111\n1111\n\nSorry, you lost!\n")
