import pygame as pg
import random as rd


class Ball:
    def __init__(self, xpos, ypos, xvel, yvel, ballsize):
        self.xpos = xpos
        self.ypos = ypos
        self.vel = pg.math.Vector2(xvel, yvel)
        self.ballsize = ballsize

    def collision(self):
        if self.xpos + self.ballsize > 1000:
            self.xpos = 1000 - self.ballsize
            self.vel.x *= -1
        elif self.xpos - self.ballsize < 0:
            self.xpos = self.ballsize
            self.vel.x *= -1
        if self.ypos + self.ballsize > 800:
            self.ypos = 800 - self.ballsize
            self.vel.y *= -1
        elif self.ypos - self.ballsize < 0:
            self.ypos = self.ballsize
            self.vel.y *= -1

    def ballmovement(self):
        self.xpos += self.vel.x
        self.ypos += self.vel.y

    def drawball(self):
        pg.draw.circle(WIN, (200, 200, 200), (self.xpos, self.ypos), self.ballsize)


class Plate:
    def __init__(self, xpos, ypos, platelen):
        self.xpos = xpos
        self.ypos = ypos
        self.platelen = platelen

    def borders(self):
        if self.ypos - self.platelen / 2 < 0:
            self.ypos = self.platelen / 2
        elif self.ypos + self.platelen / 2 > 800:
            self.ypos = 800 - self.platelen / 2

    def drawplate(self):
        pg.draw.rect(WIN, (255, 255, 255), (self.xpos - 10, self.ypos - self.platelen / 2, 20, self.platelen))


pg.init()
WIN = pg.display.set_mode((1000, 800))
pg.display.set_caption("Pong")

if __name__ == '__main__':
    runWin: bool = True
    clock = pg.time.Clock()

    leftplayer = Plate(50, 400, 100)
    rightplayer = Plate(950, 400, 100)
    ball = Ball(450, 400, rd.uniform(1, 5), rd.uniform(1, 5), 20)

    while runWin:
        clock.tick(60)
        WIN.fill((50, 50, 75))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                runWin = False

        keys = pg.key.get_pressed()
        if keys[pg.K_w] and leftplayer.ypos - leftplayer.platelen / 2 > 0:
            leftplayer.ypos -= 5
        if keys[pg.K_s] and leftplayer.ypos + leftplayer.platelen / 2 < 800:
            leftplayer.ypos += 5
        if keys[pg.K_UP] and rightplayer.ypos - rightplayer.platelen / 2 > 0:
            rightplayer.ypos -= 5
        if keys[pg.K_DOWN] and rightplayer.ypos + rightplayer.platelen / 2 < 800:
            rightplayer.ypos += 5

        leftplayer.borders()
        rightplayer.borders()

        leftplayer.drawplate()
        rightplayer.drawplate()
        ball.ballmovement()
        ball.collision()
        ball.drawball()
        pg.display.update()
    pg.quit()
