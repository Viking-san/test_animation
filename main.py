import pygame as pg

pg.init()
width = 800
height = 400
run = True
fps = 60
clock = pg.time.Clock()
win = pg.display.set_mode((width, height), pg.RESIZABLE)
hit = False
dir = 'right'
weapon = 'sword'
sword1, sword2, sword3, sword4 = pg.image.load('sword1.png'), pg.image.load('sword2.png'), pg.image.load('sword1_.png'), pg.image.load('sword2_.png')
mace1, mace2, mace3, mace4 = pg.image.load('mace1.png'), pg.image.load('mace2.png'), pg.image.load('mace1_.png'), pg.image.load('mace2_.png')
sword = pg.transform.scale(pg.transform.rotate(sword1, -90), (110, 80))
mace = pg.transform.scale(pg.transform.rotate(mace1, -40), (160, 140))
hit_animation = {'sword': {'left': [sword1, sword2], 'right': [sword3, sword4]},
                 'mace': {'left': [mace1, mace2], 'right': [mace3, mace4]}}


def win_update(p, weapon):
    win.fill((200, 200, 200))
    pg.draw.circle(win, (0, 0, 0), p.get_head(), p.headr)
    pg.draw.rect(win, (0, 0, 0), p.get_body())
    win.blit(sword, (500, 40))
    win.blit(mace, (565, -13))
    if weapon == 'sword':
        pg.draw.rect(win,(0, 0, 0), (520, 43, 95, 35), 3)
    elif weapon == 'mace':
        pg.draw.rect(win, (0, 0, 0), (615, 43, 95, 35), 3)


class Player:
    def __init__(self):
        self.x = 50
        self.y = 300
        self.headr = 25

    def get_head(self):
        return self.x + 25, self.y - 40

    def get_body(self):
        return self.x, self.y, 50, 80

    def hit_with(self, weapon, dir):
        if dir == 'left':
            for i in hit_animation[weapon][dir]:
                win_update(self, weapon)
                win.blit(i, (self.x + 60, self.y - 120))
                pg.time.delay(100)
                pg.display.update()
            pg.time.delay(220)
        elif dir == 'right':
            for i in hit_animation[weapon][dir]:
                win_update(self, weapon)
                win.blit(i, (self.x - 220, self.y - 120))
                pg.time.delay(100)
                pg.display.update()
            pg.time.delay(220)


player = Player()

while run:
    clock.tick(fps)
    pg.display.set_caption(f'fps: {fps}')
    if hit:
        player.hit_with(weapon, dir)
        hit = False
    else:
        win_update(player, weapon)
        pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
            if event.key == pg.K_f:
                hit = True
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 43 < y < 73:
                if 520 < x < 605:
                    weapon = 'sword'
                if 615 < x < 710:
                    weapon = 'mace'

    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        player.x -= 10
        dir = 'right'
    if keys[pg.K_d]:
        player.x += 10
        dir = 'left'

pg.quit()
