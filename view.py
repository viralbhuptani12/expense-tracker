total = 0.0
by_category = {}

with open("expenses.txt", "r") as f:
    for line in f:
        parts =(line.strip()).split(" | ")
        category = parts[1]
        amount = float(parts[2])
        total = total + amount
        if category in by_category:
            by_category[category] = by_category[category] + amount
        else:
            by_category[category] = amount
    
print(f"\n Total spent = ₹{total:.2f} \n")
print("Where did you spend: ")
for category in by_category:
    print(f" {category}: ₹{by_category[category]:.2f}")