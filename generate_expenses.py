import csv
from datetime import datetime

# Sample expenses dataset
expenses = [
    ["2024-10-01 12:30:00", 50.00, "Food", "Lunch at restaurant"],
    ["2024-10-02 09:15:00", 20.00, "Transport", "Taxi fare to office"],
    ["2024-10-02 18:45:00", 150.00, "Entertainment", "Movie tickets"],
    ["2024-10-03 11:00:00", 120.00, "Shopping", "Groceries"],
    ["2024-10-03 14:30:00", 30.00, "Food", "Coffee with friends"],
    ["2024-10-04 08:00:00", 60.00, "Transport", "Monthly bus pass"],
    ["2024-10-04 19:00:00", 200.00, "Shopping", "Clothing purchase"],
    ["2024-10-05 13:20:00", 45.00, "Food", "Dinner at restaurant"],
    ["2024-10-05 22:00:00", 80.00, "Entertainment", "Concert tickets"],
    ["2024-10-06 08:30:00", 90.00, "Transport", "Car fuel"]
]

# Save dataset to a CSV file
with open('expenses.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Amount', 'Category', 'Description'])  # Header
    writer.writerows(expenses)

print("Expenses dataset created and saved as 'expenses.csv'.")
