from datetime import datetime
amount = float(input("How much did you spend today? ₹ "))
category = input("Category(food, transport, bills): ").lower()
description = input("What was it for? ")
today = datetime.now().strftime("%Y-%m-%d")
##print(f"{today} | {category} | ₹{amount:.2f} | {description}")
with open("expenses.txt","a") as f:
    f.write(f"{today} | {category} | {amount:.2f} | {description} \n")
            
print("Saved!")



