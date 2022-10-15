import unittest
import sys
from snake_game import snake


class TestSnakeGame(unittest.TestCase):
    def setUp(self):
        self.grid_size = 20

    def test_initialize_grid(self):
        grid = snake.initialize_grid(size=self.grid_size)
        self.assertEqual(len(grid), self.grid_size)
        self.assertEqual(len(grid[0]), self.grid_size)

    def test_valid_move_w_pressed(self):
        output = snake.valid_move(direction='a', new_direction='w')
        output2 = snake.valid_move(direction='d', new_direction='w')
        output3 = snake.valid_move(direction='w', new_direction='w')
        output4 = snake.valid_move(direction='s', new_direction='w')
        self.assertTrue(output)
        self.assertTrue(output2)
        self.assertFalse(output3)
        self.assertFalse(output4)

    def test_valid_move_s_pressed(self):
        output = snake.valid_move(direction='a', new_direction='s')
        output2 = snake.valid_move(direction='d', new_direction='s')
        output3 = snake.valid_move(direction='w', new_direction='s')
        output4 = snake.valid_move(direction='s', new_direction='s')
        self.assertTrue(output)
        self.assertTrue(output2)
        self.assertFalse(output3)
        self.assertFalse(output4)

    def test_valid_move_a_pressed(self):
        output = snake.valid_move(direction='a', new_direction='a')
        output2 = snake.valid_move(direction='d', new_direction='a')
        output3 = snake.valid_move(direction='w', new_direction='a')
        output4 = snake.valid_move(direction='s', new_direction='a')
        self.assertFalse(output)
        self.assertFalse(output2)
        self.assertTrue(output3)
        self.assertTrue(output4)

    def test_valid_move_d_pressed(self):
        output = snake.valid_move(direction='a', new_direction='d')
        output2 = snake.valid_move(direction='d', new_direction='d')
        output3 = snake.valid_move(direction='w', new_direction='d')
        output4 = snake.valid_move(direction='s', new_direction='d')
        self.assertFalse(output)
        self.assertFalse(output2)
        self.assertTrue(output3)
        self.assertTrue(output4)

    def test_initialize_snake_position_and_direction(self):
        position = snake.initialize_snake_position_and_direction(self.grid_size)
        self.assertIsInstance(position, list)
        self.assertEqual(len(position), 2)
        self.assertGreaterEqual(position[0], 1)
        self.assertLessEqual(position[1], self.grid_size-2)

    def test_display_grid(self):
        sys.stdout = open("tests/display_grid.txt", "w")
        grid = snake.initialize_grid(size=4, background="1")
        snake_body_coordinates = [[0,0], [0,1], [0,2]]
        snake.display_grid(
            grid=grid, 
            snake_body_coordinates=snake_body_coordinates,
            snake="0",
            background="1"
        )
        sys.stdout.close()

        with open("tests/display_grid.txt", "r") as f:
            self.assertEqual(f.read(), "0001\n1111\n1111\n1111\n")
