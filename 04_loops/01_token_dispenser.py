# Tea Token Dispenser
for token in range(1, 11):
    print("Serving chai to token #{token}")


# Batch Chai Preparation
for batch in range(1, 5):
    print(f"Preparing chai fro batch #{batch}")



# Generate Multiplication Table
def multiplication_table(number: int) -> list[str]:
    table = []
    for i in range(1, 11):
        result = number * i
        table.append(f"{number} x {i} = {result}")
    return table

