# Friendship Compatibility Calculator

def friendship_score(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    score = 0
    shared_letters = set(name1) & set(name2)
    vowels = set('aeiou')

    score += len(shared_letters) * 5
    score += len(vowels & shared_letters) * 10

    return min(score, 100)

def run_frendship_calculator():
    print("Friendship Compatibility Calculator")
    name1 = input("Enter first name: ")
    name2 = input("Enter second name: ")

    score = friendship_score(name1, name2)

    print(f"\n {score}")
    
    if score > 80:
        print("Very good! You two are practically inseparable best friends! 🌟")
    elif score > 50:
        print("Good! You have a solid bond with great chemistry! 😊")
    else:
        print("Poor! You might need to spend a bit more time getting to know each other. 🤝")

run_frendship_calculator()