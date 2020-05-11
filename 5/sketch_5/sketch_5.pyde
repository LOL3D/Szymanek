class Kwadrat():
    def __init__(self, kolor, xpoz, ypoz, szybkosc):
        self.kolor = kolor
        self.xpoz = xpoz
        self.ypoz = ypoz
        self.szybkosc = szybkosc

    def kwadrat(self):
        stroke(50)
        fill(self.kolor)
        square(self.xpoz, self.ypoz, 50);

    def ruch(self):
        self.ypoz = self.ypoz + self.szybkosc;
        if self.ypoz > height:
            self.ypoz = 0

kwadrat_1 = Kwadrat(color(255, 69, 0), 50, 100, 2)
kwadrat_2 = Kwadrat(color(75, 0, 130), 0, 300, 1)

def setup():
    size(600,600)

def draw(): 
  background(70)
  kwadrat_1.ruch()
  kwadrat_1.kwadrat()
  kwadrat_2.ruch()
  kwadrat_2.kwadrat()
