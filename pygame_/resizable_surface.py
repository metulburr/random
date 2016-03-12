
import pygame as pg
import random

class Ball:
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        self.image = pg.Surface([50,50]).convert()
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        
        self.speed_init = 10
        self.speed = self.speed_init
        self.set_ball()
        
    def set_ball(self):
        self.vel = [random.choice([-1,1]), 0]
        self.rect.center = self.screen_rect.center
        self.true_pos = list(self.rect.center)
        self.speed = self.speed_init
        
    def move(self):
        if self.rect.left <= 0:
            self.vel[0] *= -1
        elif self.rect.right >= self.screen_rect.right:
            self.vel[0] *= -1
        self.true_pos[0] += self.vel[0] * self.speed
        #self.true_pos[1] += self.vel[1] * self.speed
        self.rect.center = self.true_pos
        
    def update(self, screen_rect):
        self.screen_rect = screen_rect
        self.move()
        
    def draw(self, surf):
        surf.blit(self.image, self.rect)
        


class Control:
    def __init__(self):
        self.resolutions = [(300,200), (600,400),(800, 600), (928, 696)]
        self.render_size = self.resolutions[-1] #largest
        self.screen = pg.display.set_mode(self.resolutions[-1], pg.RESIZABLE)
        self.screen_rect = self.screen.get_rect()
        self.render_surf = pg.Surface(self.render_size).convert()

        #pg.event.clear(pg.VIDEORESIZE)
        self.clock = pg.time.Clock()
        self.done = False
        self.fps = 60
        
        self.ball = Ball(self.screen_rect)
        
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.VIDEORESIZE:
                self.on_resize(event.size)
                #pg.event.clear(pg.VIDEORESIZE)
                
    def on_resize(self, size):
        if size == self.screen_rect.size:
            return
        res_index = self.resolutions.index(self.screen_rect.size)
        adjust = 1 if size > self.screen_rect.size else -1
        if 0 <= res_index+adjust < len(self.resolutions):
            new_size = self.resolutions[res_index+adjust]
        else:
            new_size = self.screen_rect.size
        self.screen = pg.display.set_mode(new_size, pg.RESIZABLE)
        self.screen_rect.size = new_size
        self.set_scale()

    def set_scale(self):
        w_ratio = self.render_size[0]/float(self.screen_rect.w)
        h_ratio = self.render_size[1]/float(self.screen_rect.h)
        self.scale = (w_ratio, h_ratio)
                
    def update(self):
        self.ball.update(self.render_surf.get_rect()) #give obj updated screen size
        
    def render(self):
        if self.render_size != self.screen_rect.size:
            scale_args = (self.render_surf, self.screen_rect.size, self.screen)
            pg.transform.smoothscale(*scale_args)
        else:
            self.screen.blit(self.render_surf, (0, 0))
        self.render_surf.fill((255,255,255))
        self.ball.draw(self.render_surf)

        
    def game_loop(self):
        while not self.done:
            self.event_loop()
            self.update()
            self.render()
            pg.display.update()
            self.clock.tick(self.fps)

pg.init()
app = Control()
app.game_loop()
pg.quit()
