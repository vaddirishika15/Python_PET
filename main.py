import csv
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename='expenses.csv'):
        self.filename = filename

    def add_expense(self, amount, category, description):
        
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(), amount, category, description])
        print(f"Expense added: {amount} - {category} - {description}")

    def view_expenses(self):
        print("\nYour Expenses:")
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def get_total_expenses(self):
        total = 0
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                total += float(row[1])  # Amount is in the second column
        return total

    def delete_expense(self, index):
        expenses = self.get_expenses()
        if 0 <= index < len(expenses):
            del expenses[index]
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Date', 'Amount', 'Category', 'Description'])  # Header
                writer.writerows(expenses)
            print("Expense deleted successfully.")
        else:
            print("Invalid index. No expense deleted.")

    def get_expenses(self):
        expenses = []
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                expenses.append(row)
        return expenses

# Create a CLI to interact with the user
def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Get Total Expenses")
        print("4. Delete an Expense")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            amount = input("Enter amount: ")
            category = input("Enter category (e.g., Food, Transport, etc.): ")
            description = input("Enter description: ")
            tracker.add_expense(amount, category, description)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            total = tracker.get_total_expenses()
            print(f"Total Expenses: {total}")
        elif choice == '4':
            tracker.view_expenses()
            index = int(input("Enter the index of the expense to delete: "))
            tracker.delete_expense(index)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
