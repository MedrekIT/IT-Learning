import pygame as pg


class Ball:
    def __init__(self, xpos, rectsize, vel, mass):
        self.x = xpos
        self.y = 250
        # self.rectsize = rectsize
        self.vel = vel
        self.mass = mass

    def moveball(self):
        self.x += self.vel

    def drawball(self):
        xcon = constrain(self.x, self.xlimit)
        pg.draw.rect(WIN, (150, 150, 150), (xcon, self.y - self.rectsize, self.rectsize, self.rectsize), 10)

    def checkcollision(self, other):
        if self.x <= 0:
            clicksound.play()
            self.vel *= -1
        if self.x + self.rectsize >= other.x and self.x <= other.x + other.rectsize:
            clicksound.play()
            self.vel, other.vel = (self.mass * self.vel + other.mass * other.vel + other.mass * (
                        other.vel - self.vel)) / (self.mass + other.mass), (
                                              other.mass * other.vel + self.mass * self.vel + self.mass * (
                                                  self.vel - other.vel)) / (self.mass + other.mass)


def drawscreen():
    pg.draw.rect(WIN, (100, 75, 75), (0, 250, 600, 50))
    block1.drawblock()
    block2.drawblock()

    # count = text.render(f' = {}', True, (255, 255, 255), None)
    # WIN.blit(count, (0, 250))


pg.init()
WIN = pg.display.set_mode((600, 300))
pg.display.set_caption("Pool balls")

pg.font.init()
text = pg.font.SysFont('Times New Roman', 30)

balls = []


clicksound = pg.mixer.Sound('clack_sound.wav')

if __name__ == '__main__':
    runWin: bool = True
    clock = pg.time.Clock()

    for _ in range(15):
        balls.append(Ball)

    block1 = Block(100, 20, 0, 1, 0)
    block2 = Block(300, 100, -5 / STEPS, 100 ** 7, 20)

    while runWin:
        clock.tick(60)
        WIN.fill((50, 50, 75))

        block1.moveblock()
        block2.moveblock()

            block1.checkcollision(block2)
        drawscreen()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                runWin = False

        pg.display.update()
    pg.quit()
