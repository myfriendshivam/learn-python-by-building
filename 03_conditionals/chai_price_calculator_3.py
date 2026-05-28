# Building a Chai Price Calculator
cup = input("Choose your cup size(small/medium/large): ").lower()
if cup == "small":
    print("Price is 10 rupees")
elif cup == "medium":
    print("Price is 15 rupees")
elif cup == "large":
    print("Price is 20 rupees")
else:
    print("Unknown cup size")


# Delivery Charge Calculator
def calculater_delivery_charge(distance: float) -> str:
    if distance <= 2:
        return "Delivery charge: 0"
    elif distance <= 5:
        return "Delivery charge: 30"
    elif distance <= 10:
        return "Delivery charge: 50"
    else:
        return "Delivery not available for your location."