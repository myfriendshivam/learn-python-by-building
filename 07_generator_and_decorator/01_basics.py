# Generators and Decorators in Python

# Generators
# you save memory
# you dont want the results immedietely
# lazy evaluation
# yield as a keyword
# yield pauses and resumes the function

def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"


stall = serve_chai()
for cup in stall:
    print(cup)

def get_chai_list():
    return ["Cup 1", "Cup 2","Cup 3"]

# generator function
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()
print(chai) # Only referance

print(next(chai)) # first value of generator
print(next(chai))
print(next(chai))
print(next(chai))  # gives error


# Infinite Generators in Python -  usefull for the real time system where we constantly updating the value

def infinite_chai():
    count = 1
    while True:
        yield f"Refile #{count}"
        count += 1

refile = infinite_chai()
user2 = infinite_chai()

for _ in range(3):
    print(next(refile))

for _ in range(5):
    print(next(refile))


# Send value to Generators
def chai_customer():
    print("Welcome! What chai would you like ?")
    order = yield 
    while True:
        print(f"Preparing: {order}")
        order = yield

chai_stall = chai_customer()
next(chai_stall) # Start the generator
chai_stall.send("Masala Chai") # this send directly interact with generator
chai_stall.send("Lemon Chai")


# Yield from and Close the Generators
# close() -> it stops the generator from running further 

def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)


def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("Stall closed, No more chai")
    
stall__2 = chai_stall()
print(next(stall__2))
stall__2.close()   # cleanup memory

