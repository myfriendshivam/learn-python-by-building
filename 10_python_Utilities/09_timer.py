# Set a Counterdown Timer

import time

while True:
    try:
        seconds = int(input("Enter the time in second: "))
        if seconds < 1:
            print("Please enter a number greater than 0")
            continue
        break
    except ValueError:
        print("Invalid input, please entera whole number")

print("\n🔔 Timer started...")
for remaining in range(seconds, -1, -1):
    mins, secs = divmod(remaining, 60)
    time_format = f"{mins:02d}:{secs:02d}"
    print(f"⏰ Time left: {time_format}",end="\r", flush=True)
    time.sleep(1)

print("\n Time's up! Take a break or move on to next task.")
# print("\a") # optimal; makes a beep sound
