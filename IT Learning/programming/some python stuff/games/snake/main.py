import pygame as pg
import time
import Snake
import Apple
import GameLogic

if __name__ == '__main__':
    pg.init()

    #Game window
    WIN = pg.display.set_mode((800, 800))
    pg.display.set_caption("Snake")
    pg.font.init()
    gameFont = pg.font.SysFont('Times New Roman', 30)

    #Game time parameters
    tickSpeed: int = 10
    slowness: int = 100
    gameTime = time.time()
    clock = pg.time.Clock()

    #Creating objects
    snake = Snake.Snake(2, 40, 40)
    apple = Apple.Apple(snake)

    #Base snake direction
    snakeDirection = previousDirection = None

    runWin: bool = True
    while runWin:
        #Game speed
        clock.tick(tickSpeed)

        #Drawing a display and objects
        WIN.fill((50, 50, 75))
        GameLogic.drawgame(WIN, gameFont, gameTime, snake, apple)

        #Events and keyboard handling
        for event in pg.event.get():
            if event.type == pg.QUIT:
                runWin = False
            if event.type == pg.KEYDOWN:
                #Snake motion control
                if (pg.key.name(event.key) in {'w', 's'} and snakeDirection not in {'w', 's'} or
                        pg.key.name(event.key) in {'a', 'd'} and snakeDirection not in {'a', 'd'}):
                    previousDirection = snakeDirection
                    snakeDirection = pg.key.name(event.key)
                #Apple position reset
                if event.key == pg.K_r:
                    apple.__init__(snake)

        #Handling snake biting itself
        if not GameLogic.checkcollision(tickSpeed, slowness, snake, apple, snakeDirection, previousDirection):
            runWin = False
        #Changing direction based on motion control
        if snakeDirection:
            snakeDirection = snake.movement(snakeDirection, previousDirection)

        #Using a delay until slowness is small enough
        if slowness > 4:
            pg.time.delay(slowness)

        #Refreshing game screen
        pg.display.update()

        #Limiting game time
        if time.time() - gameTime >= 180:
            runWin = False
    pg.quit()
