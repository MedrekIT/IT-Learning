import pygame as pg

class Character:
    def __init__(self):
        self.xpos = 400
        self.ypos = 400

    def drawcharacter(self):
        pg.draw.rect(WIN, (255, 255, 255), (self.xpos, self.ypos, 50, 50))

pg.init()
WIN = pg.display.set_mode((800, 800))
pg.display.set_caption("Elastic ball collision")

if __name__ == '__main__':
    runWin: bool = True
    clock = pg.time.Clock()

    player = Character()

    while runWin:
        clock.tick(60)
        WIN.fill((50, 50, 75))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                runWin = False

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            player.ypos -= 5
        if keys[pg.K_a]:
            player.xpos -= 5
        if keys[pg.K_s]:
            player.ypos += 5
        if keys[pg.K_d]:
            player.xpos += 5

        player.drawcharacter()
        pg.display.update()
    pg.quit()
