# List  [expression for item in iterable if condition]

menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Chai"
]

iced_tea = [tea for tea in menu if "Iced" in tea]
new_iced_tea = [my_tea for my_tea in menu if len(my_tea)>12]

print(iced_tea)
print(new_iced_tea)

# Set { expression for item in iterable if condition }
favourite_chais = [
    "Masala Chai",
    "Green Tea",
    "Masala Chai",
    "Lemon Tea",
    "Green Tea",
    "Elaichai Chai"
]

# unique one -> used set
unique_chai = {chai for chai in favourite_chais}
new_unique_chai = {chai for chai in favourite_chais if len(chai)>8}

print(unique_chai)

recipes = {
    "Masala Chai": ["ginger", "cardamom", "clover"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clover"]
}

unique_spices = { spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)

# Dictonary {expression for item in iterable if condition}
# key: value
tea_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}

tea_prices_used = {tea:price / 80  for tea, price in tea_prices_inr.items()}
print(tea_prices_used)

# Generator (expression for item in iterable if condition)
# used only for saving the memory
# [x for x in items] -> make entire list in memory
# (x for x in items) -> like a stream

dealy_sales = [5, 10, 12 ,7 ,3 ,8, 9, 15]
total_cups = sum(sale for sale in dealy_sales if sale > 5)

total_cups = [sale for sale in dealy_sales if sale > 5]
print(total_cups)
