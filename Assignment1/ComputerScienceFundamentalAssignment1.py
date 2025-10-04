from datetime import datetime, timedelta

# Sample library inventory (book title: number of copies)
library_books = {"CSF": 3,"To Kill a Mockingbird": 1,"The Great Gatsby": 2}

# Sample list to store borrowing records
borrow_records = []

# Function to borrow a book
def borrow_book():
    # Get user input
    user_id = input("Enter your User ID: ")
    book_title = input("Enter the book title you want to borrow: ").lower()

    # Normalize book title (case-insensitive matching)
    matched_title = None
    for title in library_books:
        if title.lower() == book_title:
            matched_title = title
            break

    # Check if book exists
    if matched_title:
        # Check availability
        if library_books[matched_title] > 0:
            # Update inventory
            library_books[matched_title] -= 1

            # Set borrow and return dates
            borrow_date = datetime.now()
            return_date = borrow_date + timedelta(days=14)

            # Record the transaction
            borrow_records.append({
                "user_id": user_id,
                "book_title": matched_title,
                "borrow_date": borrow_date.strftime("%Y-%m-%d"),
                "return_date": return_date.strftime("%Y-%m-%d")
            })

            # Show confirmation
            print("\n✅ Book borrowed successfully!")
            print(f"User ID: {user_id}")
            print(f"Book Title: {matched_title}")
            print(f"Return by: {return_date.strftime('%Y-%m-%d')}")
        else:
            print("\nSorry, this book is currently not available.")
    else:
        print("\n Book not found in the library.")

# Run the function
borrow_book()
