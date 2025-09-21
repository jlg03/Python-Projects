def menu(to_do_list):
    valid_input = False
    while not valid_input:
        from_menu = True
        print(" 1) Add to the to do list \n 2) Remove from the to do list \n 3) View list  \n 4) Quit the to do list")
        user_choice = input("Select an option: ")
        if user_choice == "1":
            valid_input = True
            add_to_list(to_do_list)
        elif user_choice == "2":
            valid_input = True
            remove_from_list(to_do_list)
        elif user_choice == "3":
            valid_input = True
            show_list(to_do_list, from_menu)
        elif user_choice == "4":
            exit_to_do()
        else:
            print("That was an invalid input please try again")

def add_to_list(to_do_list):
    new_item = input("Enter item to add to the list: ")
    to_do_list.append(new_item)
    print("Item added")
    show_list(to_do_list, 0)
    menu(to_do_list)

def remove_from_list(to_do_list):
    show_list(to_do_list, 0)
    valid_input = False
    while not valid_input:
        selected_item = input("Select the number of the item to remove: ")
        if selected_item.isnumeric() and int(selected_item) <= len(to_do_list) and int(selected_item) != 0:
            valid_input = True
            selected_item = int(selected_item)
            selected_item -= 1
            to_do_list.pop(selected_item)
            print("Item removed")
            show_list(to_do_list, 0)
            menu(to_do_list)
        else:
            print("Invalid input please try again")
    
def show_list(to_do_list, from_menu):
    print("Current list: ")
    print("-------------------------")
    for index, item in enumerate(to_do_list):
        index += 1
        index = str(index)
        print(index + ") " + item)
    print("-------------------------")
    if from_menu:
        menu(to_do_list)
    
    
    

def exit_to_do():
    exit(1)


to_do = []
menu(to_do)

