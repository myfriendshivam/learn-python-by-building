#String
chai_type = "Ginger chai"
customer_name = "Priya"
print(f"Oder for {customer_name} : {chai_type} please!")

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[0:8:2]}")
print(f"Last word: {chai_description[12:]}")
print(f"reversing word: {chai_description[::-1]}")

label_text = "Chai Special 🐍"
print(f"Non Encoded label: {label_text}")

encoded_label = label_text.encode("utf-8")
print(f"Encoded label: {encoded_label}")

decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")