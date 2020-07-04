global m
m = "morze.jpg"


class Obraz():
    def wyswietl(self,img):
        img = loadImage(m)
        image(img, width/2, height/2)
        
class Ramka():
    def wyswietl(self):
        noFill()
        strokeWeight(10)
        rect(width/2,height/2, 490, 383)
        
class Komunikat():
    def wyswietl(self):
        strokeWeight(0)
        fill(214, 235, 251)
        rect(width/2,height/2, 380, 100)
        fill(0, 0, 0)
        text("Plik nie istnieje, lub jego\nnazwa jest nieprawidlowa", width/2, height/2-10)
    

def setup():
    background(88, 112, 112)
    size(800, 700)
    textSize(20)
    textAlign(CENTER)
    imageMode(CENTER)
    rectMode(CENTER)
    obraz = Obraz()
    ramka = Ramka()
    komunikat = Komunikat()
    
    try:
        obraz.wyswietl(m) # sprawdeniepod kątem wyjątku powinno dotyczyć wyłąćznie sprawdzenia wczytanai i wyświetlenia obrazu
        
    except:
        komunikat.wyswietl()
        stroke(210, 25, 41)
        
    else:
        stroke(65, 155, 209)
        
    finally:
        ramka.wyswietl() # to robisz w obydwu wypadkach
        
#1,75pkt i plus za ładną oganizację kodu
        
