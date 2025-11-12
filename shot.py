from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x, y, SHOT_RADIUS)

        diameter = SHOT_RADIUS * 2
        self.image = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        pygame.draw.circle(self.image, ("white"), (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position  # Update rect position to match the new position
