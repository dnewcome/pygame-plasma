import pygame
import sys
import time
from comet import Comet  # your comet.py file
# or: from your_module.comet import Comet

# Configuration
NUM_PIXELS = 60
PIXEL_SIZE = 12
FPS = 30

# Init
pygame.init()
screen = pygame.display.set_mode((NUM_PIXELS * PIXEL_SIZE, PIXEL_SIZE))
pygame.display.set_caption("Comet Animation")

clock = pygame.time.Clock()
comet = Comet(NUM_PIXELS, tail_length=10, color=(255, 50, 50))
comet.reset()

def draw_frame(frame_bytes):
    screen.fill((0, 0, 0))
    for i in range(NUM_PIXELS):
        r = frame_bytes[i * 3]
        g = frame_bytes[i * 3 + 1]
        b = frame_bytes[i * 3 + 2]
        pygame.draw.rect(
            screen,
            (r, g, b),
            (i * PIXEL_SIZE, 0, PIXEL_SIZE, PIXEL_SIZE)
        )
    pygame.display.flip()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    frame = comet.get_next()
    draw_frame(frame)
    clock.tick(FPS)
