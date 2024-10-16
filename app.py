import streamlit as st
import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Initialize session state for expenses if it doesn't exist
if 'session_expenses' not in st.session_state:
    st.session_state.session_expenses = []

# Add Expense Function (only in session, but still write to CSV)
def add_expense(amount, category, description):
    expense = [datetime.now(), amount, category, description]
    st.session_state.session_expenses.append(expense)  # Add to session state
    
    # Save to CSV (this won't affect what is displayed, just saves for record-keeping)
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(expense)
    
    st.success(f"Added Expense: {amount} - {category} - {description}")


# View Session Expenses Function (only from current session)
def view_session_expenses():
    if st.session_state.session_expenses:
        df = pd.DataFrame(st.session_state.session_expenses, columns=['Date', 'Amount', 'Category', 'Description'])
        st.write(df)
    else:
        st.write("No expenses added yet in this session.")


# Get Total Expenses in Current Session
def get_total_expenses():
    total = sum(float(expense[1]) for expense in st.session_state.session_expenses)
    return total


# Delete Expense Function (delete from current session only)
def delete_expense(index):
    if 0 <= index < len(st.session_state.session_expenses):
        del st.session_state.session_expenses[index]
        st.success("Expense deleted successfully.")
    else:
        st.error("Invalid index. Please choose a valid index.")


# Create a Pie Chart for Category Distribution
def category_distribution():
    if st.session_state.session_expenses:
        df = pd.DataFrame(st.session_state.session_expenses, columns=['Date', 'Amount', 'Category', 'Description'])
        category_totals = df.groupby('Category')['Amount'].sum()
        fig, ax = plt.subplots()
        ax.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%')
        st.pyplot(fig)
    else:
        st.write("No expenses to display for this session.")


# Streamlit Web App Interface
def main():
    st.title("Personal Expense Tracker")

    # Sidebar for actions
    action = st.sidebar.selectbox("Choose Action", ["Add Expense", "View Expenses", "Get Total Expenses", "Delete an Expense", "Category Distribution"])

    if action == "Add Expense":
        st.subheader("Add a New Expense")
        amount = st.number_input("Amount", min_value=0.0, format="%.2f")
        category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Shopping", "Other"])
        description = st.text_input("Description")
        if st.button("Add Expense"):
            add_expense(amount, category, description)

    elif action == "View Expenses":
        st.subheader("View All Expenses (Current Session Only)")
        view_session_expenses()

    elif action == "Get Total Expenses":
        st.subheader("Total Expenses (Current Session Only)")
        total = get_total_expenses()
        st.write(f"Total Expenses: ${total:.2f}")

    elif action == "Delete an Expense":
        st.subheader("Delete an Expense (Current Session Only)")
        view_session_expenses()
        index = st.number_input("Enter the index of the expense to delete", min_value=0)
        if st.button("Delete"):
            delete_expense(index)

    elif action == "Category Distribution":
        st.subheader("Category Distribution (Current Session Only)")
        category_distribution()


if __name__ == "__main__":
    main()
