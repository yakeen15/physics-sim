width = 800
height = 600
dt = 0.01
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
            print(self.vx)
            self.vx=-self.vx
        if self.y+self.ht>height or self.y<0:
            print(self.vy)
            self.vy=-self.vy
    def netforcex(self,f=[0]):
        netf = 0
        for force in f:
            netf = netf+force
        self.ax = netf
    def netforcey(self,f=[0]):
        netf = 0
        for force in f:
            netf = netf+force
        self.ay = netf
    def harmonicForcex(self,coef=0.002,orig=150):
        return -coef*(self.x-orig)
    def harmonicForcey(self,coef=0.002,orig=150):
        return -coef*(self.y-orig)
    def gravForce(self,g=0.5):
        return g
    def buoyancy(self,vol=1,liq_den=1,g=0.5):
        return -vol*liq_den*g
    def viscous(self,visc=1):
        return -visc*self.vy