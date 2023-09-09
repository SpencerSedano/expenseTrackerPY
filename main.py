# Importing Modules
import csv
import os


# Print the information of how the app will work

print("Welcome to the app! \n")
print("1. Add an expense \n")
print("2. Summary Expenses \n")
print("3. Modify an expense \n")
print("4. Delete an expense \n")

#Headers of the CSV
headers = ['expense', 'amount', 'date']

# Check if the CSV file exists, and if not, create it with the header
if not os.path.isfile('expenses.csv') or os.path.getsize('expenses.csv') == 0:
    with open('expenses.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        
#Adding expenses
def add_expense():
    user_expense = input("Name of the expense: ")
    user_expense_amount = int(input("How much? "))
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writerow({'expense': user_expense, 'amount': user_expense_amount})


#Getting the user's input number
user_input = int(input("Choose a number: "))

if user_input == 1:
    add_expense()
else:
    print("Invalid number")





