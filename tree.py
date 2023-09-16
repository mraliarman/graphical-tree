import stddraw
import math
stddraw.setPenColor(stddraw.brown)
def tree(n, x0, y0, height, angle = 0, pen = 0.005):
    if n == 0: return 0
    stddraw.setPenRadius(pen)

    y1 = math.sqrt(math.pow(height / 2, 2) - math.pow(height / 4, 2)) + y0   
    y2 = math.sqrt(math.pow(height / 2, 2) - math.pow(height / 4, 2)) + y0   
    y3 = math.sqrt(math.pow(height / 2, 2) - math.pow(height / 4, 2)) / 2 + y0
       
    x1, y1 = ( (height * 0.2)*math.cos(math.radians(angle-5))-(y1-y0)*math.sin(math.radians(angle-5)) + x0 , (height * 0.2)*math.sin(math.radians(angle-5))+(y1-y0)*math.cos(math.radians(angle-5))+y0)   
    x2, y2 = ( (- height * 0.3)*math.cos(math.radians(angle+30))-(y2-y0)*math.sin(math.radians(angle+30))+x0 , (- height * 0.3)*math.sin(math.radians(angle+30))+(y2-y0)*math.cos(math.radians(angle+30))+y0)
    x3, y3 = ( -(y3-y0)*math.sin(math.radians(angle+15))+x0 , +(y3-y0)*math.cos(math.radians(angle+15))+y0)  

    stddraw.line(x0, y0, x1, y1)
    stddraw.line(x0, y0, x2, y2)
    stddraw.line(x0, y0, x3, y3)
    stddraw.setPenColor(stddraw.BLUE)
    tree(n - 1, x1, y1, height * 0.7, angle - 20, pen - 0.0005)
    stddraw.setPenColor(stddraw.RED)
    tree(n - 1, x2, y2, height * 0.7, angle + 60, pen - 0.0005)
    stddraw.setPenColor(stddraw.brown)
    tree(n - 1, x3, y3, math.sqrt(math.pow(height / 2, 2) - math.pow(height / 4, 2)) * 0.7, angle + 30, pen - 0.0005)

stddraw.setXscale(0, 1)
stddraw.setYscale(0, 1)
stddraw.setPenRadius(0.01)
stddraw.line(0.5, 0, 0.5, 0.25)
stddraw.setPenColor(stddraw.brown)
tree(10, 0.5, 0.25,  0.25)
stddraw.show()