import pygame

import color_palette
import config
import game_logic
import renderer
from input import KEY_TO_DIRECTION, is_movement_allowed
from models import Direction

pygame.init()
pygame.display.set_caption('Snake')

fonts = {
    'sm': pygame.font.Font(None, 48),
    'md': pygame.font.Font(None, 56),
    'lg': pygame.font.Font(None, 72),
}

screen = pygame.display.set_mode(config.SCREEN_SIZE)
clock = pygame.time.Clock()


def main():
    score, snake, food, current_direction, game_over = game_logic.init_game()

    start_game_btn = None
    running = True

    while running:
        # prevent instant snake reversal within the same tick
        direction_changed = False

        # process user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and game_over:
                if start_game_btn.collidepoint(event.pos):
                    score, snake, food, current_direction, game_over = game_logic.init_game()
                    break

            if not game_over and event.type == pygame.KEYDOWN:
                new_direction: Direction | None = KEY_TO_DIRECTION.get(event.key)

                if (
                        not direction_changed
                        and new_direction is not None
                        and is_movement_allowed(current_direction, new_direction)
                ):
                    current_direction = new_direction
                    direction_changed = True

        # update
        new_snake = game_logic.move_snake(snake, current_direction)
        grow = game_logic.is_food_collision(new_snake[0], food)

        if not game_over:
            if grow:
                score += 1
                food = game_logic.place_food(new_snake)
            else:
                new_snake.pop()
            snake = new_snake

        wall_hit = game_logic.is_wall_collision(snake[0], config.GRID_WIDTH, config.GRID_HEIGHT)
        self_hit = game_logic.is_self_collision(snake)
        game_over = wall_hit or self_hit

        # draw
        screen.fill(color_palette.BG_COLOR)

        if game_over:
            renderer.draw_game_over_screen(screen, fonts, score)
            start_game_btn = renderer.draw_start_new_game_btn(screen, fonts)
        else:
            renderer.draw_food(screen, food)
            renderer.draw_snake(screen, snake)

        pygame.display.flip()
        clock.tick(12)


if __name__ == '__main__':
    main()
