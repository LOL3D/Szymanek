add_library('pdf')
def setup():
    size(500, 600)
    textSize(11)
    global ana
    global was
    global oksy
    global razem
    global p1
    ana = loadImage("Ana.png") 
    was = loadImage("was.png") # korzystniej byłoby, gdyby była wczytana grafika z samym wąśem ,nie z nałożonym już na zdjęcie - to miał robić program
    oksy = loadImage("oksy.png") # zwłąszcza, że testuję na swoim zdjęciu by sprawdzić, jak radzicie sobie z inną rozdzielczością i czasem proporcją niż wybrana przez was
    razem = loadImage("razem.png") # w poleceniu było "Program ma wczytać dowolne standardowe zdjęcie dokumentowe", tu narzucasz zastąpieniem przez swoje
    p1 = 0
    
def draw():
    global ana
    global was
    global oksy
    global razem
    global p1
    
    
    def ui():
        fill(178,34,34)
        square (0,0,50)
        fill(30,144,255)
        rect (width/2+150, height/2-80, 60, 50, 5)
        fill(30,144,255)
        rect (width/2-210, height/2-80, 60, 50, 5)
        fill(30,144,255)
        rect (width/2+150, height/2+40, 60, 50, 5)
        fill(30,144,255)
        rect (width/2-210, height/2+40, 60, 50, 5)
        line(2,2,48,48)
        line(48,2, 2, 48)
        fill(0,0,0)
        text("Moustache", width/2-208, height/2-50)
        text("Wszystko", width/2-206, height/2+70)
        text("Okulary", width/2+158, height/2-50)
        text("Nic", width/2+171, height/2+70)
    
    background(70)
    image(ana, width/2-125,height/2-150, width/2, height/2)
    ui()        
            
    if mouseY > height/2-80 and mouseY< height/2-20 and mouseX > width/2-210 and mouseX < width/2-150:
        if mousePressed and (mouseButton == LEFT):
            p1 = 1
                
    if mouseY > height/2-80 and mouseY< height/2-20 and mouseX > width/2+150 and mouseX < width/2+210:
        if mousePressed and (mouseButton == LEFT):
            p1 = 2
            
    if mouseY > height/2+40 and mouseY< height/2+100 and mouseX > width/2-210 and mouseX < width/2-150:
        if mousePressed and (mouseButton == LEFT):
            p1 = 3
            
    if mouseY > height/2+40 and mouseY< height/2+100 and mouseX > width/2+150 and mouseX < width/2+210:
        if mousePressed and (mouseButton == LEFT):
            p1 = 4
            
            
    if p1 == 1:
        beginRecord(PDF, "skan.pdf")
        background(70)
        image(was, 0, 0, width, height)
        endRecord()
        background(70)
        image(was, width/2-125,height/2-150, width/2, height/2)
        ui()
    
    if p1 == 2:
        beginRecord(PDF, "skan.pdf")
        background(70)
        image(oksy, 0, 0, width, height)
        endRecord()
        background(70)
        image(oksy, width/2-125,height/2-150, width/2, height/2)
        ui()
        
    if p1 == 3:
        beginRecord(PDF, "skan.pdf")
        background(70)
        image(razem, 0, 0, width, height)
        endRecord()
        background(70)
        image(razem, width/2-125,height/2-150, width/2, height/2)
        ui()
        
    if p1 == 4:
        beginRecord(PDF, "skan.pdf")
        background(70)
        image(ana, 0, 0, width, height)
        endRecord()
        background(70)
        image(ana, width/2-125,height/2-150, width/2, height/2)
        ui()
        
    if mouseY > 0 and mouseY< 50 and mouseX > 0 and mouseX < 50:
        if mousePressed and (mouseButton == LEFT):
            exit()
                                
# przekombinowane, ale wczytywać obrazki i zapisywać pdfy umiesz ;)
# 1,75p
            
    

    
