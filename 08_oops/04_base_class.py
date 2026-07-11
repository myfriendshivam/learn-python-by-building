# Accessing Base class
# 1) Code Duplication

class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength
    
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level


# 2) Explicit call
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)
#         self.spice_level = spice_level

# 3) super()
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level



# Method Resolution Order(MRO)
class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala blend"

class C(A):
    label = "C: Herbal blend"

# class D(B, C):  # O/P --> B: Masala blend
#     pass

class D(C, B):  # O/P --> C: Herbal blend
    pass

cup = D()
print(cup.label)
print(D.__mro__)


# Static Methods -> It is helpful when you want utility functions grouped with your classes with dependeing on any instance.

class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    
raw = " water  , milk , ginger , honey "

# obj = ChaiUtils()
# obj.clean_ingredients(raw)

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)


# Classmethod vs Staticmethod
# class receives argument but static receives no automatic first argument
# class operate on the class, not instance but static utility function related to the class
# class access to cls but static never access cls
# class and static never access to self
class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size
    
    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"]
        )
    
    @classmethod
    def from_string(cls, order_srting):
        tea_type, sweetness, size = order_srting.split("-")
        return cls(tea_type, sweetness, size)
    
class ChaiUtility:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]
    
print(ChaiUtility.is_valid_size("Medium"))

order1 = ChaiOrder.from_dict({"tea_type": "masala", "sweetness": "medium", "size": "Large"})

order2 = ChaiOrder.from_dict("Ginger-Low-Small")

order3 = ChaiOrder("Large", "Low", "Large")

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)
                             

# Property Decorator - Getter and Setter
class TeaLeaf:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")

leaf = TeaLeaf(2)
print(leaf.age)
leaf.age = 4
print(leaf.age)

