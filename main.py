import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    #initial setup for pygame window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    #version and screen size logging
    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #initialize main player object in center of screen
    
    updatable = pygame.sprite.Group() #updateable groups
    drawable = pygame.sprite.Group() #drawable groups
    asteroids = pygame.sprite.Group() #asteroid groups
    Player.containers = (updatable, drawable) #set player containers to groups
    Asteroid.containers = (updatable, drawable, asteroids) #set asteroid containers to groups
    AsteroidField.containers = (updatable) #set asteroid field containers to groups
    field = AsteroidField() #create asteroid field object


    while True: #main game loop for runtime arguments
        log_state()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #exit condition to end game if window is closed
                pygame.quit()
                return
            

        screen.fill("black") #background color
        #main_player.update(dt)
        updatable.update(dt)
       #main_player.draw(screen)
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip() #update the full display surface to the screen
        dt = clock.tick(60) / 1000 # Limit to 60 FPS
        



if __name__ == "__main__":
    main()
