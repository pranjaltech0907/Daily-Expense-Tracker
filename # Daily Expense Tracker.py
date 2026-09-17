# Daily Expense Tracker

expenses = []  
# global list to store all expense dictionaries


def show_menu():
    print("     DAILY EXPENSE TRACKER    ")
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. View Total & Average")
    print("4. Filter Expenses by Category")
    print("5. Exit")
    


def add_expense():
    item_name = input("Enter expense name: ")
    category = input(
        "Enter category (Food/Travel/Bills/Other): "
    ).capitalize()

    # Type conversion and simple input handling
    amount_str = input("Enter amount spent: ")
    amount = float(amount_str)

    # Using dictionaries and lists
    record = {"item": item_name, "category": category, "amount": amount}

    expenses.append(record)
    print("Expense recorded successfully!")


def view_all():
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    print("\n--- List of Expenses ---")
    count = 1
    # For loop iteration
    for exp in expenses:
        print(
            str(count)
            + ". "
            + exp["item"]
            + " | "
            + exp["category"]
            + " | Rs. "
            + str(exp["amount"])
        )
        count = count + 1


def calculate_summary():
    if len(expenses) == 0:
        print("No data available to calculate total.")
        return

    total = 0.0
    for exp in expenses:
        # Arithmetic operators
        total = total + exp["amount"]

    # Average calculation using basic division
    average = total / len(expenses)

    print("\n--- Expense Summary ---")
    print("Total Amount Spent: Rs. " + str(round(total, 2)))
    print("Number of Expenses: " + str(len(expenses)))
    print("Average per Expense: Rs. " + str(round(average, 2)))


def differentiate_by_category():
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    search_cat = input(
        "Enter category to search (Food/Travel/Bills/Other): "
    ).capitalize()
    found = False
    subtotal = 0.0

    print("\n--- Expenses for: " + search_cat + " ---")
    for exp in expenses:
        if exp["category"] == search_cat:
            print("- " + exp["item"] + ": Rs. " + str(exp["amount"]))
            subtotal = subtotal + exp["amount"]
            found = True

    if found == False:
        print("No records found under this category.")
    else:
        print("Category Subtotal: Rs. " + str(round(subtotal, 2)))


# Main driver loop
def main():
    while True:
        show_menu()
        choice = input("Enter choice (1-5): ")

        # Control flow using if-elif-else
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all()
        elif choice == "3":
            calculate_summary()
        elif choice == "4":
            differentiate_by_category()
        elif choice == "5":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid input! Please enter a number between 1 and 5.")


main()
