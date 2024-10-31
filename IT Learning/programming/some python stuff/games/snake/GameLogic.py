import pygame as pg
from time import time

def checkcollision(tickSpeed, slowness, snake, apple, direction, previous):
    headx, heady = snake.cords[0]
    #Checking if snake's head is touching its body
    if (direction == 'w' and snake.cords[1] in {(headx, heady - 5), (headx, heady + 75)} or
            direction == 's' and snake.cords[1] in {(headx, heady + 5), (headx, heady - 75)} or
            direction == 'a' and snake.cords[1] in {(headx - 5, heady), (headx + 75, heady)} or
            direction == 'd' and snake.cords[1] in {(headx + 5, heady), (headx - 75, heady)}):
        direction = previous
    for i in snake.cords[1:]:
        if (direction == 'w' and ((i[0], i[1] + 5) == snake.cords[0] or (i[0], i[1] - 75) == snake.cords[0]) or
                direction == 's' and ((i[0], i[1] - 5) == snake.cords[0] or (i[0], i[1] + 75) == snake.cords[0]) or
                direction == 'a' and ((i[0] + 5, i[1]) == snake.cords[0] or (i[0] - 75, i[1]) == snake.cords[0]) or
                direction == 'd' and ((i[0] - 5, i[1]) == snake.cords[0] or (i[0] + 75, i[1]) == snake.cords[0])):
            return False
    #Checking if snake's head is going to eat an apple
    if (direction == 'w' and (
            (apple.applePosX, apple.applePosY + 5) == snake.cords[0] or (apple.applePosX, apple.applePosY - 75) ==
            snake.cords[0]) or
            direction == 's' and ((apple.applePosX, apple.applePosY - 5) == snake.cords[0] or (
                    apple.applePosX, apple.applePosY + 75) == snake.cords[0]) or
            direction == 'a' and ((apple.applePosX + 5, apple.applePosY) == snake.cords[0] or (
                    apple.applePosX - 75, apple.applePosY) == snake.cords[0]) or
            direction == 'd' and ((apple.applePosX - 5, apple.applePosY) == snake.cords[0] or (
                    apple.applePosX + 75, apple.applePosY) == snake.cords[0])):
        snake.cords.insert(0, (apple.applePosX, apple.applePosY))
        snake.snakeSize += 1

        #Speeding up the game when an apple is eaten
        if slowness > 4:
            slowness -= 5 if slowness % 2 == 0 else 1
        else:
            tickSpeed += 5 if tickSpeed % 2 == 0 else 1
        #Generating new apple
        apple.__init__(snake)
    return True

def drawgame(WIN, gameFont, gameTime, snake, apple):
    #Drawing objects
    snake.drawsnake(WIN)
    apple.drawapple(WIN)

    #Drawing scoreboard
    scoreboard = gameFont.render(f'{int(time()-gameTime)} SCORE = {snake.snakeSize - 2}', True, (255, 255, 255), None)
    WIN.blit(scoreboard, (50, 50))

    # Refreshing game screen
    pg.display.update()