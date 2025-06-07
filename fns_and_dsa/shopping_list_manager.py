shopping_list = []

def append(item):
    shopping_list.append(item)

def remove(item):
    shopping_list.remove(item)

def print_list():
    for i in range(len(shopping_list)):
        print(shopping_list[i])

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item_name = input("Enter the item to add: ")
            append(item_name)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item_name = input("Enter the item name yo want to remove: ")
            remove(item_name)
            pass
        elif choice == '3':
            # Display the shopping list
            print(print_list())
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()