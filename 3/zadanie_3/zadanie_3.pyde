def setup():
    size(750,750)
    rectMode(CORNER)
    frameRate(60)
    textSize(200)
    global odznaczenie, zaznaczenie, klikniete
    odznaczenie = (0,0,0)
    zaznaczenie = (178,34,34) # czasem tak dla czytelności i ułatwienia warto stworzyć zmienną, wtedy też zmianą w jednym miejscu można łątwo zmienić kolor wszędzie
    klikniete = False
def draw():
    background(70)
    global klikniete
    fill(*odznaczenie)
    text("P", width/2-115, height/2+60)
    text("S", width/2, height/2+60)
    
    if  mouseX > width/2-100 and mouseX < width/2 and mouseY > height/2-90 and mouseY< height/2+70:
        fill(*zaznaczenie)
        text("P", width/2-115, height/2+60)
        if keyPressed and key == CODED and keyCode == 39:
            fill(*odznaczenie)
            text("P", width/2-115, height/2+60)
            fill(*zaznaczenie)
            text("S", width/2, height/2+60)
            
    if  mouseX > width/2 and mouseX < width/2+100 and mouseY > height/2-90 and mouseY< height/2+70:
        fill(*zaznaczenie)
        text("S", width/2, height/2+60)
        if keyPressed and key == CODED and keyCode == 37:
            fill(*odznaczenie)
            text("S", width/2, height/2+60)
            fill(*zaznaczenie)
            text("P", width/2-115, height/2+60)
    
    print(key)
    
    print(keyCode)
    
    if keyPressed: # czasem lepiej rozdzielić warunki, niż powtarzać jeden kilkukrotnie - w końcu obowiązuje w całym wytabowanym bloku
        if key == 'p' or key == 'P':
            fill(*zaznaczenie)
            text("P", width/2-115, height/2+60)
            
        if key == 's' or key == 'S':
            fill(*zaznaczenie)
            text("S", width/2, height/2+60)
        
        if klikniete:
            if keyCode == 39:
                fill(*odznaczenie)
                text("P", width/2-115, height/2+60)
                fill(*zaznaczenie)
                text("S", width/2, height/2+60)
            if keyCode == 37:
                fill(*odznaczenie)
                text("S", width/2, height/2+60)
                fill(*zaznaczenie)
                text("P", width/2-115, height/2+60)
            
        klikniete = True # to było trochę tricky, bo w jednej klatce szczytuje tylko jeden klawisz, więc trzeba było zapamiętać czy klatkę temu był wciśnięty
    else:
        klikniete=False
            
    o = createShape()
    o.beginShape()
    o.fill(255,140,0)
    o.stroke(255,140,0)
    o.vertex(0, height)
    o.vertex(width/2+50, height)
    o.vertex(width/2+100, height/2+100)
    o.vertex(width/2-100, height/2+100)
    o.vertex(width/2+20, height/2+110)
    o.endShape(CLOSE)
    shape(o)
    
    
    fill(178,34,34)
    square (0,0,50)
    
    line(2,2,48,48)
    line(48,2, 2, 48)
    
    
    if mouseY > 0 and mouseY< 50 and mouseX > 0 and mouseX < 50:
        if mousePressed and (mouseButton == LEFT):
            exit() 

# 2pkt
