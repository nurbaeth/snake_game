import pytest
from snake import Snake

def test_initial_snake_length():
    snake = Snake()
    assert len(snake.body) == 3  # Assuming initial length is 3

def test_snake_movement():
    snake = Snake()
    initial_head = snake.body[0]
    snake.change_direction("RIGHT")
    snake.move()
    assert snake.body[0] != initial_head  # Head position should change

def test_snake_growth():
    snake = Snake()
    initial_length = len(snake.body)
    snake.grow()
    assert len(snake.body) == initial_length + 1

def test_snake_collision_with_self():
    snake = Snake()
    snake.body = [(5, 5), (5, 6), (5, 7), (5, 8)]  # Example position
    snake.change_direction("UP")
    snake.move()
    assert snake.check_collision() is True
