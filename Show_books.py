def Show_books(): # Función para mostrar todos los libros en el inventario
    if not library:
        print("The inventory is empty.")
        return
    print("\n--- Book Inventory ---")
    for book in library:
        print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Year: {book['year']} | Category: {book['category']} | Status: {book['status']}")