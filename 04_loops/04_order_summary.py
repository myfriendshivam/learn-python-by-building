# Zip can Combine list
names = ["Shivam", "Meera", "Sam"]
bills  = [40, 70, 100]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")


# Student Scores Report
def generate_score_report(names: list[str], scores: list[int]) -> list[str]:
    # Write your code below this line
    report = []
    for name, score in zip(names, scores):
        report.append(f"{name} scored {score} marks")
    return report