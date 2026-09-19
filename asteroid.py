from circleshape import CircleShape
from logger import log_event
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        


    def update(self, dt):
        self.position += (self.velocity * dt)


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: #small asteroid --> disappears
            return
        log_event("asteroid_split")
        degree = random.uniform(20, 50)
        firstAV = self.velocity.rotate(degree)
        secondAV = self.velocity.rotate(-degree)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        firstA = Asteroid(self.position.x, self.position.y, new_radius)
        secondA = Asteroid(self.position.x, self.position.y, new_radius)

        firstA.velocity = firstAV * 1.2
        secondA.velocity = secondAV * 1.2





    
