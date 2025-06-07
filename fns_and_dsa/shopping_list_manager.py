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