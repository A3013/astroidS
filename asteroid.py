from circleshape import CircleShape
import pygame
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        diameter = radius * 2
        self.image = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        pygame.draw.circle(self.image, (255, 0, 0), (radius, radius), radius)

    def draw(self, screen):
        pygame.draw.circle(screen, ("white"), self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position  # Update rect position to match the new position
    
    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = pygame.Vector2(-self.velocity.y, self.velocity.x).rotate(angle) * 1.2
            asteroid2.velocity = pygame.Vector2(self.velocity.y, -self.velocity.x).rotate(-angle) * 1.2
            return [asteroid1, asteroid2]
        else:
            return []
