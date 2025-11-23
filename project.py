import csv
import os
from datetime import datetime
from collections import defaultdict

DATA_FILE = 'expenses.csv'
FIELDNAMES = ['Date', 'Category', 'Amount', 'Description']
DATE_FORMAT = '%Y-%m-%d'

def load_expenses():
    expenses = []
    if not os.path.exists(DATA_FILE):
        return expenses

    try:
        with open(DATA_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    row['Amount'] = float(row['Amount'])
                    expenses.append(row)
                except ValueError:
                    print(f"Warning: Skipping invalid amount entry in file: {row}")
            return expenses
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

def save_expenses(expenses):
    try:
        with open(DATA_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(expenses)
        print("\n[INFO] Expenses saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")

def add_expense(expenses):
    print("\n--- Add New Expense ---")
    
    while True:
        date_str = input(f"Enter Date (YYYY-MM-DD, e.g., {datetime.now().strftime(DATE_FORMAT)}): ").strip()
        if not date_str:
            date_str = datetime.now().strftime(DATE_FORMAT)
            print(f"Using today's date: {date_str}")
        try:
            datetime.strptime(date_str, DATE_FORMAT)
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    while True:
        try:
            amount = float(input("Enter Amount: ").strip())
            if amount <= 0:
                print("Amount must be positive.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    
    print("Available Categories: Food, Bills, Transport, Entertainment, Income, Other")
    category = input("Enter Category: ").strip() or "Other"

    description = input("Enter Description (optional): ").strip() or "N/A"

    new_expense = {
        'Date': date_str,
        'Category': category,
        'Amount': amount, 
        'Description': description
    }
    expenses.append(new_expense)
    print("\n[INFO] Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("\n(No expenses recorded yet.)")
        return

    print("\n--- All Expenses ---")
    
    sorted_expenses = sorted(expenses, key=lambda x: x['Date'], reverse=True)
    
    col_widths = {
        'Date': 10,
        'Category': max(len(row['Category']) for row in expenses) if expenses else 8,
        'Amount': 10,
        'Description': 30
    }
    for key in col_widths:
        col_widths[key] = max(col_widths[key], len(key))

    def pad(text, width):
        return str(text).ljust(width)

    header = f"| {pad('Date', col_widths['Date'])} | {pad('Category', col_widths['Category'])} | {pad('Amount', col_widths['Amount'])} | {pad('Description', col_widths['Description'])} |"
    separator = '-' * len(header)
    
    print(separator)
    print(header)
    print(separator)

    for expense in sorted_expenses:
        amount_str = f"{expense['Amount']:.2f}".rjust(col_widths['Amount'])
        row = (
            f"| {pad(expense['Date'], col_widths['Date'])} "
            f"| {pad(expense['Category'], col_widths['Category'])} "
            f"| {amount_str} "
            f"| {pad(expense['Description'][:col_widths['Description']], col_widths['Description'])} |"
        )
        print(row)
    
    print(separator)


def summarize_expenses(expenses):
    if not expenses:
        print("\n(No expenses to summarize.)")
        return

    print("\n--- Expense Summary ---")

    total_expense = 0.0
    category_summary = defaultdict(float)

    for expense in expenses:
        amount = expense['Amount']
        category = expense['Category']
        
        total_expense += amount
        category_summary[category] += amount

    print(f"\nTOTAL SPENT: ${total_expense:,.2f}")
    
    print("\nBreakdown by Category:")
    
    max_cat_len = max(len(cat) for cat in category_summary.keys())
    
    for category, amount in sorted(category_summary.items(), key=lambda item: item[1], reverse=True):
        percentage = (amount / total_expense) * 100 if total_expense else 0
        
        category_padded = category.ljust(max_cat_len)
        amount_formatted = f"${amount:,.2f}".rjust(12)
        percentage_formatted = f"({percentage:5.2f}%)"
        
        print(f"  - {category_padded}: {amount_formatted} {percentage_formatted}")
    
    print("-" * (max_cat_len + 20))

def main():
    print("Welcome to the CLI Expense Tracker!")
    
    expenses = load_expenses()
    print(f"Successfully loaded {len(expenses)} existing records.")

    while True:
        print("\n\n--- Menu ---")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. View Summary Report")
        print("4. Save & Exit")
        
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_expense(expenses)
        
        elif choice == '2':
            view_expenses(expenses)
            
        elif choice == '3':
            summarize_expenses(expenses)
            
        elif choice == '4':
            save_expenses(expenses)
            print("\n[INFO] Thank you for using the tracker. Goodbye!")
            break
            
        else:
            print("\n[ERROR] Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
