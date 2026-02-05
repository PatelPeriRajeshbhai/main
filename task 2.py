class Book:
    def __init__(self,title,author,ISBN,available_copies):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available_copies = available_copies
    
    def borrow(self):
        if self.available_copies > 0:
           self.available_copies -= 1
           return True
        return False 
    
    def return_book(self):
        self.available_copies += 1
            
    def display_info(self):
        print("Title:",self.title)
        print("author:",self.author)
        print("ISBN:",self.ISBN)
        print("available_copies:",self.available_copies)
        
class Member:
    def __init__(self,name,member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        
    def borrowed_books(self,book):
        if book.borrow():
          self.borrowed_books.append(book.title)

     
    def return_book(self,book):
        if book.title in self.borrowed_books:
           book.return_book()
           self.borrowed_books.remove(book.title)
        
    def display_borrowed_books(self):
         print(self.name, "borrowed:", self.borrowed_books)

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        
    def add_book(self,book):
        self.books.append(book)
        
    def add_member(self,member):
        self.members.append(member)
        
    def issue_book(self,isbn, member_id):
      for book in self.books:
        for member in self.members:
            if book.ISBN == isbn and member.member_id == member_id:
                if book.available_copies > 0:
                    book.available_copies -= 1
                    member.borrowed_books.append(book.title)
                    print("Book issued")
                    return
    print("Book or Member not found / Not available")
     
    def receive_book(self,book):
        for self.receive_book in book:
            if book == book:
                return "Book is receive"
            
    def dispalay_available_books(self):
       for book in self.books:
            if book.available_copies > 0:
                book.display_info()
            
lib = Library()

b1 = Book("Python", "Guido", "101", 2)
b2 = Book("DSA", "Narasimha", "102", 1)

m1 = Member("Rahul", "M01")

lib.add_book(b1)
lib.add_book(b2)
lib.add_member(m1)

lib. dispalay_available_books()
lib.issue_book("101","M01")
lib. dispalay_available_books()
lib.receive_book("101","M01")
lib. dispalay_available_books()

            
            
        
            
     

                          
        
        