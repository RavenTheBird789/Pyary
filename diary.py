# Diary
import os
import time

def diary_UI(selection):
    def wrapper():
        print("=========================")
        print("----------DIARY----------")
        print("=========================")
        print("---By: RavenTheBird789---")
        print("=========================")
        print("Option 1: Add an entry")
        print("Option 2: Remove an entry")
        print("Option 3: Update an entry")
        print("Option 4: Show all entries")
        print("Option 5: Exit")
        print("=========================")
        selection()
    return wrapper

def load_entries():
    if os.path.exists("entries.txt"):
        with open("entries.txt", "r") as ef:
            return [line.strip() for line in ef if line.strip()]
    return []

def save_entries(entry_list):
    with open("entries.txt", "w") as ef:
        ef.write("\n".join(entry_list))

def diary_entry():
    entry_list = load_entries()
    entry = input("Write about your day: ")
    if entry:
        entry_list.append(entry)
        save_entries(entry_list)

def remove_entry():
    entry_list = load_entries()
    i = 0
    for entry in entry_list:
        i = i + 1
        print(f"{i}: {entry}")
    int_query = int(input("Enter the number of the entry you'd like to remove: "))
    entry_int = int_query - 1
    entry_list.remove(entry_list[entry_int])
    save_entries(entry_list)

def update_entries():
    entry_list = load_entries()
    i = 0
    for entry in entry_list:
        i = i + 1
        print(f"{i}: {entry}")
    int_query = int(input("Enter the number of the entry you'd like to update: "))
    entry_int = int_query - 1
    entry_list[entry_int] = input("Type your new entry here: ")
    save_entries(entry_list)

def show_entries():
    entry_list = load_entries()
    myDiary = {i + 1: entry for i, entry in enumerate(entry_list)}
    print(myDiary)

def user_prompt():
    prompt = input("Would you like to return to the main menu? (yes/no): ")
    if prompt == "yes":
        os.system('clear')
        user_selection()
    elif prompt == "no":
        os.system('clear')
        return;
    else:
        os.system('clear')
        print("Invalid input, returning to main menu...")
        time.sleep(3);
        os.system('clear')
        user_selection()

@diary_UI
def user_selection():
    user_choice = input("Select your choice: ")
    if user_choice == '1':
        diary_entry()
        time.sleep(2)
        user_prompt()
    elif user_choice == '2':
        remove_entry()
        time.sleep(2)
        user_prompt()
    elif user_choice == '3':
        update_entries()
        time.sleep(2)
        user_prompt()
    elif user_choice == '4':
        show_entries()
        time.sleep(2)
        user_prompt()
    elif user_choice == '5':
        os.system('clear')
        os._exit(0)
    else:
        print("Invalid Input")
user_selection()