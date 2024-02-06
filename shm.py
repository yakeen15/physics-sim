import pygame
from Rect import Circ
from lib.lib import draw_rect_alpha, writelog
import sys
from math import sin, pi
width = 800
height = 600
dt = 0.01
pygame.init()

window_size = (width, height)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Simple Harmonic Motion")

SQR_SIZE = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TRANSPARENT_BLUE = (0, 0, 255, 128)
orig_x = 400
orig_y = 200
orig_angle = 4
orig_theta = orig_angle*pi/180
length_string = 100
r1 = Circ(SQR_SIZE,BLACK,orig_x,orig_y)
r1.theta = orig_theta
logger = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #or len(logger)>100:
            pygame.quit()
            writelog(logger)
            sys.exit()
    window.fill(WHITE)
    r1.wallCollision(width,height)
    r1.pendulum(L=length_string)
    logger.append([r1.x,r1.y])
    r1.update(dt)
    pygame.draw.circle(window, r1.clr, (r1.x, r1.y),r1.r)
    pygame.draw.line(window, BLACK, (r1.x, r1.y), (orig_x-length_string*sin(orig_theta),0), 2)
    pygame.display.flip()