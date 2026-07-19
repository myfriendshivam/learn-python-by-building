# Raise your own errors

def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "elaichi"]:
        raise ValueError("Unsupported chai flavour...")
    print(f"brewing {flavor} chai...")


brew_chai("mint")

# Custom Exceptions
class OutOfIngredientsError(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Missing milk or sugar")
    print("Chai is ready...")

make_chai(0, 1)



# Mini Project with Exception Learning
class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("That chai not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        total = menu[flavor] * cups
        print(f"You bill for {cups} cups of {flavor} chai: rupees {total}")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thank you for visiting chaicode!")

bill("mint", 2)
bill("minmasalat", "two")
bill("ginger", 3)