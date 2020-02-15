import pygame
import sys
from collections import defaultdict

args = sys.argv[1:]
if not args:
    framerate = 10000
else:
    framerate = int(args[0])

print(f"Tick is {framerate}")

RECT_SIZE = 4

pygame.init()
clock = pygame.time.Clock()

# ant_directions
all_directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
current_direction = 2

# white == 0, black == 1
grid = defaultdict(int)

# window sizes
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
screen_x, screen_y = width / 2, height / 2

key = 0, 0
while True:
    # exit game?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if grid[key] == 0:
        current_direction = (current_direction + 1) % 4
    elif grid[key] == 1:
        current_direction = (current_direction + 3) % 4

    grid[key] = not grid[key]

    # let's translate our grid and draw
    screen.fill((255, 255, 255))

    for x, y in grid:
        if grid[(x, y)] == 0:
            continue

        left = screen_x + (x * RECT_SIZE)
        top = screen_y + (y * RECT_SIZE)

        rect = pygame.Rect(left, top, RECT_SIZE, RECT_SIZE)
        pygame.draw.rect(screen, pygame.Color((0, 0, 0)), rect)

    x, y = key
    new_x = x + all_directions[current_direction][0]
    new_y = y + all_directions[current_direction][1]

    key = new_x, new_y

    pygame.display.flip()

    clock.tick(framerate)
