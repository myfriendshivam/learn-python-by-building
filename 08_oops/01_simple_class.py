# Object Oriented Programming in Python
# <class 'type'>   ---> object

class  Chai: 
    pass

class ChaiTime:
    pass

print(type(Chai))

ginger_tea = Chai()   # object
print(type(ginger_tea))
print(type(ginger_tea) is Chai)
print(type(ginger_tea) is ChaiTime)


# Class and Object Namespace
class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)

# Creating objects from class Chai
masala = Chai()
print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")
masala.is_hot = False

print("Class: ",Chai.is_hot)
print(f"Masala {masala.is_hot}")

masala.flavor = "Masala"
print(masala.flavor)


# Attribute Shadowing
class Chai:
    temperature = "hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"
print("After changing ", cutting.temperature)
print("Cup size is ", cutting.cup)
print("Direct look into the class ", Chai.temperature)

del cutting.temperature
del cutting.cup

print(cutting.temperature)
print(cutting.cup)    # it gives error -> Chai object has no cup attribute


# Self argument
class Chaicup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size}ml chai cup"

cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))

cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two))

# Constructors and Init
# initiate the object and the way define it is through reserved method constructor
# init create constr. or constr. create init

class Chaiorder:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size
    
    def summary(self):
        return f"{self.size}ml of {self.type} chai"
    
order =  Chaiorder("Masala", 200)
print(order.summary())

order_two = Chaiorder("Ginger", 220)
print(order_two.summary())

