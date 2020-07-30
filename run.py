import pygame, sys, os
from rocket import Rocket


class Game(object):

    def __init__(self):
        # Config
        self.color_x = 0
        self.tps_max = 120.0
        self.resolution = (1280, 720)

        # Initialization
        self.up_or_down = 0
        pygame.init()
        self.screen = pygame.display.set_mode(self.resolution)
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        self.background = pygame.image.load(os.path.join("game_assets", "bg.jpg"))

        self.player = Rocket(self)

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick() # Wymusza wywołanie funkcji tick (39 linijka) o wartość self.tps_max = 60 razy na sekundę
                self.tps_delta -= 1 / self.tps_max

            # Drawing
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    def tick(self):
        self.player.tick() # self.player odnosi się do 18 linijki, natomiast z tick() odnosi się do def tick(self): znajdującego się w pliku rocket.py czyli tak jakby wpisać Rocket(self).tick(self)
        self.player.tick()
        self.color_change()
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.player.draw()


    def color_change(self):
        if self.color_x == 0:
            self.up_or_down = 0
        if self.color_x == 255:
            self.up_or_down = 1
        if self.up_or_down == 0:
            self.color_x += 1
        if self.up_or_down == 1:
            self.color_x -= 1

if __name__=="__main__":
    Game()