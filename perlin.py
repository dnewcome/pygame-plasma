import pygame
import time
import math
import colorsys
from noise import pnoise3  # Perlin noise (3D)

# Display config
NUM_COLS, NUM_ROWS = 600, 12 
PIXEL_SIZE = 5 
BRIGHTNESS = 255
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((NUM_COLS * PIXEL_SIZE, NUM_ROWS * PIXEL_SIZE))
pygame.display.set_caption("Perlin Plasma")
clock = pygame.time.Clock()

def xy(x, y):
    return y * NUM_COLS + x

def perlin_plasma():
    t_start = time.time()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Time-based Z axis for 3D noise
        ms = int((time.time() - t_start) * 1000)

        for i in range(NUM_COLS):
            for j in range(NUM_ROWS):
                # Scale X/Y for nice wave texture
                x_noise = i * 0.1
                y_noise = j * 0.1
                z_noise = ms / 4000.0  # slow evolving Z

                # Perlin noise returns -1..1; normalize to 0..1
                noise_val = pnoise3(x_noise, y_noise, z_noise)
                index = int((noise_val + 1) * 127.5)  # 0..255

                # Cycle hue over time
                hue = ((index + ms / 200) % 255) / 255.0
                rgb = colorsys.hsv_to_rgb(hue, 1.0, BRIGHTNESS / 255.0)
                rgb_scaled = tuple(int(c * 255) for c in rgb)

                pygame.draw.rect(
                    screen,
                    rgb_scaled,
                    (i * PIXEL_SIZE, j * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)
                )

        pygame.display.flip()
        clock.tick(FPS)

perlin_plasma()
