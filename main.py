import pygame
import random

pygame.init()
square_width = 620
pixel_width = 25
screen = pygame.display.set_mode([square_width] * 2)
clock = pygame.time.Clock()
running = True


def generate_starting_position():
    position_range = (pixel_width // 2, square_width - pixel_width // 2, pixel_width)
    return [random.randrange(*position_range), random.randrange(*position_range)]


snake_pixel = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
snake_pixel.center = generate_starting_position()
snake = [snake_pixel.copy()]
snake_direction = (0, 0)
snake_length = 3

target = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
target.center = generate_starting_position()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # Collide Events
    if snake_pixel.colliderect(target):
        target.center = generate_starting_position()
        snake_length += 1
        snake.append(snake_pixel.copy())

    # Key Press Event
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if snake_direction != (0, pixel_width):
            snake_direction = (0, -pixel_width)
    if keys[pygame.K_s]:
        if snake_direction != (0, -pixel_width):
            snake_direction = (0, pixel_width)
    if keys[pygame.K_a]:
        if snake_direction != (pixel_width, 0):
            snake_direction = (-pixel_width, 0)
    if keys[pygame.K_d]:
        if snake_direction != (-pixel_width, 0):
            snake_direction = (pixel_width, 0)

    for snake_part in snake:
        pygame.draw.rect(screen, "green", snake_part)

    pygame.draw.rect(screen, "red", target)

    snake_pixel.move_ip(snake_direction)
    snake.append(snake_pixel.copy())
    snake = snake[-snake_length:]

    pygame.display.flip()

    clock.tick(10)

pygame.quit()