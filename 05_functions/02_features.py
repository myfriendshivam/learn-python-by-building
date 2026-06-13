# Hiding Implementation Details

def get_input():
    print("Getting user input")

def validating_input():
    print("Validating the user info")

def save_to_db():
    print("saving  to database")

def register_user():
    get_input()
    validating_input()
    save_to_db()
    print("User register compete")

register_user()


# Improving the Readability

def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

my_bill = calculate_bill(3, 15)
print(my_bill)

print("rder for table 2: ", calculate_bill(4, 16))

# Improving Traceability

def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/ 100

orders = [100, 150, 200]
for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Original: {price}, Final with VAT: {final_amount}")