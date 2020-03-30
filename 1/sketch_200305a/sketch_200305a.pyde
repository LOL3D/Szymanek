def setup():
    size(720,480)
def draw():
    if mousePressed:
        circle(mouseX, height/2, 100)
        c = color(30,144,255)
        fill(c)
    else:
        clear()
