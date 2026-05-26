# Building a Snack Suggestion System

snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! We'll serve you {snack}")
else:
    print("Sorry, we only serve cookies or samosa with chai")


# Restaurant Billing System
def get_delivery_offer(bill_amount: float) -> str:
    # Write your code below this line
    if bill_amount > 500:
        return "You get a free dessert!"
    else:
        return "No free dessert this time."
    pass