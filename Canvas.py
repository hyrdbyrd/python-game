import pygame
from Consts import *

M = METRIKA

class Canvas:
    def __init__(self, title='Snake Game'):
        self.title = title
        self.init_window()

    def draw(self):
        w, h = METRIKA['size']
        color = COLORS['black']

        y = 0
        for row in self.matrix:
            x = 0
            for cell in row:
                if cell == 1:
                    color = COLORS['green']
                if cell == 0:
                    color = COLORS['black']
                if cell == 2:
                    color = COLROS['red']

                pygame.draw.rect(
                    self.screen,
                    color,
                    pygame.Rect(x * w, y * h, w, h)
                )
                x += 1
            y += 1

    def update(self):
        self.window.blit(self.screen, (0, 0))
        pygame.display.update()

    def init_window(self):
        pygame.init()
        self.window = pygame.display.set_mode((M['width'], M['height']))

        # Set title for window
        pygame.display.set_caption(self.title)

        self.screen = pygame.Surface((M['width'], M['height']))
