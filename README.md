# 💸 Expense Tracker (CLI)

A command-line app to record daily expenses and see where the money goes. Built for tracking a student's monthly budget (food, travel, rent, etc.).

## Features
- Add an expense with category, description and amount
- View all saved expenses in a table
- Category-wise summary with percentages
- Data is saved automatically in `expenses.csv`

## Tools Used
- Python 3 (`csv`, `datetime`, `os`; no external libraries)

## How to Run
```bash
python expense_tracker.py
```

## Sample Output
```
--- Summary by category ---
rent      Rs   6000.00  (60.0%)
food      Rs   2500.00  (25.0%)
travel    Rs   1500.00  (15.0%)
TOTAL     Rs  10000.00
```

## What I Learned
File handling with CSV, dictionaries, menu-driven programs and basic data summarising.
