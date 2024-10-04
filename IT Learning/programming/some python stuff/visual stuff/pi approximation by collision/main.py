import pygame as pg


class Block:
    def __init__(self, xpos, rectsize, vel, mass, xlimit):
        self.x = xpos
        self.y = 250
        self.rectsize = rectsize
        self.vel = vel
        self.mass = mass
        self.xlimit = xlimit

    def moveblock(self):
        self.x += self.vel

    def drawblock(self):
        xcon = constrain(self.x, self.xlimit)
        pg.draw.rect(WIN, (150, 150, 150), (xcon, self.y - self.rectsize, self.rectsize, self.rectsize), 10)

    def checkcollision(self, other):
        global PIAPPROX
        if self.x <= 0:
            clicksound.play()
            self.vel *= -1
            PIAPPROX += 1
        if self.x + self.rectsize >= other.x and self.x <= other.x + other.rectsize:
            clicksound.play()
            PIAPPROX += 1
            self.vel, other.vel = (self.mass * self.vel + other.mass * other.vel + other.mass * (
                        other.vel - self.vel)) / (self.mass + other.mass), (
                                              other.mass * other.vel + self.mass * self.vel + self.mass * (
                                                  self.vel - other.vel)) / (self.mass + other.mass)


def constrain(xpos, min_val, max_val=600):
    if xpos < min_val:
        return min_val
    if xpos > max_val:
        return max_val
    return xpos


def drawscreen():
    pg.draw.rect(WIN, (100, 75, 75), (0, 250, 600, 50))
    block1.drawblock()
    block2.drawblock()

    count = text.render(f'Bounces = {PIAPPROX}', True, (255, 255, 255), None)
    WIN.blit(count, (0, 250))


pg.init()
WIN = pg.display.set_mode((600, 300))
pg.display.set_caption("Pi approximation by collision")

PIAPPROX = 0

pg.font.init()
text = pg.font.SysFont('Times New Roman', 30)

STEPS = 10

clicksound = pg.mixer.Sound('clack-85854.mp3')

if __name__ == '__main__':
    runWin: bool = True
    clock = pg.time.Clock()

    block1 = Block(100, 20, 0, 1, 0)
    block2 = Block(300, 100, -5 / STEPS, 100 ** 1, 20)

    while runWin:
        clock.tick(60)
        WIN.fill((50, 50, 75))

        for i in range(STEPS):
            block1.moveblock()
            block2.moveblock()

            block1.checkcollision(block2)
        drawscreen()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                runWin = False

        pg.display.update()
    pg.quit()
