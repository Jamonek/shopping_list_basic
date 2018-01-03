import os

# make a list to hold onto our items
shopping_list = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_help():
    clear_screen()
    # print out instructions on how to use app
    print("Welcome to your easy shopping list!")
    print("What should we pick up at the store?")
    print("""
    
Enter 'DONE' to stop adding items
Enter 'HELP' for this help
Enter 'SHOW' to see your current list.
""")


def show_list():
    clear_screen()
    # print out the list
    print("Here's your list:")

    index = 1
    for item in shopping_list:
        print("{}. {}".format(index, item))
        index += 1

    print("-"*10)


def add_to_list(item):
    show_list()
    if len(shopping_list):
        position = input("Where should I add {}?\n"
                         "Press ENTER to add to the end of the list\n"
                         "> ".format(item))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(new_item)

    show_list()


def file_store():
    outF = open("shopping_list_file.txt", "a")
    for line in shopping_list:
        outF.write(line)
        outF.write("\n")
    outF.close()

show_help()

while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit app
    if new_item.upper == 'DONE' or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
         show_list()
    else:
        add_to_list(new_item)

show_list()
file_store()
