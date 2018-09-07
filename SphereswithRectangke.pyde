g=0;
y=0;
dy=1;
def setup():
    size(800,600,P3D)    
def draw():
    background(255)
    pushMatrix()
    translate(200,300)
    global g
    rotate(radians(g))
    g=g+1                        #sphere which is rotating anticlock wise
    mouse()
    sphere(100)
    popMatrix()
    pushMatrix()
    translate(600,300)
    rotate(radians(-g)) 
    g=g+1
    mouse()
    sphere(100)                  #sphere which is rotating anticlock wise
    popMatrix()
    pushMatrix()
    global y,dy
    rect(400,y,15,45)            #rectangle which is moving along Y-axis
    y=(y+dy)%600;
    if y>height:
       dy=0;
    popMatrix()
def mouse():
    fill(random(150),random(255),random(0))      #color of spheres and rectangle
