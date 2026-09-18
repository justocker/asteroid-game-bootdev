import pygame
from constants import *
from logger import log_state
from player import Player

def main():
    pygame.init()

    updatable = pygame.sprite.Group() # this will hold all the objects that can be updated
    drawable = pygame.sprite.Group() # this will hold all the objects that can be drawn
    Player.containers = (updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt: float = 0.0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    

    

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)

        for draws in drawable:
            draws.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

        
        


if __name__ == "__main__":
    main()
 



