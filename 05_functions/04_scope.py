# Scope and Named Space in Functions

#local - inside a function
# Enclosing from outer function if nested
# global - top level script
# Built in

def serve_chai():
    chai_type = "Masala" # local scope
    print(f"Inside function {chai_type}")

chai_type = "Lemon"
serve_chai()
print(f"Outer function: {chai_type}")

def chai_counter():
    chai_order = "lemon" # enclosing scope
    def print_order():
        chai_order = "Ginger"
        print("Inner: ", chai_order)
    print_order()
    print("Outer: ", chai_order)


chai_order = "Tulsi" # global
chai_counter()
print("Global: ", chai_order)
