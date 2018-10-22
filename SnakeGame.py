from Consts import METRIKA as M

from pygame.locals import *
import pygame

from time import time

import sys

from random import random
from Canvas import Canvas

class SnakeGame(Canvas):
    isAlive = True
    # In seconds!
    speed = 0.3
    matrix = [
        [i * 0 for i in range(M['fractions'][0])]
        for i in range(M['fractions'][1])
    ]

    diffTime = time() + speed

    # Xdir and Ydir
    dirs = (1, 0)

    def inputFrom(self, events, with_keys=False):
        for event in events:
            if event.type == KEYDOWN:
                self.diffTime -= self.speed
            if event.type == KEYDOWN and event.key == K_LEFT and self.dirs != (1, 0):
                self.dirs = (-1, 0)
            if event.type == KEYDOWN and event.key == K_RIGHT and self.dirs != (-1, 0):
                self.dirs = (1, 0)
            if event.type == KEYDOWN and event.key == K_UP and self.dirs != (0, 1):
                self.dirs = (0, -1)
            if event.type == KEYDOWN and event.key == K_DOWN and self.dirs != (0, -1):
                self.dirs = (0, 1)
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                sys.exit(0)

    def update(self):
        self.moveAhead()
        self.diffTime = time()
        self.inputFrom(pygame.event.get(), True)
        Canvas.update(self)

    def moveAhead(self):
        dirX, dirY = self.dirs

        i = 0
        for pos in self.pos:
            self.matrix[pos[1]][pos[0]] = 0

            if i == 0:
                prevPos = pos
                self.pos[i] = (pos[0] + dirX, pos[1] + dirY)
            else:
                self.pos[i] = prevPos
                prevPos = pos

            # Cycle loop of space
            newPos = self.pos[i]
            if newPos[1] > len(self.matrix) - 1:
                self.pos[i] = (newPos[0], 0)
            if newPos[1] < 0:
                self.pos[i] = (newPos[0], len(self.matrix) - 1)
            if newPos[0] > len(self.matrix[0]) - 1:
                self.pos[i] = (0, newPos[1])
            if newPos[0] < 0:
                self.pos[i] = (len(self.matrix[0]) - 1, newPos[1])

            i += 1

        for pos in self.pos:
            self.matrix[pos[1]][pos[0]] = 1

    def __init__(self):
        Canvas.__init__(self, 'Snake Game v1.0.0')

        fw, fh = M['fractions']

        cY = fh // 2
        cX = fw // 2

        self.pos = [
            (cX + 1, cY),
            (cX, cY),
            (cX - 1, cY)
        ]

        # Set snake at center
        self.matrix[cY][cX] = 1
        self.matrix[cY][cX - 1] = 1
        self.matrix[cY][cX + 1] = 1

        self.loop()

    def apple_gen(self):
        pass

    def loop(self):
        while self.isAlive:
            self.draw()
            self.inputFrom(pygame.event.get())
            localTimeDiff = time() - self.diffTime
            if localTimeDiff >= self.speed:
                self.update()

if __name__ == '__main__': SnakeGame()
