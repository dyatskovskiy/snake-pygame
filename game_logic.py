from random import randrange

import config
from models import Point, Direction


def move_snake(snake_segments: list[Point], dir_: Direction):
    current_snake = snake_segments.copy()
    head = current_snake[0]

    match dir_:
        case Direction.LEFT:
            current_snake.insert(0, Point(head.x - 1, head.y))
        case Direction.RIGHT:
            current_snake.insert(0, Point(head.x + 1, head.y))
        case Direction.UP:
            current_snake.insert(0, Point(head.x, head.y - 1))
        case Direction.DOWN:
            current_snake.insert(0, Point(head.x, head.y + 1))

    return current_snake


def place_food(snake: list[Point]):
    food_point = (Point(randrange(config.GRID_WIDTH), randrange(config.GRID_HEIGHT)))

    while food_point in snake:
        food_point = (Point(randrange(config.GRID_WIDTH), randrange(config.GRID_HEIGHT)))

    return food_point


def is_food_collision(head: Point, food: Point):
    return head == food


def is_wall_collision(head: Point, field_w: int, field_h: int):
    # horizontal collision
    if head.x < 0 or head.x >= field_w:
        return True
    # vertical collision
    if head.y < 0 or head.y >= field_h:
        return True

    return False


def is_self_collision(snake: list[Point]):
    head, *body = snake
    return head in body


def init_game():
    score = 0
    snake = [
        Point(2, 0),
        Point(1, 0),
        Point(0, 0)
    ]
    food = place_food(snake)
    current_direction = Direction.RIGHT
    game_over = False

    return score, snake, food, current_direction, game_over
