# Handle Multiple return 

def make_chai():
    # return "Here is your masala chai"
    print("Here is your masala chai")

# print(make_chai())

return_vale = make_chai()
print(return_vale)

# Nothing -> implicitly return None
# one value   
def idle_chaiwala():
    pass

print(idle_chaiwala())

def sold_cups():
    return 120
total = sold_cups()
print(total)

# early from a function
def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "Chai is ready"
    print("chai")

print(chai_status(0))
print(chai_status(5))

# muliple value 
def chai_report():
    return 100, 20, 10 # sold, remaining

sold, remaining, _ = chai_report()
print("Sold: ", sold)
print("Remaining: ", remaining)