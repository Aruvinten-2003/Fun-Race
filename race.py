import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Car Racing")

# Colors
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (200, 0, 0)

# Clock
clock = pygame.time.Clock()

# Load car image
car_width, car_height = 50, 90
player_car = pygame.Surface((car_width, car_height))
player_car.fill(RED)

# Car starting position
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 20
car_speed = 5

# Obstacles
obstacle_width, obstacle_height = 50, 90
obstacles = []
obstacle_speed = 5
spawn_delay = 40
frame_count = 0

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    clock.tick(60)  # 60 FPS
    screen.fill(GRAY)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed

    # Spawn obstacles
    frame_count += 1
    if frame_count >= spawn_delay:
        frame_count = 0
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        obstacles.append([obstacle_x, -obstacle_height])

    # Move obstacles
    for obs in obstacles:
        obs[1] += obstacle_speed
        if obs[1] > HEIGHT:
            obstacles.remove(obs)
            score += 1  # increase score when an obstacle passes

    # Collision detection
    player_rect = pygame.Rect(car_x, car_y, car_width, car_height)
    for obs in obstacles:
        obs_rect = pygame.Rect(obs[0], obs[1], obstacle_width, obstacle_height)
        if player_rect.colliderect(obs_rect):
            print("Game Over! Final Score:", score)
            pygame.quit()
            sys.exit()

    # Draw car
    screen.blit(player_car, (car_x, car_y))

    # Draw obstacles
    for obs in obstacles:
        pygame.draw.rect(screen, WHITE, (obs[0], obs[1], obstacle_width, obstacle_height))

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
