CLI Expense Tracker (Python)

A simple, command-line interface (CLI) application built with Python for tracking personal expenses. All data is persisted locally in a expenses.csv file, allowing you to easily manage and analyze your financial history.

Features

Expense Logging: Easily record new expenses with a date, category, amount, and description.

Data Persistence: Automatically saves all entries to a local expenses.csv file upon exiting.

View Entries: Display a formatted, chronological list of all recorded transactions.

Financial Summary: Generate a quick report showing the total amount spent and a detailed breakdown of spending by category.

Input Validation: Basic checks ensure that input amounts are numerical and dates follow the required format (YYYY-MM-DD).

Requirements

Python 3.6+ (The script uses standard library packages: csv, os, datetime, collections).

Installation and Setup

Clone or Download: Get the expense_tracker.py file to your local machine.

Run the Script: Open your terminal or command prompt, navigate to the directory where you saved the file, and run:

python expense_tracker.py


The application will automatically create an empty expenses.csv file in the same directory if one does not already exist.

Usage

When you run the application, you will be presented with the main menu:

Welcome to the CLI Expense Tracker!
Successfully loaded 0 existing records.


--- Menu ---
1. Add New Expense
2. View All Expenses
3. View Summary Report
4. Save & Exit
Enter your choice (1-4): 


1. Add New Expense

Select option 1 to input details for a new transaction. The application will guide you through entering the date, amount, category, and description.

Date: Enter in YYYY-MM-DD format (e.g., 2025-11-20). Leaving it blank defaults to today's date.

Category: Choose from suggested categories (Food, Bills, Transport, Entertainment, Income, Other) or enter a custom one.

2. View All Expenses

Select option 2 to display a neatly formatted table of all expenses, sorted by date (newest first).

3. View Summary Report

Select option 3 to see two key statistics:

Total Spent: The sum of all recorded amounts.

Category Breakdown: A list of how much was spent in each category, including the percentage of the total.

4. Save & Exit

Always select option 4 to ensure your current session's expenses are saved to the expenses.csv file before closing the program.
