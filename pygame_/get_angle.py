import pygame as pg
import math

def get_angle(A, B, C):
    '''get angle ABC'''
    AB = math.sqrt(math.pow(B.rect.x-A.rect.x, 2)+math.pow(B.rect.y-A.rect.y, 2))
    BC = math.sqrt(math.pow(B.rect.x-C.rect.x, 2)+math.pow(B.rect.y-C.rect.y, 2))
    AC = math.sqrt(math.pow(C.rect.x-A.rect.x, 2)+math.pow(C.rect.y-A.rect.y, 2))
    try:
        return math.degrees(math.acos((BC*BC+AB*AB-AC*AC)/(2*BC*AB)))
    except ZeroDivisionError:
        return 0
        
def make_text(message,color,center,size):
    font = pg.font.SysFont("Fixedsys500c",50)
    text = font.render(message,True,color)
    rect = text.get_rect(center=center)
    return text,rect

def update_text(msg=''):
    return make_text(msg, (0,0,225), screen_rect.center, 13)
        

class Points(object):
    def __init__(self, center):
        self.image = pg.Surface([25,25]).convert()
        self.rect = self.image.get_rect(center=center)
        self.inner_point = pg.Surface([3,3]).convert()
        self.inner_point.fill((0,0,0))
        self.inner_point_rect = self.inner_point.get_rect(center=center)
        self.click = False
        
    def get_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(pg.mouse.get_pos()):
                self.click = True
                pg.mouse.get_rel()
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.click = False
        
    def update(self):
        if self.click:
            self.rect.move_ip(pg.mouse.get_rel())
            self.inner_point_rect.center = self.rect.center
            self.rect.clamp_ip(screen_rect)
            self.inner_point_rect.clamp_ip(screen_rect)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.inner_point, self.inner_point_rect)
        
class Point1(Points):
    '''point A'''
    def __init__(self):
        super(Point1, self).__init__((100,300))
        self.image.fill((255,0,0))
        
class Point2(Points):
    '''theta point'''
    def __init__(self):
        super(Point2, self).__init__((200,200))
        self.image.fill((0,0,255))
        
class Point3(Points):
    '''point C'''
    def __init__(self):
        super(Point3, self).__init__((300,300))
        self.image.fill((0,255,0))

if __name__ == '__main__':
    running = True
    pg.init()
    screen = pg.display.set_mode((600,400))
    screen_rect = screen.get_rect()
    clock = pg.time.Clock()
    angle = 0
    points = [Point1(), Point2(), Point3()]
    text, text_rect = update_text()

    while running:
        screen.fill((0,0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
            for obj in points:
                obj.get_event(event)
        
        screen.blit(text, text_rect)
        for obj in points:
            obj.draw(screen)
            obj.update()
        pg.draw.aaline(screen, (255,255,255), points[1].rect.center, points[0].rect.center, 2)
        pg.draw.aaline(screen, (255,255,255), points[1].rect.center, points[2].rect.center, 2)
        
        
        angle = get_angle(points[0], points[1], points[2])
        angle_display = '{0:.2f}'.format(angle)
        text, text_rect = update_text(angle_display)
        pg.display.update()
        clock.tick(60)
