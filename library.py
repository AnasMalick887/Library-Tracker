# library.py
# A simple command-line library tracker.

books = {}  # title -> {"author": str, "available": bool}

def show_menu():
    print("\n=== Library Tracker ===")
    print("1. Add book")
    print("2. List books")
    print("3. Borrow book")
    print("4. Return book")
    print("0. Exit")
    
def add_book():
    title = input("Title: ").strip()
    if title in books:
        print(f'"{title}" is already in the library.')
        return
    author = input("Author: ").strip()
    books[title] = {"author": author, "available": True}
    print(f'Added "{title}".')
    
def list_books():
    if not books:
        print("No books in the library.")
        return

    print("\n=== All Books ===")

    for title, details in books.items():
        status = "Available" if details["available"] else "Borrowed"

        print(f"Title: {title}")
        print(f"Author: {details['author']}")
        print(f"Status: {status}")
        print("--------------------")
        
def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            list_books()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
            
if __name__ == "__main__":
    main()
