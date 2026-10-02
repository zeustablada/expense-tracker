# Project: Expense Tracker - Installment 2
# Author: Zeus Zyrix Z. Tablada
# Description: Displays the landing page and main menu layout for the expense tracker.

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("\nWelcome! This is your personal expense tracker.\n")

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

total = amount1 + amount2
average = total / 2

print("\n" + "-" * 40)
print("SUMMARY")
print(f" -{item1}:".ljust(16)+f"${amount1}")
print(f" -{item2}:".ljust(16)+f"${amount2}")
print("Total spent:".ljust(16)+f"${total}")
print("Average:".ljust(16)+f"${average}")
print("-" * 40)

print(f"Made by: {name} | Installment 2")