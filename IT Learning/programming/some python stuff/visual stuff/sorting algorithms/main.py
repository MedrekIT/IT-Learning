import pygame as pg
import random as rd


def randomize(t):
    for i in range(200):
        t[i] = i
    rd.shuffle(t)


def bubblesort(win, t):
    for i in range(len(t) - 1):
        for j in range(len(t) - 1 - i):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]
                draw(win, t, {j: (255, 0, 0)}, True)


def insertionsort(win, t):
    for i in range(len(t)):
        j = i
        while j > 0 and t[j] < t[j - 1]:
            t[j], t[j - 1] = t[j - 1], t[j]
            j -= 1
            draw(win, t, {j: (255, 0, 0), i: (255, 255, 255)}, True)


def draw(win, t, col=None, sorting=False):
    if col is None:
        col = {}
    pg.draw.rect(win, (0, 0, 0), (0, 0, 900, 800))
    for i in range(len(t)):
        if i in col:
            color = col[i]
        else:
            color = (0, 255, 0)
        pg.draw.lines(win, color, True,
                      [((i * 800 + 400) // len(t), 700), ((i * 800 + 400) // len(t), 700 - 3.5 * t[i])], 800 // (2 * len(t)))
    if sorting:
        pg.display.update()


def writeInfo(win, t):
    pg.draw.circle(win, (0, 0, 255), (400, 400), 50, 5)
    draw(win, t)
    pg.display.update()


pg.init()

WIN = pg.display.set_mode((800, 800))
pg.display.set_caption("Sorting algorithms")

if __name__ == '__main__':
    runWin = True
    clock = pg.time.Clock()

    t = [0] * 200

    randomize(t)

    while runWin:
        clock.tick(60)
        WIN.fill((0, 0, 0))

        writeInfo(WIN, t)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                runWin = False
            if event.type != pg.KEYDOWN:
                continue
            if event.key == pg.K_b:
                bubblesort(WIN, t)
            if event.key == pg.K_d:
                draw(WIN, t)
            if event.key == pg.K_i:
                insertionsort(WIN, t)
            if event.key == pg.K_r:
                randomize(t)

    pg.quit()
