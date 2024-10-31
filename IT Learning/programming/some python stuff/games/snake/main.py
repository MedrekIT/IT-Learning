import pygame as pg
import time
import Snake
import Apple
import GameLogic

if __name__ == '__main__':
    pg.init()

    WIN = pg.display.set_mode((800, 800))

    tickSpeed: int = 10
    slowness: int = 100

    pg.display.set_caption("Snake")
    pg.font.init()
    gameFont = pg.font.SysFont('Times New Roman', 30)

    gameTime = time.time()

    runWin: bool = True
    clock = pg.time.Clock()

    snake = Snake.Snake(2, 40, 40)
    apple = Apple.Apple(snake)

    snakeDirection = previousDirection = None

    while runWin:
        clock.tick(tickSpeed)
        WIN.fill((50, 50, 75))

        GameLogic.drawgame(WIN, gameFont, gameTime, snake, apple)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                runWin = False
            if event.type == pg.KEYDOWN:
                if (pg.key.name(event.key) in {'w', 's'} and snakeDirection not in {'w', 's'} or
                        pg.key.name(event.key) in {'a', 'd'} and snakeDirection not in {'a', 'd'}):
                    previousDirection = snakeDirection
                    snakeDirection = pg.key.name(event.key)
                if event.key == pg.K_r:
                    apple.__init__(snake)

        if not GameLogic.checkcollision(tickSpeed, slowness, snake, apple, snakeDirection, previousDirection):
            runWin = False
        if snakeDirection:
            snakeDirection = snake.movement(snakeDirection, previousDirection)

        if slowness > 4:
            pg.time.delay(slowness)
        pg.display.update()

        if time.time() - gameTime >= 180:
            print(snake.snakeSize - 2)
            runWin = False
    pg.quit()
