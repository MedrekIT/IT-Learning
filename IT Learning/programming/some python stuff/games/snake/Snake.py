import pygame as pg

class Snake:
    def __init__(self, length, row, col):
        self.snakeSize: int = length
        self.x: int = row
        self.y: int = col
        self.cords: list = []

        for i in range(self.snakeSize):
            self.cords.append((self.x, self.y + i))

    def drawsnake(self, WIN):
        for x, y in self.cords:
            pg.draw.rect(WIN, (75, 255, 0), (x * 10, y * 10, 50, 50), 0, 2)

    def movement(self, direction, previous):
        headx, heady = self.cords[0]
        if direction == 'w':
            if self.cords[1] in {(headx, heady - 5), (headx, heady + 75)}:
                return previous
            heady -= 5 if heady > 0 else -75
        if direction == 's':
            if self.cords[1] in {(headx, heady + 5), (headx, heady - 75)}:
                return previous
            heady += 5 if heady < 75 else -75
        if direction == 'a':
            if self.cords[1] in {(headx - 5, heady), (headx + 75, heady)}:
                return previous
            headx -= 5 if headx > 0 else -75
        if direction == 'd':
            if self.cords[1] in {(headx + 5, heady), (headx - 75, heady)}:
                return previous
            headx += 5 if headx < 75 else -75

        self.cords.insert(0, (headx, heady))
        del self.cords[-1]

        return direction