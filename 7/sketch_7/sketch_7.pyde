from abc import ABCMeta, abstractmethod
class Pet():
    __metaclass__=ABCMeta
    @abstractmethod
    def speak(self):
        super().__init__()
        return 'no sound'
class Cat(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('meow', random(50, width-70), random(50, height-50))
        return 'meow'
    def __sub__(self, other):
        return self.name + other.name[::-4]
class Dog(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('woof', random(50, width-70), random(50, height-50))
        return 'woof'
    def gimmePaw(self):
        image(loadImage("lapa.png"), random(50, width-70), random(50, height-100))
    def __add__(self, other):
        return self.name[0]+ ' i ' + other.name[0]
class Bunny(Pet):
    pass
class Giraffe(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('mlask', random(50, width-70), random(50, height-50))
        return 'mlask'
    
def setup():
    size(400,400)
    textSize(20)
    rex = Dog('Rex')
    benio = Dog('Benio')
    skrypcik = Cat('Skrypcik')
    magdalena = Giraffe('Magdalena')
    samuel = Cat('Samuel')
    global list_of_pets
    list_of_pets = [rex, benio, skrypcik, magdalena, samuel] 
    print(isinstance(skrypcik, Pet))
    print(rex+benio)
    print(samuel-skrypcik)

def draw():
    pass
    
def mouseClicked():
    for pet in list_of_pets:
        pet.speak()
        if isinstance(pet, Dog):
            pet.gimmePaw()
