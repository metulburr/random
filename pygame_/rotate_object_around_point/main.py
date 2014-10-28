import pygame as pg
import math

class Rotator:
    def __init__(self, screen_rect):
        self.radar = screen_rect.center
        self.radar_len = 100
        self.angle = 0
        self.image = pg.Surface([25,25]).convert()
        self.get_pos()
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.image.fill((255,0,0))
        self.speed = 200

    def render(self, screen):
        screen.blit(self.image, self.rect)
        pg.draw.line(screen, (255,255,255), self.radar, (self.x,self.y), 1)
        
    def update(self, seconds):
        keys = pg.key.get_pressed()
        self.get_pos()
        self.rect.center = (self.x, self.y)
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.angle -= self.speed * seconds
        elif keys[pg.K_LEFT] or keys[pg.K_a]:
            self.angle += self.speed * seconds
        
    def get_pos(self):
        self.x = self.radar[0] + math.cos(math.radians(self.angle)) * self.radar_len
        self.y = self.radar[1] + math.sin(math.radians(self.angle)) * self.radar_len

if __name__ == '__main__':
    running = True
    pg.init()
    screen = pg.display.set_mode((600,400))
    screen_rect = screen.get_rect()
    rotator = Rotator(screen_rect)
    clock = pg.time.Clock()
    seconds = 0

    while running:
        screen.fill((0,0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                rotator.radar = pg.mouse.get_pos()
        rotator.update(seconds)
        rotator.render(screen)
        pg.display.set_caption('x,y:{} {}'.format(rotator.x, rotator.y))
        pg.display.update()
        milli = clock.tick(60)
        seconds = milli / 1000.0

