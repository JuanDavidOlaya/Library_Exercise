from generalFunctions import *
from juanFunctions import *
from stefaniaFunctions import *
from luisFunctions import *

flag = True

while flag:
    try:
        clear_screen()
        show_menu([
            "1. Register a book",
            "2. Show books",
            "3. Search books",
            "4. Lend a book",
            "5. Return a book",
            "6. Show borrowed books",
            "7. Exit"
        ], "LIBRARY MANAGEMENT SYSTEM")
        
        option = input(MAGENTA + "What do you want to do? " + RESET)
        clear_screen()
        
        if option == '1':
            Register_a_book()
        elif option == '2':
            Show_books()
        elif option == '3':
            search_a_book(library)
        elif option == '4':
            lend_a_book(library)
        elif option == '5':
            return_book(library)
        elif option == '6':
            show_borrowed_books(library)
        elif option == '7':
            delete_book(library)
        elif option == '8':
            print(GREEN + "Thank you for using the Library Management System. Goodbye!" + RESET)
            break
        else:
            print(RED + "Invalid option." + RESET)
            
        input(YELLOW + "\nPress Enter to continue..." + RESET)
        
    except ValueError:
        print(RED + "Invalid input, please enter a valid number." + RESET)
        input(YELLOW + "\nPress Enter to continue..." + RESET)
    except KeyboardInterrupt:
        print(YELLOW + "\nProgram interrupted by user." + RESET)
        break
