class library:
    def __init__(self, book_name, author, available=True):
        self.book_name=book_name
        self.author=author
        self.available=available
    def check_out(self):
        if self.available:
            self.available=False
            print(f'"{self.book_name}"has been checked out.')
        else:
            print(f'"{self.book_name}"is currently not available.')

    def return_book(self):
        self.available=True
        print(f'"{self.book_name}"has been returned and is now available.')
    
    def display_book(self):
        status="Available" if self.available else "Not available"
        print(f"Book name:{self.book_name}, Author:{self.author}, Status:{status}")
book1=library("Python programming","Guido van rossum")
book2=library("Data structures","Mark allen weiss")

book1.display_book()
book1.check_out()
book1.display_book()