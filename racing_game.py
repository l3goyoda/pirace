import math
import numpy
import pygame
import sys


class world():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        mapImage = pygame.image.load("Track.png")
        self.screen.blit(mapImage, )
    def draw(self):
        pass

def main():
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption("Car physics 2d test")
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))
    angle = 0
    x_velocity = 0
    y_velocity = 0
    car_mass = 50
    friction = 0.7
    player_x = 0
    player_y = 0
    world.__init__(screen, 0, 0)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                sys.exit()
        pressed = pygame.key.get_pressed()
        #if pressed[pygame.K_w]:
        pygame.display.update()

            
main()