# Immutable(not changeable)
number=2
print(f"Initial number: {number}")

number=12
print(f"Second Initial number: {number}")

print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")

# Mutable(changeable)
spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")
print(f"{spice_mix}")

spice_mix.add("Ginger")
spice_mix.add("cardamon")
 
print(f"After spice mix id: {id(spice_mix)}")
print(f"{spice_mix}")
