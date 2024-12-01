# Write a program to create a simplified Library Management System using object-oriented programming principles in Python. This system should manage books and patrons (library users), allowing for basic operations such as adding new books, registering patrons, borrowing books, and returning books. 


class Library:
    def __init__(self):
        self.__books = []
        self.__users = []
        self.__id = 0
        self.len_books = len(self.__books)

    def add_user(self, user):
        self.__id += 1
        user.id = self.__id
        self.__users.append(user)

    def add_book(self, book):
        self.__books.append(book)

    def show_books(self):
        for i, book in enumerate(self.__books,start=1):
            print(f"{i} -> ", book)

    def borrow(self, bk_code):
        for book in self.__books:
            if book.bk_code == bk_code and book.available == True:
                user_id = int(input("Enter User Id: "))
                book.available = False
                book.borrower = user_id
                for user in self.__users:
                    if user.id == user_id:
                        user.borrowed_book = bk_code
                        print("Book borrowed successfully")
                        break
                    else:
                        print("Error while borrowing book try again")
                break
            else:
                print("Book not available")

    def return_book(self, user_id):
        for user in self.__users:
            if user.id == user_id and user.borrowed_book != None:
                user.borrowed_book = None
                for book in self.__books:
                    if book.borrower == user_id:
                        book.borrower = None
                        book.available = True
                        print("Book returned successfully")
                        break
            else:
                print("You didnt borrowed any book")
                break

    def show_users(self):
        for i, user in enumerate(self.__users, start=1):
            print(i , '. ',user)

class User:
    def __init__(self, name, email):
        self.id = None
        self.name = name
        self.email = email
        self.borrowed_book = None

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}"
    
class Book:
    def __init__(self, bk_code, bk_name):
        self.bk_code = bk_code
        self.bk_name = bk_name
        self.available = True
        self.borrower = None

    def __str__(self) -> str:
        return f"Id: {self.bk_code}, Book_Name: {self.bk_name}, Available: {self.available}, Borrower: {self.borrower}"



if __name__ == "__main__":
    print("Library Management System\n")

    lib = Library()

    while True:
        print("@ Menu")
        ch = int(input("1. Add user\n2. Add Book\n3. Show Books\n4. Borrow Book\n5. Return Book\n6. Show users\n7. Exit\n> "))

        if ch == 1:
            print("@ Adding user...")
            name = input("Enter name: ")
            email = input("Enter email: ")
            user = User(name, email)
            lib.add_user(user)
            print("User added...Id = ", user.id)
        
        elif ch == 2:
            print("@ Adding Books...")
            bk_code = input("Book Code: ")
            bk_name = input("Book Name: ")
            book = Book(bk_code, bk_name)
            lib.add_book(book)
            print(f"Book added\n{book}")

        elif ch == 3:
            print("@ Showing books...")
            lib.show_books()

        elif ch == 4:
            print("@ Borrowing Book...")
            lib.show_books()
            bk_code = input("Enter Book Code: ")
            lib.borrow(bk_code)
            

        elif ch == 5:
            print("@ Returning Book...")
            user_id = int(input("Enter User ID: "))
            lib.return_book(user_id)
        
        elif ch == 6:
            print("@ Showing Users...")
            lib.show_users()

        elif ch == 7:
            print("Exiting...")
            break

        print("\n")