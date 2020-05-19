class Kwadrat(): # trochę mało orygnalny pomysł xD
    def __init__(self, kolor, xpoz, ypoz, szybkosc):
        self.kolor = kolor
        self.xpoz = xpoz
        self.ypoz = ypoz
        self.szybkosc = szybkosc

    def rysuj(self): # metody to czynności, jeśli się tego trzymamy, kod sięlepiej później czyta i jest logiczniejszy
        stroke(50)
        fill(self.kolor)
        square(self.xpoz, self.ypoz, 50);

    def rusz(self):
        self.ypoz = self.ypoz + self.szybkosc;
        if self.ypoz > height:
            self.ypoz = 0

def setup():
    size(100,600) # po co szerzej? ;P
    kwadrat_1 = Kwadrat(color(255, 69, 0), 50, 100, 2) # powinny się znaleźć w setupie, by mieć pewność, że będą utwozone na początku programu
    kwadrat_2 = Kwadrat(color(75, 0, 130), 0, 300, 1)
    global kwadraty
    kwadraty = (kwadrat_1, kwadrat_2) # przy większej ilości obiektów warto je zagregować w kolekcję

def draw(): 
  background(70)
  for kwadrat in kwadraty:
      kwadrat.rusz()
      kwadrat.rysuj()
      
#2pkt
