# Break, Continue and Loop fallback

flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour  == "Out of Stock":
        continue
    if flavour == "Discontinued":
        break
    print("{flavour} item found")

print(f"Out side of loop")


# for else -> fall back
staff = [("Amit", 16), ("Zara", 17), ("Raj", 15)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print(f"No one is eligible to manage the staff")


# Parcel Scanning System
def scan_parcels(parcel_codes: list[str]) -> list[str]:
    # Write your code below this line
    logs = []
    for code in parcel_codes:
        if code == "DAMAGED":
            logs.append("Skipped damaged parcel")
            continue
        if code == "STOP":
            logs.append("Critical error: Stopping scan")
            break
        logs.append(f"Scanned parcel: {code}")
    else:
        logs.append("All parcels scanned successfully")
    return logs