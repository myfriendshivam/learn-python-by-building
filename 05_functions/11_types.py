# Types of Function

# pure vs impure
def pure_chai(cups):
    return cups * 10

total_chai = 0

# not recommended way
def impure_chai(cups):
    global total_chai
    total_chai +=cups

# Recursive functions
def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1)

print(pour_chai(3))

# Lambdas(Anonymous function)
chai_types = ["light", "kadak", "ginegr", "kadak"]
strong_chai = list(filter(lambda chai: chai=="kadak", chai_types))

strong_chai = list(filter(lambda chai: chai!="kadak", chai_types))
print(strong_chai)
