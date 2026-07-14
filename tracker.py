from datetime import datetime
def add_expense():
    try:
        amount = float(input("How much did you spend today? ₹ "))
    except ValueError:
        amount = float(input("Please enter the value in numbers ₹ "))

    category = input("Category(food, transport, bills): ").lower()
    description = input("What was it for? ")
    today = datetime.now().strftime("%Y-%m-%d")
    ##print(f"{today} | {category} | ₹{amount:.2f} | {description}")
    with open("expenses.txt","a") as f:
        f.write(f"{today} | {category} | {amount:.2f} | {description}\n")
    print("Saved!")
    print()


def view_summary():
    total = 0.0
    by_category = {}

    with open("expenses.txt", "r") as f:
        for line in f:
            parts =(line.strip()).split(" | ")
            category = parts[1].strip()
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
    print()

while True:
    user_choice = input( "What do you want to do add[a] or view summary[v] or quit[q]?\n").lower()
    if user_choice == "a":
        add_expense()
    elif user_choice == "v":
        view_summary()
    elif user_choice == "q":
        break
    else:
        print("Please enter a correct choice")



