import pygame
import sys
import work
import random

# Initialize Pygame
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PC")
pygame.display.set_icon(work.icon)

# Load assets
background = pygame.image.load("bash/textures/background.png").convert_alpha()
enemy_hit_1 = pygame.image.load("bash/textures/enemy_1.png").convert_alpha()
enemy_hit_2 = pygame.image.load("bash/textures/enemy_2.png").convert_alpha()
player_1 = pygame.image.load("bash/textures/player_walk_1.png").convert_alpha()
player_2 = pygame.image.load("bash/textures/player_walk_1.png").convert_alpha()

# Enemy setup
enemy_x = 800
enemy_speed = random.randint(1, 3)

# Load and play music
pygame.mixer.music.load("bash/sounds/music.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.load("bash/sounds/attack.wav")

# Create clock for FPS control
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Update enemy position
    enemy_x -= enemy_speed
    if enemy_x < 600:
        enemy_x = 600

    # Draw game objects
    window.blit(background, (0, 0))
    y = (300, 350, 400, 450, 500)
    window.blit(enemy_hit_1, (enemy_x, 300));window.blit(enemy_hit_1, (enemy_x, 350));window.blit(enemy_hit_1, (enemy_x, 400));window.blit(enemy_hit_1, (enemy_x, 450));window.blit(enemy_hit_1, (enemy_x, 500))
    
    # Update display
    pygame.display.update()

    # Control FPS
    clock.tick(60)