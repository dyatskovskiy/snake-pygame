import pygame

from models import Direction

KEY_TO_DIRECTION = {
    pygame.K_LEFT: Direction.LEFT,
    pygame.K_RIGHT: Direction.RIGHT,
    pygame.K_UP: Direction.UP,
    pygame.K_DOWN: Direction.DOWN
}


def is_movement_allowed(current_direction: Direction, new_direction: Direction):
    if current_direction == Direction.RIGHT and new_direction == Direction.LEFT:
        return False
    if current_direction == Direction.LEFT and new_direction == Direction.RIGHT:
        return False
    if current_direction == Direction.UP and new_direction == Direction.DOWN:
        return False
    if current_direction == Direction.DOWN and new_direction == Direction.UP:
        return False
    return True
