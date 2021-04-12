import os
import random
import time
import neat
import pygame as pg

winWidth = 500
winHeight = 800
gen = 0
drawLines = True

win = pg.display.set_mode((winWidth, winHeight))
pg.display.set_caption("Flappy Bird")

pg.font.init()
statFont = pg.font.SysFont("comicsans", 50)
endFONT = pg.font.SysFont("comicsans", 70)

birdImg = [
    pg.transform.scale2x(pg.image.load("Imgs\\Bird1.png")),
    pg.transform.scale2x(pg.image.load("Imgs\\Bird2.png")),
    pg.transform.scale2x(pg.image.load("Imgs\\Bird3.png")),
]
baseImg = pg.transform.scale2x(pg.image.load("Imgs\\Base.png").convert_alpha())
pipeImg = pg.transform.scale2x(pg.image.load("Imgs\\Pipe.png").convert_alpha())
bgImg = pg.transform.scale2x(pg.image.load("Imgs\\BG.png").convert_alpha())


class Bird:
    bImg = birdImg
    maxRot = 25
    rotVel = 20
    animaTime = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tickCou = 0
        self.vel = 0
        self.height = self.y
        self.imgCou = 0
        self.img = self.bImg[0]

    def jump(self):
        self.vel = -10.5
        self.tickCou = 0
        self.height = self.y

    def move(self):
        self.tickCou += 1

        disp = self.vel * (self.tickCou) + 0.5 * (3) * (self.tickCou) ** 2

        if disp >= 16:
            disp = (disp / abs(disp)) * 16

        if disp < 0:
            disp -= 2

        self.y = self.y + disp

        if disp < 0 or self.y < self.height + 50:
            if self.tilt < self.maxRot:
                self.tilt = self.maxRot

        else:
            if self.tilt > -90:
                self.tilt -= self.rotVel

    def draw(self, win):
        self.imgCou += 1

        if self.imgCou < self.animaTime:
            self.img = self.bImg[0]

        elif self.imgCou < self.animaTime * 2:
            self.img = self.bImg[1]

        elif self.imgCou < self.animaTime * 3:
            self.img = self.bImg[2]

        elif self.imgCou < self.animaTime * 4:
            self.img = self.bImg[1]

        elif self.imgCou == self.animaTime * 4 + 1:
            self.img = self.bImg[0]
            self.imgCou = 0

        if self.tilt <= -80:
            self.img = self.bImg[1]
            self.imgCou = self.animaTime * 2

        blitRotateCenter(win, self.img, (self.x, self.y), self.tilt)

    def mask(self):
        return pg.mask.from_surface(self.img)


