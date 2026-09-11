from logger import log_event
from constants import ASTEROID_MIN_RADIUS
import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float,) -> None:
        super().__init__(x, y, radius)
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        t = random.uniform(20, 50)
        first_vector = self.velocity.rotate(t)
        second_vector = self.velocity.rotate(-t)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_new_asteroid.velocity = first_vector * 1.2
        second_new_asteroid.velocity = second_vector * 1.2
