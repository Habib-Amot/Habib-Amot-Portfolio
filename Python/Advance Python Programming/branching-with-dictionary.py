# branching are mostly done with if, elifs and else statements. The same effect can be achieved by making use of dictionaries which stores
# the options and the corresponding function or method that we want to call
# here is a main program that takes user input and then calls a function based on the input
import sys

selections = []


def main():
    choices = {"A", "S", "Q", "D", 'U'}  # these are the set of valid choices, set is used here for fast memebership testing
    actions = {
        "A": add_item,
        # "S": save_selections,
        "Q": quit_program,
        "D": delete_item,
        "U": update_item,
    }

    while True:
        view_all_items()
        print()

        try:
            print("Please select an action")
            user_input = input(show_options()).strip()
            if user_input.upper() not in choices:
                print("Invalid option")
                continue
            else:
                user_input = user_input.upper()
                actions[user_input]()

        except KeyboardInterrupt:
            choice = input("\nExit program or continue [y/n]:")
            while choice.lower() not in {'y', 'n'}:
                choice = input("Exit program or continue [y/n]:")
                continue
            if choice.lower == 'n':
                continue
            else:
                sys.exit(0)



def show_options():
    return"[A]dd item, [S]ave selections, [Q]uit, [D]elete item, [U]pdate item : "  


def get_index(action):
    while True:
        try:
            index = int(input("Enter Item number to {}: ".format(action))) - 1
            if 0 > index or index >= len(selections):
                print("number out of range")
                continue
            else:
                return index
        except ValueError as err:
            print(err.__class__.__name__)
            continue


def view_all_items():
    if len(selections) == 0:
        print("No task")
    else:
        for num, item in enumerate(selections, start=1):
            print('[{0}]: {1}'.format(num, item))


def delete_item():
    index = get_index("delete")
    del selections[index]


def update_item():
    index = get_index("update")
    new_item = input("Enter new item to use (press <Enter> to keep the current value): ")
    if not new_item:
        return
    else:
        selections[index] = new_item


def add_item():
    global selections
    new_item = input("Enter new item (press <Enter> to keep the current value): ")
    if not new_item:
        return
    else:
        selections.append(new_item)


def quit_program():
    sys.exit()


if __name__ == "__main__":
    main()
