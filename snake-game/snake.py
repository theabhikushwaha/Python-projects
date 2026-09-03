"""
Snake Game
A basic Nokia-style Snake game built with pygame.

Controls:
    Arrow keys / WASD - move
    P                 - pause
    R                 - restart after game over
    Esc / Q           - quit
"""

import pygame
import random
import sys

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS = 10  # snake "speed" - higher = faster

# Colors
BLACK = (15, 15, 15)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 140, 0)
RED = (220, 40, 40)
WHITE = (240, 240, 240)
GRAY = (60, 60, 60)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("consolas", 24)
        self.big_font = pygame.font.SysFont("consolas", 40, bold=True)
        self.reset()

    def reset(self):
        start_x, start_y = GRID_WIDTH // 2, GRID_HEIGHT // 2
        self.snake = [(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)]
        self.direction = RIGHT
        self.next_direction = RIGHT
        self.food = self.spawn_food()
        self.score = 0
        self.game_over = False
        self.paused = False

    def spawn_food(self):
        while True:
            pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if pos not in self.snake:
                return pos

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_q):
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_p and not self.game_over:
                    self.paused = not self.paused

                if event.key == pygame.K_r and self.game_over:
                    self.reset()

                if not self.paused and not self.game_over:
                    if event.key in (pygame.K_UP, pygame.K_w) and self.direction != DOWN:
                        self.next_direction = UP
                    elif event.key in (pygame.K_DOWN, pygame.K_s) and self.direction != UP:
                        self.next_direction = DOWN
                    elif event.key in (pygame.K_LEFT, pygame.K_a) and self.direction != RIGHT:
                        self.next_direction = LEFT
                    elif event.key in (pygame.K_RIGHT, pygame.K_d) and self.direction != LEFT:
                        self.next_direction = RIGHT

    def update(self):
        if self.game_over or self.paused:
            return

        self.direction = self.next_direction
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        # Wall collision
        if not (0 <= new_head[0] < GRID_WIDTH) or not (0 <= new_head[1] < GRID_HEIGHT):
            self.game_over = True
            return

        # Self collision
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self.spawn_food()
        else:
            self.snake.pop()

    def draw_grid(self):
        for x in range(0, SCREEN_WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, GRAY, (0, y), (SCREEN_WIDTH, y))

    def draw(self):
        self.screen.fill(BLACK)

        for i, (x, y) in enumerate(self.snake):
            color = GREEN if i > 0 else DARK_GREEN
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, color, rect)

        fx, fy = self.food
        food_rect = pygame.Rect(fx * CELL_SIZE, fy * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.screen, RED, food_rect)

        score_surf = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_surf, (10, 10))

        if self.paused and not self.game_over:
            self._center_text("PAUSED", self.big_font)

        if self.game_over:
            self._center_text("GAME OVER", self.big_font, y_offset=-20)
            sub = self.font.render("Press R to restart or Q to quit", True, WHITE)
            rect = sub.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25))
            self.screen.blit(sub, rect)

        pygame.display.flip()

    def _center_text(self, text, font, y_offset=0):
        surf = font.render(text, True, WHITE)
        rect = surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset))
        self.screen.blit(surf, rect)

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(FPS)


if __name__ == "__main__":
    SnakeGame().run()
