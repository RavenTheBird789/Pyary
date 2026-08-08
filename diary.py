# Diary
import os
import time
import hashlib

def red(text: str) -> str:
    return f"\033[91m{text}\033[0m"

def green(text: str) -> str:
    return f"\033[92m{text}\033[0m"

def bold(text: str) -> str:
    return f"\033[1m{text}\033[0m"

def yellow(text: str) -> str:
    return f"\033[93m{text}\033[0m"

def diary_UI(selection):
    def wrapper():
        print("=========================")
        print("----------" + yellow("PYARY") + "----------")
        print("=========================")
        print("---" + red("By: RavenTheBird789") + "---")
        print("=========================")
        print("Option 1: Add an entry")
        print("Option 2: Remove an entry")
        print("Option 3: Update an entry")
        print("Option 4: Show all entries")
        print("Option 5: Change password")
        print("Option 6: Exit")
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

def exit_animation():
    """Handles the graceful exit animation cleanly."""
    for i in range(4):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Exiting{'.' * i}")
        time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    os._exit(0)

def user_prompt():
    prompt = input("Would you like to return to the main menu? (yes/no): ")
    if prompt == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        user_selection()
    elif prompt == "no":
        os.system('cls' if os.name == 'nt' else 'clear')
        exit_animation()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(red(bold("Invalid input, returning to main menu...")))
        time.sleep(3);
        os.system('cls' if os.name == 'nt' else 'clear')
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
        new_password = input("What is your new password?: ").strip()
        os.system('cls' if os.name == 'nt' else 'clear')
        confirmation = input("Enter your new password again: ").strip()
        if new_password == confirmation:
            hashed_new_pass = hashlib.sha256(new_password.encode()).hexdigest()
            os.remove("password.txt")
            with open("password.txt", "w") as pw:
                        pw.write("".join(hashed_new_pass))
            for i in range(4):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"Updating Password{'.' * i}")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')
            print(green(bold("Your password has been updated!")))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            user_selection()
        else:
            print(red(bold("Error: Passwords do not match")))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            user_selection()  
    elif user_choice == '6':
        os.system('cls' if os.name == 'nt' else 'clear')
        exit_animation()
    else:
        print(red(bold("Invalid Input")))

def main():
    if os.path.exists("password.txt"):
        user_name = ""
        user_password = ""
        with open("username.txt", "r", encoding="utf-8") as un:
            user_name = un.read().strip()
        with open("password.txt", "r", encoding="utf-8") as pt:
            user_password = pt.read().strip()

        authentication_query = input("What is the password?: ").strip()
        hashed_auth_query = hashlib.sha256(authentication_query.encode()).hexdigest()

        if hashed_auth_query == user_password:
            print(green(bold("Access Granted")))
            time.sleep(1)
            print(f"Welcome, {user_name} :)")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            user_selection()
        else:
            print(red(bold("Access Denied")))

    else:
        username = input("What is your name?: ")
        with open("username.txt", "w") as un:
            un.write("".join(username))
    
        password = input("What is the password you'd like to set?: ").strip()
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        with open("password.txt", "w") as pw:
            pw.write("".join(password_hash))
        print("Your password has been saved")
        time.sleep(1)
        print("Please, run the script again")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
main()
