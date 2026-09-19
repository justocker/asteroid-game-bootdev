import pygame
import sys
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import *
from logger import *
from player import Player
from circleshape import CircleShape
from shot import Shot


def main():
    pygame.init()

    shots = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group() # for the asteroids
    updatable = pygame.sprite.Group() # this will hold all the objects that can be updated
    drawable = pygame.sprite.Group() # this will hold all the objects that can be drawn

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (drawable, updatable, shots)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt: float = 0.0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    AsteroidField()

    

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        
        for ast in asteroids:
            if ast.collides_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for shot in shots:
                if ast.collides_with(shot):
                    log_event("asteroid_shot")
                    ast.kill()
                    shot.kill()

        for draws in drawable:
            draws.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

        
        


if __name__ == "__main__":
    main()
 



