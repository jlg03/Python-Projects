from datetime import date, datetime



def main_menu(list_expenses):
    print("Select what you want to do")
    print()
    print("1. Add an expense")
    print()
    print("2. Update an expense")
    print()
    print("3. Delete an expense")
    print()
    print("4. View all expenses")
    print()
    print("5. View summary of all expenses")
    print()
    print("6. View summary of expense for a specific month (in the current year)")
    print()
    print("7. Quit")
    user_selection = input("Enter your selection: ")
    
    if user_selection == "1":
        description = input("Description: ")
        amount = float(input("Enter amount: "))
        add_expense(description=description, amount=amount, list_expenses=list_expenses)
    elif user_selection == "2":
        selected_date = input("Select a date (YYYY-MM-DD): ")
        convert_format = datetime.strptime(selected_date, "%Y-%m-%d").date()
        
        list_expense(date= convert_format, list_expenses=list_expenses)
        selected_id = int(input("Select an ID number: "))
        new_amount = float(input("Enter the new amount: "))
        update_expense(date=convert_format, id=selected_id, amount=new_amount,  list_expenses=list_expenses)
    elif user_selection == "3":
        selected_date = input("Select a date (YYYY-MM-DD): ")
        convert_format = datetime.strptime(selected_date, "%Y-%m-%d").date()
        list_expense(date=convert_format,  list_expenses=list_expenses)
        selected_id = int(input("Select an ID number to remove: "))
        delete_expense(date=convert_format, id=selected_id,  list_expenses=list_expenses)
    # elif user_selection == "4":
    #     list_expense(list_expenses=list_expenses)
    # elif user_selection == "5":
    #     total_expense(list_expenses=list_expenses)
    # elif user_selection == "6":
    #     total_expense_month(month=, list_expenses=list_expenses)
    # elif user_selection == "7":
    #     quit()
    else:
        print("That was an invalid input")
    
    

def add_expense(description, amount, list_expenses):
    id_number = 1
    today_date = date.today()
    if len(list_expenses) == 0:
        list_expenses.append([today_date,[id_number, description, amount]])
        print(f"Added successfully (ID: {id_number})")
        main_menu(list_expenses=list_expenses)
    else:
        for index in range(len(list_expenses)):
            if today_date == list_expenses[index][0]:
                id_number = len(list_expenses[index])
                list_expenses[index].append([id_number, description, amount])
                print(f"Added successfully (ID: {id_number})")
                main_menu(list_expenses=list_expenses)
            else:
                list_expenses.append([today_date,[id_number, description, amount]])
                print(f"Added successfully (ID: {id_number})")
                main_menu(list_expenses=list_expenses)    
    
def list_expense(date, list_expenses):
    for index in range(len(list_expenses)):
            if date == list_expenses[index][0]:
                print(list_expenses[index])
    # if date not empty list expenses for selected date
    # else list all expenses recorded
    
# def total_expense_month(month, list_expenses):
#     # list all expenses of the selected month of the current year
    
# def total_expense(list_expenses):
#     # list all expenses ever made
    
def update_expense(date, id, amount, list_expenses):
    for index in range(len(list_expenses)):
            if date == list_expenses[index][0]:
                if id == list_expenses[index][1][0]:
                    list_expenses[index][1][2] = amount
                    main_menu(list_expenses=list_expenses)
                        
def delete_expense(date, id, list_expenses):
    for index in range(len(list_expenses)):
            if date == list_expenses[index][0]:
                if id == list_expenses[index][1][0]:
                    list_expenses.remove(list_expenses[index])
                


list_expenses = []
main_menu(list_expenses)