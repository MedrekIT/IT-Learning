import pygame as pg
import random as rd
import math


class Ball:
    def __init__(self, mousepos, vel, rgbintensity, mass):
        self.position = pg.Vector2(mousepos)
        self.velocity = pg.Vector2(vel)
        self.color = rgbintensity
        self.mass = mass
        self.radius = 15*math.log(self.mass, 2)

    def ballmovement(self):
        self.position += self.velocity

        if self.position.x + self.radius > 800:
            self.position.x = 800 - self.radius
            self.velocity.x *= -1
        elif self.position.x - self.radius < 0:
            self.position.x = self.radius
            self.velocity.x *= -1

        if self.position.y + self.radius > 800:
            self.position.y = 800 - self.radius
            self.velocity.y *= -1
        elif self.position.y - self.radius < 0:
            self.position.y = self.radius
            self.velocity.y *= -1

    def ballcollision(self, other):
        distance = self.position.distance_to(other.position)
        if distance < self.radius + other.radius:
            overlap = self.radius + other.radius - distance
            direction = (self.position - other.position).normalize()

            self.position += direction * (overlap / 2)
            other.position -= direction * (overlap / 2)

            tempvel = self.velocity
            tempother = other.velocity
            diffpos = self.position - other.position
            sqaredpos = diffpos.x ** 2 + diffpos.y ** 2
            self.velocity = self.velocity + ((2*other.mass/(self.mass+other.mass))*(tempother - tempvel) * (other.position - self.position) / sqaredpos) * (
                    other.position - self.position)
            other.velocity = other.velocity + ((2*self.mass/(self.mass+other.mass))*(tempvel - tempother) * (self.position - other.position) / sqaredpos) * (
                    self.position - other.position)

    def drawball(self):
        pg.draw.circle(WIN, self.color, self.position, 15*math.log(self.mass, 2))


def newball():
    ballpos = pg.mouse.get_pos()
    ballmovement = pg.Vector2(rd.uniform(-10, 10), rd.uniform(-10, 10))
    rgb = pg.Vector3(rd.randint(100, 255), rd.randint(100, 255), rd.randint(100, 255))
    mass = rd.randint(1, 15)

    ballsList.append(Ball(ballpos, ballmovement, rgb, mass))


pg.init()
WIN = pg.display.set_mode((800, 800))
pg.display.set_caption("Elastic ball collision")

ballsList: list = []

if __name__ == '__main__':
    runWin: bool = True
    clock = pg.time.Clock()

    while runWin:
        clock.tick(60)
        WIN.fill((50, 50, 75))

        for i, ball in enumerate(ballsList):
            ball.ballmovement()
            for otherBall in ballsList[i + 1:]:
                ball.ballcollision(otherBall)
            ball.drawball()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                runWin = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                newball()
                print(len(ballsList))

        pg.display.update()
    pg.quit()
