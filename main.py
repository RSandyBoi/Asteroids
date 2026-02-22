import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import shot



def main():
    #initial setup for pygame window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    
    
   
    
    updatable = pygame.sprite.Group() #updateable groups
    drawable = pygame.sprite.Group() #drawable groups
    asteroids = pygame.sprite.Group() #asteroid groups
    shots = pygame.sprite.Group() #shot groups


    
    Asteroid.containers = (updatable, drawable, asteroids)  # set asteroid containers to groups
    AsteroidField.containers = (updatable)  # set asteroid field containers to groups (single-tuple)
    Shot.containers = (shots, updatable, drawable)  # set shot containers to groups
    asteroid_field = AsteroidField()  # create asteroid field object

    Player.containers = (updatable, drawable)  # set player containers to groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # create player at screen center
    
    dt = 0

    while True: #main game loop for runtime arguments
        log_state()

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #exit condition to end game if window is closed
                pygame.quit()
                return
            
        updatable.update(dt)

        for asteroid in asteroids: #check for collision between player and asteroids
            if player.collide_with(asteroid):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        for asteroid in asteroids: #check for collision between shots and asteroids
            for shot in shots:
                if shot.collide_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.kill()
                    shot.kill()
        screen.fill("black") #background color
        
        
       #main_player.draw(screen)
        for entity in drawable:
            entity.draw(screen)

        
        pygame.display.flip() #update display
        dt = clock.tick(60) / 1000 # Limit to 60 FPS
        player.cooldown_timer -= dt #update player cooldown timer
        



if __name__ == "__main__":
    main()
