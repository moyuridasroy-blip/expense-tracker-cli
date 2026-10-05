"""Expense Tracker (command line)
Add expenses, view them, and see a category-wise summary. Data is saved in expenses.csv.
"""
import csv
import os
from datetime import date

FILE = "expenses.csv"
FIELDS = ["date", "category", "description", "amount"]


def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, newline="") as f:
        return list(csv.DictReader(f))


def save(rows):
    with open(FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def add_expense():
    category = input("Category (food/travel/rent/other): ").strip().lower()
    description = input("Description: ").strip()
    try:
        amount = float(input("Amount (Rs): "))
    except ValueError:
        print("Invalid amount.")
        return
    rows = load()
    rows.append({"date": date.today().isoformat(), "category": category,
                 "description": description, "amount": amount})
    save(rows)
    print("Expense added.")


def view_expenses():
    rows = load()
    if not rows:
        print("No expenses yet.")
        return
    print(f"\n{'Date':<12}{'Category':<10}{'Description':<22}{'Amount':>8}")
    for r in rows:
        print(f"{r['date']:<12}{r['category']:<10}{r['description']:<22}{float(r['amount']):>8.2f}")


def summary():
    rows = load()
    if not rows:
        print("No expenses yet.")
        return
    totals = {}
    for r in rows:
        totals[r["category"]] = totals.get(r["category"], 0) + float(r["amount"])
    grand = sum(totals.values())
    print("\n--- Summary by category ---")
    for cat, amt in sorted(totals.items(), key=lambda x: -x[1]):
        print(f"{cat:<10}Rs {amt:>9.2f}  ({amt / grand * 100:.1f}%)")
    print(f"{'TOTAL':<10}Rs {grand:>9.2f}")


def main():
    while True:
        print("\n1. Add expense\n2. View expenses\n3. Summary\n4. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary()
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
