# Project: Expense Tracker - Installment 3
# Author: Zeus Zyrix Z. Tablada
# Description: Expense the tracker does math

print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("MAIN MENU")
print(" " * 2 +"[1] Add an expense".ljust(25) + "(coming soon)")
print(" " * 2 +"[2] View all expenses".ljust(25) + "(coming soon)")
print(" " * 2 +"[3] Show total spent".ljust(25) + "(coming soon)")
print(" " * 2 +"[4] Exit".ljust(25) + "(coming soon)")

name = input("\nWhat`s your name? ")
print(f"Welcome, {name}! Let`s log two expenses.\n")
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

subtotal = 0
subtotal += amount1
subtotal += amount2

tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
overBudget = total > budget
left = budget - total

print("\n" + "-" * 40)
print("SUMMARY")
print(f" -{item1}:".ljust(16)+f"${amount1}")
print(f" -{item2}:".ljust(16)+f"${amount2}")
print(f"Subtotal:".ljust(16)+f"${subtotal}")
print(f"Average:".ljust(16)+f"${average}")
print(f"Tax ({tax_percent}%):".ljust(16)+f"${tax}")
print(f"Grand total:".ljust(16)+f"${total}")
print(f"Over budget:".ljust(16)+f"${overBudget}")
print(f"Left in budget:".ljust(16)+f"${left}")
print("-" * 40)

print(f"Made by: {name} | Installment 3")