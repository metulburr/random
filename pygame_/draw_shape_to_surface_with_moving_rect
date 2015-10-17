import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
screen_rect = screen.get_rect()

circle = pygame.Surface([500,300]).convert()
circle.fill((255,0,255)) #make abnormal bg color
circle.set_colorkey((255,0,255)) #hide bg
pygame.draw.circle(circle, (200,200,0), screen_rect.center, 25, 0)
circle_rect = circle.get_rect()

running = True
while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        circle_rect.x += 1
    elif keys[pygame.K_LEFT]:
        circle_rect.x -= 1
    screen.blit(circle, circle_rect)
    pygame.display.update()