class Pipes:
    gap = 200
    vel = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.top = 0
        self.bottom = 0
        self.pipeTop = pg.transform.flip(pipeImg, False, True)
        self.pipeBottom = pipeImg
        self.passed = False
        self.setHeight()

    def setHeight(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.pipeTop.get_height()
        self.bottom = self.height + self.gap

    def move(self):
        self.x -= self.vel

    def draw(self, win):
        win.blit(self.pipeTop, (self.x, self.top))
        win.blit(self.pipeBottom, (self.x, self.bottom))

    def collide(self, bird, win):
        birdMask = bird.mask()

        topMask = pg.mask.from_surface(self.pipeTop)
        bottomMask = pg.mask.from_surface(self.pipeBottom)

        topOffset = (self.x - bird.x, self.top - round(bird.y))
        bottomOffset = (self.x - bird.x, self.bottom - round(bird.y))

        bPoint = birdMask.overlap(bottomMask, bottomOffset)
        tPoint = birdMask.overlap(topMask, topOffset)

        if bPoint or tPoint:
            return True

        return False


class Base:
    vel = 5
    width = baseImg.get_width()
    img = baseImg

    def __init__(self, y):
        self.y = y
        self.x = 0
        self.x1 = self.width

    def move(self):
        self.x -= self.vel
        self.x1 -= self.vel

        if self.x + self.width < 0:
            self.x = self.x1 + self.width

        if self.x1 + self.width < 0:
            self.x1 = self.x + self.width

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
        win.blit(self.img, (self.x1, self.y))


def blitRotateCenter(surf, image, topleft, angle):
    rotatedImage = pg.transform.rotate(image, angle)
    newRect = rotatedImage.get_rect(center=image.get_rect(topleft=topleft).center)
    surf.blit(rotatedImage, newRect.topleft)


def drawWin(win, birds, base, pipes, pipeCou, score, gen):
    if gen == 0:
        gen = 1

    win.blit(bgImg, (0, 0))

    for pipe in pipes:
        pipe.draw(win)

    base.draw(win)

    for bird in birds:
        if drawLines:
            try:
                pg.draw.line(
                    win,
                    (255, 0, 0),
                    (
                        bird.x + bird.img.get_width() / 2,
                        bird.y + bird.img.get_height() / 2,
                    ),
                    (
                        pipes[pipeCou].x + pipes[pipeCou].pipeTop.get_width() / 2,
                        pipes[pipeCou].height,
                    ),
                    5,
                )
                pg.draw.line(
                    win,
                    (255, 0, 0),
                    (
                        bird.x + bird.img.get_width() / 2,
                        bird.y + bird.img.get_height() / 2,
                    ),
                    (
                        pipes[pipeCou].x + pipes[pipeCou].pipeBottom.get_width() / 2,
                        pipes[pipeCou].bottom,
                    ),
                    5,
                )

            except:
                pass

        bird.draw(win)

    texts = statFont.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(texts, (winWidth - 10 - texts.get_width(), 10))

    textg = statFont.render("Gens: " + str(gen), 1, (255, 255, 255))
    win.blit(textg, (10, 10))

    texta = statFont.render("Alive: " + str(len(birds)), 1, (255, 255, 255))
    win.blit(texta, (10, 50))

    pg.display.update()


def main(genomes, config):
    global win, gen
    win = win
    gen += 1

    nets = []
    gens = []
    birds = []

    base = Base(730)
    pipes = [Pipes(600)]

    win = pg.display.set_mode((winWidth, winHeight))
    run = True
    score = 0

    clock = pg.time.Clock()

    for _, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        birds.append(Bird(230, 350))
        gens.append(genome)

    while run and len(birds) > 0:
        clock.tick(30)
        rem = []
        addPipe = False
        pipeCount = 0

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                quit()
                break

        if len(birds) > 0:
            if (
                len(pipes) > 1
                and birds[0].x > pipes[0].x + pipes[0].pipeTop.get_width()
            ):
                pipeCount = 1

        for x, bird in enumerate(birds):
            gens[x].fitness += 0.1
            bird.move()

            output = nets[birds.index(bird)].activate(
                (
                    bird.y,
                    abs(bird.y - pipes[pipeCount].height),
                    abs(bird.y - pipes[pipeCount].bottom),
                )
            )

            if output[0] > 0.5:
                bird.jump()

        base.move()

        for pipe in pipes:
            pipe.move()

            for bird in birds:
                if pipe.collide(bird, win):
                    gens[birds.index(bird)].fitness -= 1
                    nets.pop(birds.index(bird))
                    gens.pop(birds.index(bird))
                    birds.pop(birds.index(bird))

            if pipe.x + pipe.pipeTop.get_width() < 0:
                rem.append(pipe)

            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                addPipe = True

        if addPipe:
            score += 1

            for g in gens:
                g.fitness += 5

            pipes.append(Pipes(winWidth))

        for r in rem:
            pipes.remove(r)

        for bird in birds:
            if bird.y + bird.img.get_height() - 10 >= 730 or bird.y < -50:
                nets.pop(birds.index(bird))
                gens.pop(birds.index(bird))
                birds.pop(birds.index(bird))

        drawWin(win, birds, base, pipes, pipeCount, score, gen)


def run(path):
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        path,
    )

    popu = neat.Population(config)
    popu.add_reporter(neat.StdOutReporter(True))

    stats = neat.StatisticsReporter()
    popu.add_reporter(stats)

    winner = popu.run(main, 50)
    print(f"\nBest genome:\n{winner}")


if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    path = os.path.join(dir, "config.txt")
    run(path)
