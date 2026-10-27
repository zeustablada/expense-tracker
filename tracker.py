# Project: Expense Tracker - Installment 5
# Author: Zeus Zyrix Z. Tablada

print("========================================")
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("========================================")

name = input("What`s your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

print(f"Welcome, {name}!\n")

subtotal = 0
count = 0

print("\nMAIN MENU")
print("  [1] Add an expense")
print("  [2] View all expenses (Coming soon)")
print("  [3] Show total spent")
print("  [4] Exit")

while True:
    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1

        if amount > 200:
            print(" are you sure?")
            print(" Huge expense")
        elif amount > 100:
            print(" Big expense")
        elif amount > 50:
            print(" Moderate expense")
        else:
            print(" Small expense")

    elif choice == "2":
        print("Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax

        print(f"Expenses:\t{count}")
        print(f"Subtotal:\t${subtotal}")
        print(f"Tax ({tax_percent}%):\t${tax}")
        print(f"Grand total:\t${total}")

        if total > budget:
            over_amount = total - budget
            print(f"Over budget by ${over_amount}!")
        elif total > budget * 0.9:
            left_amount = budget - total
            print(f"Careful: only ${left_amount} left.")
        else:
            left_amount = budget - total
            print(f"Within budget. ${left_amount} left.")

    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("----------------------------------------")
        print(f"Made by: Tablada\t|\tInstallment 5")
        print("========================================")
        break

    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")