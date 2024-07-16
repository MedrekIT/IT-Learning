import pygame as pg
import random as rd


class Snake:
    def __init__(self, length, row, col):
        self.snakeSize: int = length
        self.x: int = row
        self.y: int = col
        self.cords: list = []

        for i in range(self.snakeSize):
            self.cords.append((self.x, self.y + i))

    def drawsnake(self):
        for x, y in self.cords:
            pg.draw.rect(WIN, (75, 255, 0), (x * 10, y * 10, 10, 10), 0, 2)


class Apple:
    def __init__(self):
        self.applePosX: int = rd.randint(0, 79)
        self.applePosY: int = rd.randint(0, 79)

        while (self.applePosX, self.applePosY) in snake.cords:
            self.applePosX = rd.randint(0, 79)
            self.applePosY = rd.randint(0, 79)

    def drawapple(self):
        pg.draw.rect(WIN, (255, 75, 0), (self.applePosX * 10, self.applePosY * 10, 10, 10), 0, 3)


def checkcollision(direction, previous):
    headx, heady = snake.cords[0]
    if (direction == 'w' and snake.cords[1] in {(headx, heady - 1), (headx, heady + 79)} or
            direction == 's' and snake.cords[1] in {(headx, heady + 1), (headx, heady - 79)} or
            direction == 'a' and snake.cords[1] in {(headx - 1, heady), (headx + 79, heady)} or
            direction == 'd' and snake.cords[1] in {(headx + 1, heady), (headx - 79, heady)}):
        direction = previous
    for i in snake.cords[1:]:
        if (direction == 'w' and ((i[0], i[1] + 1) == snake.cords[0] or (i[0], i[1] - 79) == snake.cords[0]) or
                direction == 's' and ((i[0], i[1] - 1) == snake.cords[0] or (i[0], i[1] + 79) == snake.cords[0]) or
                direction == 'a' and ((i[0] + 1, i[1]) == snake.cords[0] or (i[0] - 79, i[1]) == snake.cords[0]) or
                direction == 'd' and ((i[0] - 1, i[1]) == snake.cords[0] or (i[0] + 79, i[1]) == snake.cords[0])):
            return False
    if (direction == 'w' and (
            (apple.applePosX, apple.applePosY + 1) == snake.cords[0] or (apple.applePosX, apple.applePosY - 79) ==
            snake.cords[0]) or
            direction == 's' and ((apple.applePosX, apple.applePosY - 1) == snake.cords[0] or (
                    apple.applePosX, apple.applePosY + 79) == snake.cords[0]) or
            direction == 'a' and ((apple.applePosX + 1, apple.applePosY) == snake.cords[0] or (
                    apple.applePosX - 79, apple.applePosY) == snake.cords[0]) or
            direction == 'd' and ((apple.applePosX - 1, apple.applePosY) == snake.cords[0] or (
                    apple.applePosX + 79, apple.applePosY) == snake.cords[0])):
        snake.cords.insert(0, (apple.applePosX, apple.applePosY))
        snake.snakeSize += 1
        global TICKSPEED, SLOWNESS
        if SLOWNESS > 4:
            SLOWNESS -= 5 if SLOWNESS % 2 == 0 else 1
        else:
            TICKSPEED += 5 if TICKSPEED % 2 == 0 else 1
        apple.__init__()
    return True


def snakemovement(direction, previous):
    headx, heady = snake.cords[0]
    if direction == 'w':
        if snake.cords[1] in {(headx, heady - 1), (headx, heady + 79)}:
            return previous
        heady -= 1 if heady > 0 else -79
    if direction == 's':
        if snake.cords[1] in {(headx, heady + 1), (headx, heady - 79)}:
            return previous
        heady += 1 if heady < 79 else -79
    if direction == 'a':
        if snake.cords[1] in {(headx - 1, heady), (headx + 79, heady)}:
            return previous
        headx -= 1 if headx > 0 else -79
    if direction == 'd':
        if snake.cords[1] in {(headx + 1, heady), (headx - 79, heady)}:
            return previous
        headx += 1 if headx < 79 else -79

    snake.cords.insert(0, (headx, heady))
    del snake.cords[-1]

    return direction


def drawgame():
    snake.drawsnake()
    apple.drawapple()
    scoreboard = gameFont.render(f'SCORE = {snake.snakeSize - 2}', True, (255, 255, 255), None)
    WIN.blit(scoreboard, (50, 50))

    pg.display.update()


pg.init()

WIN = pg.display.set_mode((800, 800))

TICKSPEED: int = 40
SLOWNESS: int = 75

pg.display.set_caption("Snake")
pg.font.init()
gameFont = pg.font.SysFont('Times New Roman', 30)

if __name__ == '__main__':
    runWin: bool = True
    clock = pg.time.Clock()

    snake = Snake(2, 40, 40)
    apple = Apple()

    snakeDirection = previousDirection = None

    while runWin:
        clock.tick(TICKSPEED)
        WIN.fill((50, 50, 75))

        drawgame()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                runWin = False
            if event.type == pg.KEYDOWN:
                if (pg.key.name(event.key) in {'w', 's'} and snakeDirection not in {'w', 's'} or
                        pg.key.name(event.key) in {'a', 'd'} and snakeDirection not in {'a', 'd'}):
                    previousDirection = snakeDirection
                    snakeDirection = pg.key.name(event.key)
                if event.key == pg.K_r:
                    apple.__init__()

        if not checkcollision(snakeDirection, previousDirection):
            runWin = False
        if snakeDirection:
            snakeDirection = snakemovement(snakeDirection, previousDirection)

        if SLOWNESS > 4:
            pg.time.delay(SLOWNESS)
        pg.display.update()
    pg.quit()
