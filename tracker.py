# Project: Expense Tracker - Installment 4
# Author: Zeus Zyrix Z. Tablada

print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("\nMAIN MENU")
print("[1] Add an expenset\t\t(coming soon)")
print("[2] View all expenses\t\t(coming soon)")
print("[3] Show total spent\t\t(coming soon)")
print("[4] Exit\t\t\t(coming soon)")

name = input("\nWhat`s your name? ")
print(f"Welcome, {name}! Let`s log two expenses.\n")

subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

if amount1 > 200:
    print(" are you sure?")
    print(" Huge expense")
elif amount1 > 100:
    print(" Big expense")
elif amount1 > 50:
    print(" Moderate expense")
else:
    print(" Small expense") 

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

if amount2 > 200:
    print(" are you sure?")
    print(" Huge expense")
elif amount2 > 100:
    print(" Big expense")
elif amount2 > 50:
    print(" Moderate expense")
else:
    print(" Small expense") 

if amount1 > 100 and amount2 > 100:
    print(" slow down!")
    print(" Two big expenses in a row")


tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
overBudget = total > budget
left = budget - total

print("\n----------------------------------------")
print("SUMMARY")
print(f"  - {item1}:\t${amount1}")
print(f"  - {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")

if total > budget:
    over_amount = total - budget
    print(f"Over budget by ${over_amount}!")
elif total > 0.9 * budget:
    left_amount = budget - total
    print(f"Careful: only ${left_amount} left.")
else:
    left_amount = budget - total
    print(f"Within budget. ${left_amount} left.")

print("----------------------------------------")

print(f"Made by: {name} | Installment 4")