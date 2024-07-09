import pygame as pg
import math


class Body:
    DIS = 149.6e6 * 100
    G = 6.67428e-11
    SCALE = 50 / DIS
    TIMESTEP = 3600 * 24 * 100

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updPoints = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updPoints.append((x, y))

            pg.draw.lines(win, self.color, False, updPoints, 2)

        pg.draw.circle(win, self.color, (x, y), self.radius)

    def forceAttr(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        force = self.G * self.mass * other.mass / distance ** 2

        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def updPos(self, bodies):
        total_fx = total_fy = 0
        for body in bodies:
            if self == body:
                continue

            fx, fy = self.forceAttr(body)
            total_fx += fx
            total_fy += fy

        self.x_vel += ((total_fx / self.mass) * self.TIMESTEP)
        self.y_vel += (total_fy / self.mass) * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))


pg.init()

WIDTH, HEIGHT = 800, 800
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Two bodies simulation")

if __name__ == '__main__':
    runWin = True
    clock = pg.time.Clock()

    b_m = 10 ** 29 / Body.TIMESTEP
    b1 = Body(0, 0.5 * Body.DIS, 5, (0, 0, 0), b_m)
    b1.x_vel = math.sqrt((Body.G * b_m) / (2.3 * 10 ** 10))
    b2 = Body(0, -0.5 * Body.DIS, 5, (0, 0, 0), b_m)
    b2.x_vel = -math.sqrt((Body.G * b_m) / (2.3 * 10 ** 10))
    b3 = Body(1 * Body.DIS, 0, 5, (0, 0, 0), b_m)
    b3.y_vel = -math.sqrt((Body.G * b_m) / (2.3 * 10 ** 10))

    bodies = [b1, b2, b3]

    while runWin:
        clock.tick(60)
        WIN.fill((255, 255, 255))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                runWin = False

        for body in bodies:
            body.updPos(bodies)
            body.draw(WIN)

        pg.display.update()
    pg.quit()
