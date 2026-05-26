# List (mutable)

ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients: {ingredients}")
ingredients.remove("water")
print(f"Ingredients: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]


chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")

chai_ingredients.insert(2, "black tea")

last_added = chai_ingredients.pop()
chai_ingredients.reverse()
chai_ingredients.sort()
print(f"chai: {chai_ingredients}")

sugar_levels = [1,2,3,4,5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

# Operator Overloading (adding operation doing more than one time it is overloading)

base_liquid = ["water", "milk"]
extra_flavour = ["ginger"]

full_liquid_mix = base_liquid + extra_flavour
print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ["black tea","water"] * 3
print(f"String brew: {strong_brew}")

#
raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA",b"card")
print(f"Bytes: {raw_spice_data}")