def search_a_book(books):
    print("\n==== SEARCH BOOKS ====")
    
    search_term = input("Enter search term (title, author or category): ").lower().strip()
    
    if not search_term:
        print("Error: Search term cannot be empty.")
        return []
    
    results = []
    
    for book in books:
        if (search_term in book['title'].lower() or 
            search_term in book['author'].lower() or 
            search_term in book['category'].lower()):
            results.append(book)
    
    if not results:
        print(f"No books found matching '{search_term}'.")
        return []
    
    print(f"\nFound {len(results)} results for '{search_term}':")
    
    # Print table header
    print(f"{'ID':<5} {'TITLE':<30} {'AUTHOR':<20} {'YEAR':<6} {'CATEGORY':<15} {'STATUS':<10}")
    print("-" * 90)
    
    # Print book data
    for book in results:
        print(f"{book['id']:<5} {book['title'][:28]:<30} {book['author'][:18]:<20} {book['year']:<6} {book['category']:<15} {book['status']:<10}")
    
    return results


def lend_a_book(books):
    print("\n==== LEND A BOOK ====")
    
    # Show available books
    available_books = [book for book in books if book['status'] == 'Available']
    if not available_books:
        print("There are no books available for lending.")
        return False
    
    # Search for a book first
    print("First, search for the book you want to lend:")
    results = search_a_book(books)
    
    if not results:
        return False
    
    # Request book ID to lend
    while True:
        try:
            book_id = int(input("\nEnter the ID of the book you want to lend: "))
            break
        except ValueError:
            print("Error: ID must be a number.")
    
    # Search for the book by ID
    book = None
    for b in books:
        if b['id'] == book_id:
            book = b
            break
    
    # Validate that the book exists and is available
    if not book:
        print(f"Error: No book exists with ID {book_id}.")
        return False
    
    if book['status'] != 'Available':
        print(f"Error: The book '{book['title']}' is not available for lending.")
        return False
    
    # Request borrower's name
    borrower_name = input("Enter the name of the person borrowing the book: ").strip()
    if not borrower_name:
        print("Error: Name cannot be empty.")
        return False
    
    # Verify lending limit per person (maximum 3)
    counter = 0
    for b in books:
        if b['status'] == 'Borrowed' and 'loan' in b and b['loan']['name'].lower() == borrower_name.lower():
            counter += 1
    
    if counter >= 3:
        print(f"Error: {borrower_name} already has 3 books borrowed (maximum allowed).")
        return False
    
    # Register the loan
    import datetime
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    book['status'] = 'Borrowed'
    book['loan'] = {
        'name': borrower_name,
        'date': current_date
    }
    
    print(f"\nBook '{book['title']}' successfully lent to {borrower_name}.")
    print(f"Loan date: {current_date}")
    return True


