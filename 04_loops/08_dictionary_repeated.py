# Using Dictionaries instead of Reapeated Cases

users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80, "coupon": "P50"},
]

discounts = {
    "P20": (0.2, 0),
    "F10": (0.5, 0),
    "P50": (0, 10),
}

for user in users:
    precent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = (user["total"]*precent) + fixed
    print(f"id: {user["id"]} paid {user["total"]} and got discount for next visit of rupees {discount}")
