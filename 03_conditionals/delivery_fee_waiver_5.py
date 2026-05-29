#Delivery Fees Waiver System
order_amount = int(input("Enter the order amount: "))

print("Delivery cost is : 0") if order_amount > 300 else print("Delivery cost: 30")

# Age verification System

def verify_age(age_str: str) -> str:
    # Write your code here
    
    # Convert age to integer
    age = int(age_str)
    
    return "Access Granted" if age >= 18 else "Access Denied"