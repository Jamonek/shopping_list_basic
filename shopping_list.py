# make a list to hold onto our items
shopping_list = []


def show_help():
    # print out instructions on how to use app
    print("Welcome to your easy shopping list!")
    print("What should we pick up at the store?")
    print("""
    
Enter 'DONE' to stop adding items
Enter 'HELP' for this help
Enter 'SHOW' to see your current list.
""")

def show_list():
    # print out the list
    print("Here's your list:")

    for item in shopping_list:
        print(item)


def add_to_list(new_item):
    # add new items to our list
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

def show_list_total():
    print("Your list has a total of {} items".format(len(shopping_list)))


show_help()


while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit app
    if new_item == 'DONE':
        break

    elif new_item == 'HELP':
        show_help()
        continue

    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)

show_list()
show_list_total()
