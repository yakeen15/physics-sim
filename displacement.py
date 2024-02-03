import pygame
import sys

t , dt = 0 , 0.01
width = 800
height = 600
class Rect:
    def __init__(self,w,h,clr,x,y):
        self.wd = w
        self.ht = h
        self.clr = clr
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
    def update(self):
        self.x = self.x+self.vx*dt
        self.y = self.y+self.vy*dt
        self.vx = self.vx+self.ax*dt
        self.vy = self.vy+self.ay*dt
    def wallCollision(self):
        if self.x+self.wd>width or self.x<0:
            print(self.x)
            self.vx=-self.vx
        if self.y+self.ht>height or self.y<0:
            print(self.y)
            flag=1
            self.vy=-self.vy
    def harmonicForcex(self,coef=0.002,orig=150):
        self.ax=-coef*(self.x-orig)
    def harmonicForcey(self,coef=0.002,orig=150):
        self.ay=-coef*(self.y-orig)
    def gravForce(self,g=0.5):
        self.ay = g

pygame.init()


window_size = (width, height)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Rectangle Generator")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TRANSPARENT_BLUE = (0, 0, 255, 128)
orig_x = 300
orig_y = 400
r1 = Rect(25,25,BLACK,orig_x,orig_y)
while True:
    t=t+dt
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
    r1.wallCollision()
    r1.harmonicForcex()
    #r1.harmonicForcey()
    r1.update()
    pygame.draw.rect(window, r1.clr, (r1.x, r1.y, r1.wd, r1.ht))
    pygame.display.flip()
