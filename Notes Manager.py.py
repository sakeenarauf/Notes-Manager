
import os

FILENAME = "notes.txt"

def display_menu():
    print("\n=========================")
    print("      NOTES MANAGER      ")
    print("=========================")
    print("1. Add a Note")
    print("2. View Saved Notes")
    print("3. Exit")
    print("=========================")

def add_note():
    note = input("\nEnter your note: ")
    
    # Check if the user just pressed Enter without typing anything
    if note == "":
        print(" Cannot save an empty note.")
        return

    # "a" opens the file in APPEND mode. It creates the file if it doesn't exist,
    # or adds text to the end of it if it does.
    with open(FILENAME, "a") as file:
        file.write(note + "\n")
    print("✓ Note saved successfully!")

def view_notes():
    # Check if file exists first
    if not os.path.exists(FILENAME):
        print("\n No notes found. Start by adding one!")
        return

    print("\n--- Your Saved Notes ---")
    
    with open(FILENAME, "r") as file:
        counter = 1
        for line in file:
            # We use end="" because the line already has a newline character (\n)
            print(str(counter) + ". " + line, end="")
            counter = counter + 1
            
    print("\n------------------------")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-3): ")
        
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("\nGoodbye! Thanks for using Notes Manager.")
            break
        else:
            print(" Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
