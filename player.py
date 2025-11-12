import pygame
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED
from shot import Shot
from circleshape import CircleShape

class Player(CircleShape): 
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # in degrees
        diameter = PLAYER_RADIUS * 2
        self.image = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        center = (diameter // 2, diameter // 2)
        pygame.draw.polygon(self.image, (0, 255, 0), [center + pygame.Vector2(0, -PLAYER_RADIUS), center + pygame.Vector2(-PLAYER_RADIUS, PLAYER_RADIUS), center + pygame.Vector2(PLAYER_RADIUS, PLAYER_RADIUS)], 0)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, ("white"), self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        return self.rotation
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # Rotate left
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # Rotate right
            self.rotate(dt)
        if keys[pygame.K_w]:
            # Move forward
            self.move(dt)
        if keys[pygame.K_s]:
            # Move backward
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            # Shoot
            shot = self.shoot()
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
        self.rect.center = self.position  # Update rect position to match the new position

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot_direction = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = shot_direction * PLAYER_SHOOT_SPEED
        return shot