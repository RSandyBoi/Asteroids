from constants import LINE_WIDTH
from circleshape import CircleShape
import pygame
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), self.radius, LINE_WIDTH)
    def update(self, dt):
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt