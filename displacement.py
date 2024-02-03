import pygame
from Rect import Rect, width, height
from lib.lib import draw_rect_alpha
import sys

pygame.init()

window_size = (width, height)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Rectangle Generator")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TRANSPARENT_BLUE = (0, 0, 255, 128)
orig_x = 300
orig_y = 250
r1 = Rect(25,25,BLACK,orig_x,orig_y)
flag=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                r1.gravForce(g=-0.5)
            elif event.key == pygame.K_DOWN:
                r1.gravForce()
    window.fill(WHITE)
    forces = []
    r1.wallCollision()
    if r1.y+r1.ht>height//2:
        forces.append(r1.buoyancy(vol=1,liq_den=2))
        #forces.append(r1.viscous(visc=0.01))
        if flag!=1:
            print("In water")
        flag=1
    elif flag==1:
        print("Out water")
        flag=0
    forces.append(r1.gravForce())
    r1.netforcey(forces)
    r1.update()
    draw_rect_alpha(window, (0,0,255,127),(0, height//2, width, height//2))
    pygame.draw.rect(window, r1.clr, (r1.x, r1.y, r1.wd, r1.ht))
    pygame.display.flip()
