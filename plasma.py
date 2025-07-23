import pygame
import math
import sys

# Configuration
WIDTH, HEIGHT = 600, 12     # Simulated LED grid
PIXEL_SIZE = 2            # Size of each block
FPS = 15                   # Frames per second (similar to delay(100))

PI = math.pi

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH * PIXEL_SIZE, HEIGHT * PIXEL_SIZE))
pygame.display.set_caption("Plasma Effect")

clock = pygame.time.Clock()

def plasma_frame(secs):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Coordinates for wavy plasma movement
            dx = x + 0.5 * math.sin(secs / 5.0)
            dy = y + 0.5 * math.cos(secs / 3.0)

            # Plasma calculation: three waves
            dv = (
                math.sin(x * 0.2 + secs) +
                math.sin(0.2 * (x * math.sin(secs / 2.0) + y * math.cos(secs / 3.0)) + secs) +
                math.sin(math.sqrt(0.3 * (dx * dx + dy * dy) + 1) + secs)
            )

            # Convert dv to color
            r = int(255 * abs(math.sin(dv * PI)))
            g = int(255 * abs(math.sin(dv * PI + 2 * PI / 3)))
            b = int(255 * abs(math.sin(dv * PI + 4 * PI / 3)))

            # Draw rectangle as simulated LED
            pygame.draw.rect(
                screen,
                (r, g, b),
                (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)
            )

def main():
    secs = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))  # Clear screen
        plasma_frame(secs)
        pygame.display.flip()
        secs += 1
        clock.tick(FPS)

if __name__ == "__main__":
    main()
