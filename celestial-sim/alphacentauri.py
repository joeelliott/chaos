import sys
import math
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, K_SPACE

pygame.init()

# Screen
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
CENTER_X, CENTER_Y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Settings
FPS = 60
TIME_STEP = 1
SPEED_UP_FACTOR = 10
speed_up = False

# Bodies
class CelestialBody:
    def __init__(self, name, radius, distance, color):
        self.name = name
        self.radius = radius
        self.distance = distance
        self.color = color
        self.angle = 0
        self.orbit_speed = 2 * math.pi / (100 * self.distance + 1)

    def update(self):
        self.angle += self.orbit_speed * (SPEED_UP_FACTOR if speed_up else 1)
        self.angle %= 2 * math.pi

    def draw(self, surface):
        x = CENTER_X + math.cos(self.angle) * self.distance
        y = CENTER_Y + math.sin(self.angle) * self.distance
        pygame.draw.circle(surface, self.color, (int(x), int(y)), self.radius)

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Alpha Centauri System Simulation')
clock = pygame.time.Clock()

# Create celestial bodies
bodies = [
    # CelestialBody('self.name', radius, distance, color, angle0, speed),
    CelestialBody('Alpha Centauri A', 20, 100, YELLOW),
    CelestialBody('Alpha Centauri B', 15, 200, WHITE),
    CelestialBody('Proxima Centauri', 5, 1000, RED),
    # CelestialBody('Alpha Centauri B', 15, 200, RED),
]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_SPACE:
                speed_up = not speed_up

    # Update celestial bodies
    for body in bodies:
        body.update()

    # Draw everything
    screen.fill(BLACK)
    for body in bodies:
        body.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
