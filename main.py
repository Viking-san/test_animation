import pygame as pg

pg.init()
width = 800
height = 600
run = True
fps = 60
clock = pg.time.Clock()
win = pg.display.set_mode((width, height), pg.RESIZABLE | pg.FULLSCREEN)
pg.display.set_caption(f'fps: {fps}')
sword1, sword2, sword3, sword4 = pg.image.load('sword1.png'), pg.image.load('sword2.png'), pg.image.load('sword1_.png'), pg.image.load('sword2_.png')
mace1, mace2, mace3, mace4 = pg.image.load('mace1.png'), pg.image.load('mace2.png'), pg.image.load('mace1_.png'), pg.image.load('mace2_.png')
sword = pg.transform.scale(pg.transform.rotate(sword1, -90), (110, 80))
mace = pg.transform.scale(pg.transform.rotate(mace1, -40), (160, 140))
hit_animation = {'sword': {'left': [sword1, sword2, sword2], 'right': [sword3, sword4, sword4]},
                 'mace': {'left': [mace1, mace2, mace2], 'right': [mace3, mace4, mace4]}}
circle_x = 100
circle_y = 100
circle_vel = 5


def win_update(player_):
    win.fill((200, 200, 200))
    pg.draw.circle(win, (0, 0, 0), player_.get_head(), player_.headr)
    pg.draw.rect(win, (0, 0, 0), player_.get_body())
    win.blit(sword, (500, 40))
    win.blit(mace, (565, -13))
    pg.draw.circle(win, (0, 255, 0), (circle_x, circle_y), 20)
    if player_.weapon == 'sword':
        pg.draw.rect(win, (0, 0, 0), (520, 43, 95, 35), 3)
    elif player_.weapon == 'mace':
        pg.draw.rect(win, (0, 0, 0), (615, 43, 95, 35), 3)


class Player:
    def __init__(self):
        self.x = 50
        self.y = 300
        self.headr = 25
        self.hit_animation_count = 0
        self.is_attacking = False
        self.dir = 'right'
        self.weapon = 'sword'

    def get_head(self):
        return self.x + 25, self.y - 40

    def get_body(self):
        return self.x, self.y, 50, 80

    def attack(self):
        speed_animation = 10
        win_update(self)
        if self.dir == 'left':
            win.blit(hit_animation[self.weapon][self.dir][self.hit_animation_count // speed_animation], (self.x + 60, self.y - 120))
        elif self.dir == 'right':
            win.blit(hit_animation[self.weapon][self.dir][self.hit_animation_count // speed_animation], (self.x - 220, self.y - 120))

        if self.hit_animation_count == len(hit_animation[self.weapon][self.dir]) * speed_animation - 1:
            self.hit_animation_count = 0
            self.is_attacking = False


player = Player()

while run:
    clock.tick(fps)
    if 0 < circle_x < height:
        circle_x += circle_vel
    else:
        circle_vel *= -1
        circle_x += circle_vel

    if player.is_attacking:
        player.attack()
        player.hit_animation_count += 1
    else:
        win_update(player)
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
            if event.key == pg.K_f:
                player.is_attacking = True
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 43 < y < 73 and not player.is_attacking:
                if 520 < x < 605:
                    player.weapon = 'sword'
                if 615 < x < 710:
                    player.weapon = 'mace'

    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        player.x -= 10
        if not player.is_attacking:
            player.dir = 'right'
    if keys[pg.K_d]:
        player.x += 10
        if not player.is_attacking:
            player.dir = 'left'

pg.quit()
