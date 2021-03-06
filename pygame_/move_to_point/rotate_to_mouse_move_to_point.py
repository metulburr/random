import pygame
import random
import math

def normalize(v):
    vmag = magnitude(v)
    return [ v[i]/vmag  for i, val in enumerate(v) ]
    
def magnitude(v):
    return math.sqrt(sum(v[i]*v[i] for i, val in enumerate(v)))

def add(u, v):
    return [ u[i]+v[i] for i, val in enumerate(u) ]

def sub(u, v):
    return [ u[i]-v[i] for i, val in enumerate(u) ]    
 
class Bullet():
    def __init__(self, screenrect):
        self.orig_image = pygame.image.load("bullet.png")
        self.image = self.orig_image
        self.rect = self.image.get_rect(center=screenrect.center)
        self.target = self.rect.center
        self.angle = self.get_angle()
        self.speed = 4
        self.set_target(screenrect.center)
        
    def get_angle(self):
        mouse = pygame.mouse.get_pos()
        image_facing = 272
        offset = (mouse[1]-self.rect.centery, mouse[0]-self.rect.centerx)
        self.angle = image_facing-math.degrees(math.atan2(*offset))
        self.image = pygame.transform.rotate(self.orig_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def set_target(self, pos):
        self.target = pos
        
    def move_to_target(self):
        if self.rect.center != self.target:
            target_vector = sub(self.target, self.rect.center) 
            if magnitude(target_vector) > 2: 
                move_vector = [c * self.speed for c in normalize(target_vector)]
                self.rect.x, self.rect.y = add((self.rect.x, self.rect.y), move_vector)
        
    def update(self):
        self.move_to_target()
    
    def render(self, screen):
        screen.blit(self.image, self.rect)
 
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
obj = Bullet(screen.get_rect())
 
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEMOTION:
            obj.get_angle()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            obj.set_target(pygame.mouse.get_pos())

    screen.fill((255,255,255))
    obj.update()
    obj.render(screen)
    clock.tick(60)
    pygame.display.update()

