
import pygame
import time

BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
DRED  = (200,   0,   0)

pygame.init()

size = (300, 200)
screen = pygame.display.set_mode(size)

done = False

clock = pygame.time.Clock()

btn_color = DRED
btn = pygame.Surface([50,50])
btn.fill(btn_color)
btn_rect = btn.get_rect(topleft=(50,70))
draw_circle = False
button_pressed = False
timer = 0

circle_delay = 2000 #milliseconds
alpha_delay = 50
alpha_timer = 0
alpha = 255
circle = pygame.Surface([50,50]) #size of circle
circle.set_alpha(alpha)
circle.fill(BLACK)
pygame.draw.ellipse(circle, RED, (0,0, 50, 50)) #((draw to topleft of new surface),(size of circle))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            button_pressed = True
            
    if btn_rect.collidepoint(pygame.mouse.get_pos()):
        btn_color = RED
    else:
        btn_color = DRED
    screen.fill(BLACK)
    btn.fill(btn_color)
    screen.blit(btn, btn_rect)
    
    if pygame.time.get_ticks()-timer > circle_delay:
        timer = pygame.time.get_ticks()
        if button_pressed:
            draw_circle = True
    elif pygame.time.get_ticks()-alpha_timer > alpha_delay:
        alpha_timer = pygame.time.get_ticks()
        alpha -= 2
        circle.set_alpha(alpha)
        if alpha <= 0: #reset
            draw_circle = False
            alpha = 255
    
    if draw_circle:
        screen.blit(circle, (200,70))
                   
    pygame.display.flip()
    
    clock.tick(60)
pygame.quit()
