import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1200, 800))


class Moon:
    def __init__(self):
        self.colour = (255, 200, 0)
        self.image = pygame.image.load('moon.jpg')

    def draw(self):
        screen.blit(self.image, (300, 0))
        pygame.display.update()


class Tree_trunk:
    def __init__(self):
        self.colour = (50, 40, 0)
        self.Surface = screen

    def draw(self):
        start_x = 100
        for m in range(0, 2):
            pygame.draw.line(self.Surface, self.colour, (start_x, 0), (start_x, 800), 5)
            pygame.display.update()
            start_x = start_x + 100
        right_x = 1100


class Tree_Leaves:
    def __init__(self):
        self.colour = (55, 55, 0)
        self.Surface = screen
        self.r_leaf = pygame.Rect(0, 0, 100, 600)
        self.r_leaf2 = pygame.Rect(100, 0, 100, 700)
        self.r_leaf3 = pygame.Rect(205, 0, 90, 500)

    def draw(self):
        pygame.draw.rect(screen, self.colour, self.r_leaf, 0)
        pygame.draw.rect(screen, (55, 100, 0), self.r_leaf2, 0)
        pygame.draw.rect(screen, (100, 100, 0), self.r_leaf3, 0)


class Tree:
    def __init__(self):
        self.image = pygame.image.load('new_tree.jpg')

    def draw(self):
        screen.blit(self.image, (0, 1100))
        pygame.display.update()


moon = Moon()
moon.draw()
tree_trunk = Tree_trunk()
tree_trunk.draw()
tree_leaves = Tree_Leaves()
tree_leaves.draw()
tree = Tree()
tree.draw()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.flip()
