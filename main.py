import random
from collections import namedtuple
from enum import Enum

import pygame

import styles

Point = namedtuple('Point', ['x', 'y'])
Size = namedtuple('Size', ['width', 'height'])


class Direction(Enum):
    LEFT = 'l'
    RIGHT = 'r'
    UP = 'u'
    DOWN = 'd'


KEY_TO_DIRECTION = {
    pygame.K_LEFT: Direction.LEFT,
    pygame.K_RIGHT: Direction.RIGHT,
    pygame.K_UP: Direction.UP,
    pygame.K_DOWN: Direction.DOWN
}

screen_size = Size(800, 800)

pygame.init()
pygame.display.set_caption('Snake')

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

CELL_SIZE = 20
GRID_WIDTH: int = screen_size.width // CELL_SIZE
GRID_HEIGHT: int = screen_size.height // CELL_SIZE


def is_food_collision(head: Point, food: Point):
    return head == food


def place_food(snake: list[Point]):
    food_point = (Point(random.randrange(GRID_WIDTH), random.randrange(GRID_HEIGHT)))

    while food_point in snake:
        food_point = (Point(random.randrange(GRID_WIDTH), random.randrange(GRID_HEIGHT)))

    return food_point


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


def is_allowed(current_direction: Direction, new_direction: Direction):
    if current_direction == Direction.RIGHT and new_direction == Direction.LEFT:
        return False
    if current_direction == Direction.LEFT and new_direction == Direction.RIGHT:
        return False
    if current_direction == Direction.UP and new_direction == Direction.DOWN:
        return False
    if current_direction == Direction.DOWN and new_direction == Direction.UP:
        return False

    return True


def main():
    score = 0
    snake = [
        Point(2, 0),
        Point(1, 0),
        Point(0, 0)
    ]
    food = place_food(snake)
    current_direction = Direction.RIGHT

    running = True

    while running:
        # process user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                new_direction: Direction | None = KEY_TO_DIRECTION.get(event.key)

                if new_direction is not None and is_allowed(current_direction, new_direction):
                    current_direction = new_direction

        # update
        new_snake = move_snake(snake, current_direction)
        grow = is_food_collision(new_snake[0], food)

        if grow:
            score += 1
            food = place_food(new_snake)
        else:
            new_snake.pop()
        snake = new_snake

        # draw
        screen.fill(styles.BG_COLOR)

        food_rect = pygame.Rect([point * CELL_SIZE for point in food], (CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, styles.FOOD_COLOR, food_rect, border_radius=6)

        for seg in snake:
            seg_rect = pygame.Rect([point * CELL_SIZE for point in seg], (CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, styles.SNAKE_COLOR, seg_rect, border_radius=4)

        pygame.display.flip()

        clock.tick(15)


if __name__ == '__main__':
    main()
