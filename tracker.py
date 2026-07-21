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
    ##print(by_category)
    sorted_categories = sorted(by_category.items(), key=lambda item:item[1], reverse = True)
    for name,amount in sorted_categories:
        print(f"{name}: ₹{amount:.2f}")

    print()

def view_month():
    total = 0.0
    by_category = {}

    with open("expenses.txt", "r") as f:
        for line in f:
            parts =(line.strip()).split(" | ")
            tx_date = parts[0].split("-")
            if datetime.now().strftime("%Y-%m") == tx_date[0]+"-"+tx_date[1]:
                category = parts[1].strip()
                amount = float(parts[2])
                total = total + amount
                if category in by_category:
                    by_category[category] = by_category[category] + amount
                else:
                    by_category[category] = amount

        
    print(f"\n Total spent = ₹{total:.2f} \n")
    print("Where did you spend: ")
    ##print(by_category)
    sorted_categories = sorted(by_category.items(), key=lambda item:item[1], reverse = True)
    for name,amount in sorted_categories:
        print(f"{name}: ₹{amount:.2f}")

    print()

def delete_expense():
    total = 0
    print(f"List of entries \n")
    with open("expenses.txt", "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            print(f"{i+1}: {line}")
            total = i+1
    choice = input("\n Select the entry to delete \n")
    try:
        choice = int(choice)
        if choice<=total:
                with open("expenses.txt", "w") as f:
                    for i, line in enumerate(lines):
                        if i != choice - 1:
                            f.write(line)
        else:
            print(f"Enter a entry that exist")
    except ValueError:
            print("Please enter a valid number")


def search_expense():
    found = False
    keyword = input("What are you searching for? ").lower()
    with open("expenses.txt", "r") as f:
        for line in f:
            if keyword in line:
                found = True
                print(f"{line}")

        if found == False:
            print(f"No matching expense found")









while True:
    user_choice = input( "What do you want to do add[a] or view summary[v] or view current month summary[c] or delete_expense[d] or search_expense(s) or quit[q]?\n").lower()
    if user_choice == "a":
        add_expense()
    elif user_choice == "v":
        view_summary()
    elif user_choice == "c":
        view_month()
    elif user_choice == "d":  
        delete_expense()
    elif user_choice == "s":
        search_expense()
    elif user_choice == "q":
        break
    else: 
        print("Please enter a correct choice")

