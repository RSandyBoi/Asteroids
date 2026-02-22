from circleshape import CircleShape
import pygame
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SHOOT_SPEED, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS
from shot import Shot
class Player(CircleShape):
    def __init__(self, x, y,):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # in degrees
        self.cooldown_timer = 0
    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen): #draw player as triangle with white lines
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt): #rotator method to change rotation based on turn speed and delta time
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt): #basic control mapping for player movement
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt): #move method to update position based on rotation and speed
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    
    def shoot(self):
        if self.cooldown_timer > 0:
            return
        else:
            self.cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED