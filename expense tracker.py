import csv

FILENAME = "expenses.csv"

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food, Travel, Shopping, etc.): ")
    amount = float(input("Enter amount: "))

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("\nExpense added successfully!\n")


def view_expenses():
    print("\n------ Expenses ------")

    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)

            total = 0

            for row in reader:
                print(f"Date: {row[0]} | Category: {row[1]} | Amount: ₹{row[2]}")
                total += float(row[2])

            print("----------------------")
            print(f"Total Expense = ₹{total:.2f}\n")

    except FileNotFoundError:
        print("No expenses found.\n")


while True:
    print("====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid Choice\n")
