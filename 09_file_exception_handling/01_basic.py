
# Exception handling

# handle  ->  a milk spil missing ingredient brew step

orders = ["masala", "ginger"]
print(orders[2])  
# IndexError
#KeyError
# ZeroDivisionError
# TypeError
# NameError


# Try Except
chai_menu = {"masala": 30, "ginger": 40}

try:
    chai_menu["elaichi"]
except KeyError:
    print("The key you are tying to access does not exists")

print("Hello chai code")


# 
def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("We don't know that flavor")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavor} chai is served")
    finally:
        print("Next customer please")

serve_chai("masala")
serve_chai("unknown")


# Catching Multiple Exceptions
def process_order(item: str, quantity: int):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("Quantity must be in number")

process_order("ginger", 2)
process_order("masala", "two")
process_order("masala", 4)