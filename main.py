import random
from collections import namedtuple
from enum import Enum

import pygame

import color_palette

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

FONT_SIZE = 24
CELL_SIZE = 20
GRID_WIDTH: int = screen_size.width // CELL_SIZE
GRID_HEIGHT: int = screen_size.height // CELL_SIZE


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
    head = snake[0]
    body = snake[1:]

    if head in body:
        return True
    return False


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


def draw_game_over_screen(score: int):
    game_over_font = pygame.font.Font(None, 72)
    game_over_surf = game_over_font.render('Game Over', True, 'White')
    game_over_rect = game_over_surf.get_rect()
    game_over_rect.top = screen_size.height // 2 - game_over_rect.height // 2
    game_over_rect.left = screen_size.width // 2 - game_over_rect.width // 2
    score_font = pygame.font.Font(None, 48)
    score_surf = score_font.render(f'Your score: {str(score)}', True, 'Red')
    score_rect = score_surf.get_rect()
    score_rect.top = screen_size.height // 2 - score_rect.height // 2 + 48
    score_rect.left = screen_size.width // 2 - score_rect.width // 2
    screen.blit(game_over_surf, game_over_rect)
    screen.blit(score_surf, score_rect)


def draw_start_new_game_btn() -> pygame.Rect:
    font = pygame.font.Font(None, 56)
    start_game_surf = font.render('Start New Game', True, 'Yellow')
    start_game_rect = start_game_surf.get_rect()
    start_game_rect.top = screen_size.height // 2 - start_game_rect.height // 2 + 48 + 56
    start_game_rect.left = screen_size.width // 2 - start_game_rect.width // 2
    screen.blit(start_game_surf, start_game_rect)

    return start_game_rect


def start_new_game():
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


def main():
    score = 0
    snake = [
        Point(2, 0),
        Point(1, 0),
        Point(0, 0)
    ]
    food = place_food(snake)
    current_direction = Direction.RIGHT

    game_over = False
    start_game_btn = None
    running = True

    while running:
        # process user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and game_over:
                if start_game_btn.collidepoint(event.pos):
                    score, snake, food, current_direction, game_over = start_new_game()
                    break

            if not game_over and event.type == pygame.KEYDOWN:
                new_direction: Direction | None = KEY_TO_DIRECTION.get(event.key)

                if new_direction is not None and is_allowed(current_direction, new_direction):
                    current_direction = new_direction

        # update
        new_snake = move_snake(snake, current_direction)
        grow = is_food_collision(new_snake[0], food)

        if not game_over:
            if grow:
                score += 1
                food = place_food(new_snake)
            else:
                new_snake.pop()
            snake = new_snake

        wall_hit = is_wall_collision(snake[0], GRID_WIDTH, GRID_HEIGHT)
        self_hit = is_self_collision(snake)
        game_over = wall_hit or self_hit

        # draw
        screen.fill(color_palette.BG_COLOR)

        if game_over:
            draw_game_over_screen(score)
            start_game_btn = draw_start_new_game_btn()
        else:
            food_rect = pygame.Rect([point * CELL_SIZE for point in food], (CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, color_palette.FOOD_COLOR, food_rect, border_radius=6)

            for seg in snake:
                seg_rect = pygame.Rect([point * CELL_SIZE for point in seg], (CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(screen, color_palette.SNAKE_COLOR, seg_rect, border_radius=4)

        pygame.display.flip()

        clock.tick(15)


if __name__ == '__main__':
    main()
