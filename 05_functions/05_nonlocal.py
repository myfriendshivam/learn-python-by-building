# Non local and Global scopes
chai_type  = "Ginger"

def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type # access the chai_type variable in this scope
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update", chai_type)

update_order()