# Set ->  everything are to we unique

essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"clover", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"All spices: {common_spices}")

Only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices: {Only_in_essential}")

#memberShip test

print(f"Is 'cloves'in essential spices: {'cloves' in optional_spices }")

# Define unmodifiable essential items
essential_items = frozenset(["milk", "bread", "ketchup"])
print(essential_items)
 