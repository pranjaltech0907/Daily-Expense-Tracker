expenses = []


def menu():
    print("\nDAILY EXPENSE TRACKER")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Show Total and Average")
    print("4. Search by Category")
    print("5. Exit")


def add_expense():
    name = input("Enter expense name: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    expense = [name, category, amount]
    expenses.append(expense)

    print("Expense added successfully!")


def show_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
    else:
        print("\nYour Expenses:")

        for i in range(len(expenses)):
            print(i + 1, expenses[i][0], expenses[i][1], "Rs.", expenses[i][2])


def total_average():
    if len(expenses) == 0:
        print("No expenses found.")
    else:
        total = 0

        for expense in expenses:
            total = total + expense[2]

        average = total / len(expenses)

        print("Total = Rs.", total)
        print("Average = Rs.", average)


def search_category():
    category = input("Enter category: ")
    found = False
    total = 0

    for expense in expenses:
        if expense[1].lower() == category.lower():
            print(expense[0], "Rs.", expense[2])
            total = total + expense[2]
            found = True

    if found == False:
        print("No expense found.")
    else:
        print("Category Total = Rs.", total)


while True:

    menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        total_average()

    elif choice == "4":
        search_category()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Wrong choice!")


  
