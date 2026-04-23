import csv
import pandas as pd
import matplotlib.pyplot as plt
def menu():
    print("1. Add Expense ")
    print("2. Delete any wrong expense entry ")
    print("3. Show Monthly Summary ")
    print("4. View Category-Wise Summary ")
    print("5. Overall Yearly Summary of Expenses")
    print("6. Yearly Category-wise Bar Chart")
    print("7. Exit ")
def add_expense():
    try:
        date = input("Enter the date (DD-MM-YY) : ")
        category = input("Enter the category (Bills, Rent, Food or Travel): ")
        amount = int(input("Enter the amount : "))
        desc = input("Enter the description about your expense : ")
    except ValueError:
        print("Enter valid input in the details !!")

    with open("expenses.csv","a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category , amount , desc ])

    print("Expense added !")

def del_expense():
    df = pd.read_csv("expenses.csv",header=None,names=["Date","Category","Amount","Description"])
    print("All the expenses entries : ")
    print(df)

    index = int(input("Enter the index of expense that has to be deleted : "))
    df = df.drop(index)

    df.to_csv("expenses.csv",index=False, header=False)
    print("Deleted Successfully !!")
def show_summary():
    df = pd.read_csv("expenses.csv",header=None,names=["Date","Category","Amount","Description"])
    print("Monthly Summary :")
    df["Date"] = pd.to_datetime(df["Date"],format="%d-%m-%y")
    df["Month"] = df["Date"].dt.strftime("%B")
    monthly_summary = df.groupby("Month")["Amount"].sum()
    print(monthly_summary)
    print()
    
def category_wise():
    df = pd.read_csv("expenses.csv",header=None,names=["Date","Category","Amount","Description"])
    cat = input("Enter the category (Food, Bills, Travel, Rent) : ")
    print(df[df["Category"] == cat])

def yearly_summary():
    df = pd.read_csv("expenses.csv",header=None,names=["Date","Category","Amount","Description"])
    print("\nTotal Spending : ",df["Amount"].sum())
    print("\nCategory-wise spending : ")
    print(df.groupby("Category")["Amount"].sum())

def show_barchart():
    df = pd.read_csv("expenses.csv",header=None,names=["Date","Category","Amount","Description"])
    df.groupby("Category")["Amount"].sum().plot(kind="bar")
    plt.ylabel("Expenses")
    plt.xlabel("Categories")
    plt.show()

while True:
    menu()

    choice = int(input("Enter the choice : "))
    if choice == 1:
        add_expense()
    elif choice == 2:
        del_expense()
    elif choice == 3:
        show_summary()
    elif choice == 4:
        category_wise()
    elif choice == 5:
        yearly_summary()
    elif choice == 6:
        show_barchart()
    elif choice == 7:
        break
    else:
        print("Enter a valid choice !!")


