import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
import player


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
    main_player = player.Player(x = SCREEN_WIDTH / 2, y =SCREEN_HEIGHT // 2)
    while True: #main game loop for runtime arguments
        log_state()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #exit condition to end game if window is closed
                pygame.quit()
                return
        screen.fill("black") #background color
        main_player.update(dt)
        main_player.draw(screen)
        pygame.display.flip() #update the full display surface to the screen
        dt = clock.tick(60) / 1000.0 # Limit to 60 FPS
        



if __name__ == "__main__":
    main()
