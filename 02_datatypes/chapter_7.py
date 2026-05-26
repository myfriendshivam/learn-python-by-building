# Dictionary []

chai_order = dict(type="Masala Chi", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

chai_recipe = {} # empty dictionary
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")

print(f"chai recipe: {chai_recipe}")
del chai_recipe["liquid"]
print(f"chai recipe: {chai_recipe}")

# MemberShip testing
print(f"Is sugar in the order? {'sugar' in chai_order}")

chai_order = {"type": "Ginger Chi", "size": "Large", "sugar": 2}
print(f"Order details (keys): {chai_order.keys()}")
print(f"Order details (values): {chai_order.values()}")
print(f"Order details (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"Updated chai recipe: {chai_recipe}")

chai_size = chai_order["size"]
chai_size = chai_order["customer_note"] # not in dictionary
print(f"Chai size is: {chai_size}")

customer_note = chai_order.get("size", "No Note")
print(f"Customer note is: {customer_note}")


