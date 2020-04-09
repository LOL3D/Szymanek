def setup():
    size(480,480)
    rectMode(CORNER)
    frameRate(60)
    global kolory
    kolory = {"niebieski":(65,105,225,90), "zielony":(46,139,87,90), "czerwony":(255,69,0), "żółty":(255,255,0)}
    global lista_kolorow
    lista_kolorow = []
    for nazwa, rgb in kolory.items():
        lista_kolorow.append(rgb)
    global klatka
    klatka=0
    
    global x, y, kierunek_x, kierunek_y
    x=240
    y=480
    kierunek_x = 5
    kierunek_y = 5
    
def draw():
    background(70)
    global x, y, kierunek_x, kierunek_y, klatka
    
    x += kierunek_x 
    if x > width or x < 0:
        kierunek_x *= -1
        klatka += 1
        
        
    y += kierunek_y
    if y > height or y<0:
        kierunek_y *= -1
        klatka += 1
        
    fill(*lista_kolorow[klatka%len(lista_kolorow)])
    circle(x, y, 100) 
    
    fill(178,34,34)
    square (0,0,50)

    
    line(2,2,48,48)
    line(48,2, 2, 48)
    
    
    if mouseY > 0 and mouseY< 50 and mouseX > 0 and mouseX < 50:
        if mousePressed and (mouseButton == LEFT):
            exit() 

    
