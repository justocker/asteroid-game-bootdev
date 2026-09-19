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


    font = pygame.font.Font('freesansbold.ttf', 12)
    fontover = pygame.font.Font('freesansbold.ttf', 40)
    

    while True:
        log_state()

    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        # remaining lives
        text = font.render(f"Remaining lives: {player.lives}", True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.topleft = (10,10)

        #Game over
        textover = fontover.render("You lost!", True, (255, 255, 255))
        overRect = textover.get_rect()
        overRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        
        updatable.update(dt)
        screen.blit(text, textRect)
        
        for ast in asteroids:
            if ast.collides_with(player):
                player.lives -= 1
                ast.kill()
                screen.fill("red")
                print(f"Remaining lives: {player.lives}")
                if player.lives <= 0:
                    log_event("player_hit")
                    print("Game over!")
                    screen.fill("black")
                    screen.blit(textover, overRect)
                    pygame.display.flip()
                    pygame.time.wait(2500)
                    sys.exit()

            for shot in shots:
                if ast.collides_with(shot):
                    log_event("asteroid_shot")
                    ast.split()
                    shot.kill()

        for draws in drawable:
            draws.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

        
        


    
        
        


if __name__ == "__main__":
    main()
 



