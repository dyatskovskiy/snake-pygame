import pygame

import color_palette
import config
from models import Point


def draw_game_over_screen(screen, fonts, score: int):
    game_over_surf = fonts['lg'].render('Game Over', True, 'White')
    game_over_rect = game_over_surf.get_rect()
    game_over_rect.top = config.SCREEN_SIZE.height // 2 - game_over_rect.height // 2
    game_over_rect.left = config.SCREEN_SIZE.width // 2 - game_over_rect.width // 2

    score_surf = fonts['sm'].render(f'Your score: {str(score)}', True, 'Red')
    score_rect = score_surf.get_rect()
    score_rect.top = config.SCREEN_SIZE.height // 2 - score_rect.height // 2 + 48
    score_rect.left = config.SCREEN_SIZE.width // 2 - score_rect.width // 2
    screen.blit(game_over_surf, game_over_rect)
    screen.blit(score_surf, score_rect)


def draw_start_new_game_btn(screen, fonts) -> pygame.Rect:
    start_game_surf = fonts['md'].render('Start New Game', True, 'Yellow')
    start_game_rect = start_game_surf.get_rect()
    start_game_rect.top = config.SCREEN_SIZE.height // 2 - start_game_rect.height // 2 + 48 + 56
    start_game_rect.left = config.SCREEN_SIZE.width // 2 - start_game_rect.width // 2
    screen.blit(start_game_surf, start_game_rect)

    return start_game_rect


def draw_food(screen, food: Point):
    food_rect = pygame.Rect([point * config.CELL_SIZE for point in food], (config.CELL_SIZE, config.CELL_SIZE))
    pygame.draw.rect(screen, color_palette.FOOD_COLOR, food_rect, border_radius=6)


def draw_snake(screen, snake: list[Point]):
    head, *body = snake
    for seg in snake:
        seg_rect = pygame.Rect([point * config.CELL_SIZE for point in seg],
                               (config.CELL_SIZE, config.CELL_SIZE))
        color = color_palette.SNAKE_HEAD_COLOR if seg == head else color_palette.SNAKE_BODY_COLOR
        pygame.draw.rect(screen, color, seg_rect, border_radius=4)
