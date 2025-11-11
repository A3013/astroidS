from circleshape import CircleShape
import pygame
from constants import *

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
