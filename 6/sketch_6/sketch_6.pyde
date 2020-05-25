class Kwadrat():
    def __init__(self, bok):
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class PasiastyKwadrat(Kwadrat):
    def sketchPasiasty(self, x, y, paski):
        Kwadrat.sketch(self, x, y)
        space = self.bok/paski
        _xLinii_ = 0
        for pasek in range(0, paski):
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
            
class KolorowyKwadrat(Kwadrat):
    def sketchKolorowy(self, x, y, r, g, b):
        fill(r, g, b)
        Kwadrat.sketch(self, x, y)
        
            
def setup():
    size(500, 500)
    malyKwadrat = Kwadrat(50.0)
    malyKwadrat.sketch(200, 300)
    duzyKwadrat = Kwadrat(200.0)
    duzyKwadrat.sketch(50, 75)
    malyPasiastyKwadrat = PasiastyKwadrat(30.0)
    malyPasiastyKwadrat.sketchPasiasty(300, 300, 5)
    malykolorowyKwadrat = KolorowyKwadrat(50.0)
    malykolorowyKwadrat.sketchKolorowy(250,250,255,51,0)
    duzykolorowyKwadrat = KolorowyKwadrat(70.0)
    duzykolorowyKwadrat.sketchKolorowy(330,330,0, 51, 204)
