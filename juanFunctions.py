import datetime
library = [] # Lista principal para almacenar libros
last_id = 0 # Variable para generar IDs únicos de forma incremental
ALLOWED_CATEGORIES = ['fiction', 'non fiction', 'children', 'educational'] # Lista de categorías permitidas
def generate_id(): # Función para generar un ID único autoincremental
    global last_id
    last_id += 1
    return last_id
def validate_text(field): # Función para validar campos de texto obligatorios
    value = input(f"Enter {field}: ").strip()
    if not value:
        print(f"Error: {field} is required.")
        return None
    return value
def validate_integer_range(field, minimum, maximum): # Función para validar números enteros dentro de un rango definido
    value = input(f"Enter {field} ({minimum}-{maximum}): ").strip()
    try:
        number = int(value)
        if number < minimum or number > maximum:
            print(f"Error: {field} must be between {minimum} and {maximum}.")
            return None
        return number
    except ValueError:
        print(f"Error: {field} must be an integer.")
        return None
def validate_category(): # Función para validar la categoría ingresada según las permitidas
    print("Allowed categories:", ", ".join(ALLOWED_CATEGORIES))
    category = input("Enter category: ").strip().lower()
    if category not in ALLOWED_CATEGORIES:
        print("Error: Invalid category.")
        return None
    return category
def Register_a_book(): # Función para registrar un nuevo libro en el inventario
    print("\n--- Register Book ---")
    title = validate_text("Title")
    if not title:
        return
    author = validate_text("Author")
    if not author:
        return
    current_year = datetime.datetime.now().year
    year = validate_integer_range("Year of Publication", 1500, current_year)
    if not year:
        return
    category = validate_category()
    if not category:
        return
    book = {  # Crear diccionario de libro con los datos validados
        'id': generate_id(),
        'title': title,
        'author': author,
        'year': year,
        'category': category,
        'status': 'Available'
    }
    library.append(book) # Agregar el libro a la lista principal
    print(f"Book successfully registered with ID {book['id']}.")

def Show_books(): # Función para mostrar todos los libros en el inventario
    if not library:
        print("The inventory is empty.")
        return
    print("\n--- Book Inventory ---")
    for book in library:
        print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Year: {book['year']} | Category: {book['category']} | Status: {book['status']}")
