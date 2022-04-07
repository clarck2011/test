import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((2000, 990))




class Moon:
    def __init__(self):
        self.x = 1000
        self.y = 300
        self.colour = (255, 255, 255)
        self.pos = (self.x, self.y)
        self.radius = 80
        self.Surface = screen
    def draw(self):
        pygame.draw.circle(self.Surface, self.colour, self.pos, self.radius, width=0)
        pygame.display.flip()
    def move(self):
        pygame.draw.circle(self.Surface, (0, 0, 0), self.pos, self.radius, width=0)
        pygame.draw.circle(self.Surface, self.colour, (self.x + 10, self.y), self.radius, width=0)
        pygame.display.flip()



moon = Moon()
moon.draw()
moon.move()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
