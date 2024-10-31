import pygame as pg
import random as rd

class Apple:
    def __init__(self, snake):
        #Initializing apple coordinates
        self.applePosX: int = rd.randrange(0, 75, 5)
        self.applePosY: int = rd.randrange(0, 75, 5)

        while (self.applePosX, self.applePosY) in snake.cords:
            self.applePosX = rd.randrange(0, 75, 5)
            self.applePosY = rd.randrange(0, 75, 5)

    #Drawing an apple
    def drawapple(self, WIN):
        pg.draw.rect(WIN, (255, 75, 0), (self.applePosX * 10, self.applePosY * 10, 50, 50), 0, 3)
