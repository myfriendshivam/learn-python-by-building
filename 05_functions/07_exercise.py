# Loyalty Points Tracker
loyalty_points = 0

def process_transactions(transactions: list[int]) -> int:
    # Write your code below this line
    def apply_bonus():
        nonlocal total
        if total > 1000:
            total += 50  # bonus for high spenders
 
    total = 0
 
    for amount in transactions:
        total += amount
 
    apply_bonus()
 
    # update global loyalty_points
    global loyalty_points
    loyalty_points += (total // 100)  # earn 1 point per ₹100
 
    return total
    
final = process_transactions([400, 700])
print(final)