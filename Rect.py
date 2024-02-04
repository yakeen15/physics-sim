
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
        self.forcex = []
        self.forcey = []
    def update(self,dt):
        self.netforcex()
        self.netforcey()
        self.x = self.x+self.vx*dt
        self.y = self.y+self.vy*dt
        self.vx = self.vx+self.ax*dt
        self.vy = self.vy+self.ay*dt
    def wallCollision(self,width,height):
        if self.x+self.wd>width or self.x<0:
            self.vx=-self.vx
        if self.y+self.ht>height or self.y<0:
            self.vy=-self.vy
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