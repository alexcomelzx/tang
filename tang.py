import random
import pygame as pg

win_w = 400
win_h = 400
pg.init()
clock = pg.time.Clock()


def main():
    win = pg.display.set_mode((win_w, win_h))
    pg.display.set_caption("n")

    snake = Snake()
    food = Food()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                snake.turn(event.key)
                if event.key == pg.K_ESCAPE and snake.isDead():
                    return main()
                if not snake.isDead():
                    createWin(win)
                    snake.move()
                    for b in snake.body:
                        pg.draw.rect(win, (0, 0, 0), b, 0)

                if snake.body[0] == food.block:
                    food.beEaten()
                    snake.addBlock()
                pg.draw.rect(win, (0, 0, 0), food.block, 0)
                pg.display.flip()
                clock.tick(5)


def createWin(win):
    white = pg.Color(255, 255, 255)
    win.fill(white)

    drawGrid(win)


def drawGrid(win):
    black = pg.Color(0, 0, 0)
    grid_w = win_w // 20
    grid_h = win_h // 200
    grid_dx = 0
    grid_dy = 0
    for i in range(20):
        pg.draw.line(win, black, (grid_dx, 0), (grid_dy, win_w))
        pg.draw.line(win, black, (0, grid_dy), (win_w, grid_dy))
        grid_dx = grid_dx + grid_w
        grid_dy = grid_dy + grid_h


class Snake:
    def __init__(self):
        self.direction = pg.K_RIGHT
        self.body = []
        self.addBlock()
        self.addBlock()
        self.addBlock()

    def addBlock(self):
        left, top = 0, 0
        if self.body:
            left, top = self.body[0].left, self.body[0].top
        block = pg.Rect(left, top, 20, 20)
        if self.direction == pg.K_LEFT:
            block.left = block.left - 20
        elif self.direction == pg.K_RIGHT:
            block.left = block.left + 20
        elif self.direction == pg.K_UP:
            block.top = block.top - 20
        elif self.direction == pg.K_UP:
            block.top = block.top + 20
        self.body.insert(0, block)

    def move(self):
        self.addBlock()
        self.body.pop()

    def isDead(self):
        if self.body[0].x > win_w - 20 \
                or self.body[0].x < 0 \
                or self.body[0].y > win_h - 20 \
                or self.body[0].y < 0:
            return True
        if self.body[0] in self.body[1:]:
            return True
        return False

    def turn(self, turnDir):
        if (self.direction == pg.K_UP or self.direction == pg.K_DOWN) \
                and \
                (turnDir == pg.K_LEFT or turnDir == pg.K_RIGHT):
            self.direction == turnDir
        if (self.direction == pg.K_LEFT or self.direction == pg.K_RIGHT) \
                and \
                (turnDir == pg.K_UP or turnDir == pg.K_DOWN):
            self.direction = turnDir


class Food:
    def __init__(self):
        self.block = pg.Rect(200, 200, 20, 20)

    def beEaten(self):
        self.block.left = random.randint(0, 20) * 20
        self.block.top = random.randint(0, 20) * 20


main()
