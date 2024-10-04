import pygame as pg
import random as rd
import time


class Ball:
    def __init__(self, mass, mousepos, vx, vy, rgbintensity, t1):
        self.mass = mass
        self.position = pg.Vector2(mousepos)
        self.balltime = t1
        self.v0 = vy
        self.velocity = pg.Vector2(vx, vy - (self.balltime * 9.81))
        self.color = rgbintensity

    def ballmovement(self):
        t2 = time.time()
        self.position.x += self.velocity.x
        self.position.y += (self.v0 * (t2-self.balltime)) + (9.81 * (t2-self.balltime)**2)/2 if self.position.y + self.mass * 50 < 800 else 0

        if self.position.x + self.mass*5 >= 800 or self.position.x - self.mass*5 <= 0:
            self.velocity.x *= -1
        if self.position.y - self.mass*5 <= 0:
            self.position.y = self.mass * 50
            self.velocity.y *= -1
        if self.position.y + self.mass*50 >= 800:
            self.velocity.y = 0
            self.position.y = 800 - self.mass * 50

    def ballcollision(self, other):
        if (((self.position.x - other.position.x) ** 2) + (self.position.y - other.position.y) ** 2) ** 0.5 <= (self.mass*5 + other.mass*5):
            tempvel = self.velocity
            tempother = other.velocity
            diffpos = self.position - other.position
            sqaredpos = diffpos.x ** 2 + diffpos.y ** 2
            self.velocity = self.velocity + (((2 * other.mass) / (self.mass + other.mass)) * ((tempother - tempvel) * (other.position - self.position) / sqaredpos)) * (
                    other.position - self.position)
            other.velocity = other.velocity + (((2 * self.mass) / (self.mass + other.mass)) * ((tempvel - tempother) * (self.position - other.position) / sqaredpos)) * (
                    self.position - other.position)

    def drawball(self):
        pg.draw.circle(WIN, self.color, self.position, self.mass * 50)


def newball():
    t1 = time.time()
    mass = 1
    ballpos = pg.mouse.get_pos()
    vx = rd.uniform(-10, 10)
    vy = 10
    rgb = pg.Vector3(rd.randint(100, 255), rd.randint(100, 255), rd.randint(100, 255))

    ballsList.append(Ball(mass, ballpos, vx, vy, rgb, t1))


pg.init()
WIN = pg.display.set_mode((800, 800))
pg.display.set_caption("Colliding balls")

ballsList: list = []

if __name__ == '__main__':
    runWin: bool = True
    clock = pg.time.Clock()

    while runWin:
        clock.tick(30)
        WIN.fill((50, 50, 75))

        for i, ball in enumerate(ballsList):
            ball.ballmovement()
            for otherBall in ballsList[i + 1:]:
                ball.ballcollision(otherBall)
            ball.drawball()
            print(ball.velocity, ball.position)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                runWin = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                newball()

        pg.display.update()
    pg.quit()
