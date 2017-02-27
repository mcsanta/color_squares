from random import *

class square(object):
    def __init__(self, x, y, d): # create square at (x,y) with lenght d
        self.x = x
        self.y = y
        self.d = d
        
        # assign color2 then call reset function
        self.color2 = niceColor() # needs to be set, when calling reset()
        self.reset(1)
    
    def reset(self, first): # is called on creation, and when time frame expired (color1 reached color2)
        
        # transfer color2 on color1 and chose new target color (color2)
        self.color1 = self.color2
        self.color2 = niceColor()
        
        # pick timeframe (tMax) and reset timekeeper (t)
        
        # on first iteration, the timeframe needs to be offset to prevent pulsing
        self.tMax = random() * 200 *first + pow(random(), 1/3) * 200
        self.t = 0
        
    def update(self):
        # slowly go from color1 to color2
        
        # get hue values
        h1 = hue(self.color1)
        h2 = hue(self.color2)
        
        # this calculation is done so the transition works for red colors
        # it is easier fading between (-40,30) than (320,30) and having to keep track of the color circle
        # also, we DO NOT want to fade (30,320) and get all the colors inbetween
        if abs(h1-h2) > 180:
            if h1 > h2:
                h1 -= 360
            else:
                h2 -= 360
                
        # get new values for h, s, b by maping the t value onto the range 
        h = (int(map(self.t, 0, self.tMax, h1, h2)) + 360 ) % 360
        s = int(map(self.t, 0, self.tMax, saturation(self.color1), saturation(self.color2)))
        b = int(map(self.t, 0, self.tMax, brightness(self.color1), brightness(self.color2)))
        
        # set new color
        self.colorCur = color(h,s,b)
        
        # increment time
        self.t += 1
        
        # if time exceeds tMax, then call reset
        if self.t > self.tMax:
            self.reset(0)
        
        
    def show(self):
        
        # set color and draw the square
        fill(self.colorCur)
        rect(self.x, self.y, self.d, self.d)
    
def niceColor():
    # choose a 'nice' color
    
    h = randint(-26,18) # red
    if h < 0:
        h += 360
    s = randint(20,100)
    b = randint(int(map(s,20,100,100,50)), 100) # minimum brightness is dependend on saturation
    return color(h,s,b)