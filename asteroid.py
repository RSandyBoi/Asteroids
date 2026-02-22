from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event
import random
import pygame
class Asteroid(CircleShape):
    def __init__(self, x, y, radius): #inherit from CircleShape
        super().__init__(x, y, radius)

    def draw(self, screen): #draw the Asteroid override
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt): #update position override
        self.position += self.velocity * dt
    
    def split(self): #split asteroid upon collision with shot, spawn 2 more asteroids at random angles and faster velocity upon collision if not smallest size, delete source asteroid
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            vector1 = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(-angle)
            newrad = self.radius - ASTEROID_MIN_RADIUS
            newAsteroid1 = Asteroid(self.position.x, self.position.y, newrad)
            newAsteroid2 = Asteroid(self.position.x, self.position.y, newrad)
            newAsteroid1.velocity = vector1 * 1.2
            newAsteroid2.velocity = vector2 * 1.2



        