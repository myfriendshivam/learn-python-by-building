# Integer

black_tea_grams = 14
ginger_grams = 3

total_grams= black_tea_grams + ginger_grams
print(f"Total grams of base tea is {total_grams}")

remaing_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaining tea is {remaing_tea}")

milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving is {milk_litres}")

total_tea_bags = 7
pots = 4 
bags_per_pot = total_tea_bags // pots
print(f"While tea bags per pot {bags_per_pot}")

total_cadamon_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamon_pods % pods_per_cup
print(f"Leftover C pods {leftover_pods}")

base_flavour_strength = 2
scale_factor = 3
powerful_falvous = base_flavour_strength ** scale_factor
print(f"Scaled flavous strenth {powerful_falvous}")

total_tea_leaves_harvested = 1_000_000_000
print(f"tea leaves: {total_tea_leaves_harvested}")

#Boolean
is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling #upcasting
print(f"Total actions: {total_actions}")

milk_present = 0 #no milk
print(f"Is there milk? {bool(milk_present)}")

#logical operation -> and, or, not
# tea or coffee -> any one can be true
# tea and cookies -> both should be true

water_hot = True
tea_added = False
can_server = water_hot and tea_added
print(f"Can serve chai? {can_server}")

#Real number (floating)
import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.5
current_temp = 95.499999999
print(f"Ideal temp {ideal_temp}")
print(f"Current temp {current_temp}")
print(f"Difference temp {ideal_temp - current_temp}")
print(sys.float_info)