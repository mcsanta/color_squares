# this program creates an array of squares
# which slowly switch their color

# squares are assigned a color1 and a color2 and slowly fade from 1 to 2
# once complete, color1 becomes color2 and color2 is newly choosen
# the timeframe for each square is random and independent from all other squares
# colors are choosen from a 'nice red' color space

from random import *
from square import *

sqq = 16 # number of squares per row and col

def setup():
    size(640,640) # size of canvas
    noStroke() # dont outline the squares
    
    # use HSB color mode
    colorMode(HSB, 360, 100, 100)
    
    # variable 'squares' needs to be a global variable
    global squares
    
    # make 2D-array of squares
    squares = [[square(x*width/sqq, y*height/sqq, width/sqq) for x in range(sqq)] for y in range(sqq)]
    
    #frameRate()
    
def draw():
    global squares
    
    # store ampere usage of LEDs
    amps = 0
    
    for row in range(sqq):
        for col in range(sqq):
            squares[row][col].update() # call update function
            
            # do calculation for estimatet ampere usage for LEDs
            amps+= red(squares[row][col].colorCur)/360*255/16
            amps+= green(squares[row][col].colorCur)/100*255/16
            amps+= blue(squares[row][col].colorCur)/100*255/16
            
            squares[row][col].show() #show squares on canvas

    textSize(11)
    fill(0,0,0)
    textAlign(LEFT)
    text("Ampere usage: " + nf(amps/1000,0,2), 10, height-10)
    textAlign(RIGHT)
    text("FPS: " + nf(frameRate,0,-1), width-10, height-10)
    
    text