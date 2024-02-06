from math import sin, cos
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
        self.theta = 0
        self.omega = 0
        self.alpha = 0
        self.forcex = []
        self.forcey = []
        self.forcer = []
    def update(self,dt):
        self.netforcex()
        self.netforcey()
        self.netforceRot()
        self.x = self.x+self.vx*dt
        self.y = self.y+self.vy*dt
        self.vx = self.vx+self.ax*dt
        self.vy = self.vy+self.ay*dt
        self.theta = self.theta+self.omega*dt
        self.omega = self.omega+self.alpha*dt
    def wallCollision(self,width,height):
        if self.x+self.wd>width or self.x<0:
            self.vx=-self.vx
        if self.y+self.ht>height or self.y<0:
            self.vy=-self.vy
    def netforceRot(self):
        netf = 0
        for force in self.forcer:
            netf = netf+force
        self.forcer = []
        self.alpha = netf
    def netforcex(self):
        netf = 0
        for force in self.forcex:
            netf = netf+force
        self.forcex = []
        self.ax = netf
    def netforcey(self):
        netf = 0
        for force in self.forcey:
            netf = netf+force
        self.forcey = []
        self.ay = netf
    def dragy(self,drag_coef):
        self.forcey.append([-drag_coef*self.vy**2])
    def pendulum(self,g=0.5,L=1):
        self.forcer.append(-sin(self.theta)*g/L)
        self.forcex.append(-L*sin(self.theta)*self.omega**2+(-sin(self.theta)*g/L)*L*cos(self.theta))
        self.forcey.append(-L*cos(self.theta)*self.omega**2-(-sin(self.theta)*g/L)*L*sin(self.theta))
    def harmonicForcex(self,coef=0.002,orig=150):
        self.forcex.append(-coef*(self.x-orig))
    def harmonicForcey(self,coef=0.002,orig=150):
        self.forcey.append(-coef*(self.y-orig))
    def gravForce(self,g=0.5):
        self.forcey.append(g)
    def buoyancy(self,vol=1,liq_den=1,g=0.5):
        self.forcey.append(-vol*liq_den*g)
    def viscous(self,visc=1):
        self.forcey.append(-visc*self.vy) 

class Circ(Rect):
    def __init__(self,r,clr,x,y):
        super().__init__(0,0,clr,x,y)
        self.r = r
    def wallCollision(self,width,height):
        if self.x+self.r>width or self.x-self.r<0:
            self.vx=-self.vx
        if self.y+self.r>height or self.y-self.r<0:
            self.vy=-self.vy
    
