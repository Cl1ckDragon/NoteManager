def main():
    notes = []

    while True:
        print("\n--- Note Manager ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            note = input("Enter note: ")
            notes.append(note)
            print("Note added!")

        elif choice == "2":
            if not notes:
                print("No notes available!")
            else:
                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {note}")

        elif choice == "3":
            if not notes:
                print("No notes to delete!")
            else:
                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {note}")

                try:
                    index = int(input("Enter note number to delete: ")) - 1

                    if 0<= index < len(notes):
                        deleted = notes.pop(index)
                        print(f"Deleted: {deleted}")
                    else:
                        print("Invalid number!")

                except ValueError:
                    print("Please enter a valid number!")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()