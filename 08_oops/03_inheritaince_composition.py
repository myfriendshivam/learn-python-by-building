# Inheritance and Composition in Python
class BaseChai:
    def __init__(self, type_):
        self.type = type_
    
    def prepare(self):
        print(f"Preparing {self.type} chai....")

class MasalaChai(BaseChai):   # inheritance
    def add_spices(self):
        print(f"Adding cardamom, ginger, cloves.")

class ChaiShop:        
    chai_cls = BaseChai   # compisition

    def __init__(self):
        self.chai = self.chai_cls("Regular")
    
    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
# fancy.chai_cls.add_spices()   -> this will not work
fancy.chai.add_spices()
