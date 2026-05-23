class Chai:
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level
    
    def sip(self):
        print("Sipping chai")
    
    def add_sugar(self, amount):
        print("added the sugar",amount)

my_chai = Chai(sweetness=2, milk_level=3)
my_chai.add_sugar(3)