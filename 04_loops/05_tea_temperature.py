# While Loop

temperature = 40
while temperature < 100:
    print(f"Current temperature: {temperature}")
    temperature = temperature + 15  # temperature += 15

print("Tea is ready to boil")

# ATM Withdrawal Simulator
def simulate_atm_withdrawals(balance: int, withdrawals: list[int]) -> list[str]:
    # Write your code below this line
    message = []
    index = 0
    
    while index < len(withdrawals):
        amount = withdrawals[index]
        
        if amount <= balance:
            balance = balance - amount
            message.append(f"Withdrawn: {amount}")
        else:
            message.append(f"Insufficient funds for requested amount: {amount}")
        index = index + 1
    
    message.append(f"Remaining Balance: {balance}")
    return message