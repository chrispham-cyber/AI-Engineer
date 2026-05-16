from dataclasses import dataclass

@dataclass
class Book:
    title: str

@dataclass
class Member:
    name: str

class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.members = []
    
    def add_book(self, book: Book):
        self.books.append(book)

    def add_member(self, member: Member):
        self.members.append(member)

    def borrow_book(self, member: Member, book: Book):
        if book in self.books and member in self.members:
            self.books.remove(book)
            print(f"{member.name} borrowed {book.title}")
        else:
            print("Book or member not found in the library.")

    def return_book(self, member: Member, book: Book):
        if member in self.members:
            self.books.append(book)
            print(f"{member.name} returned {book.title}")
        else:
            print("Member not found in the library.")

# Example usage:
library = Library("City Library")
book1 = Book("Bible")
book2 = Book("Marvel Comics")
member1 = Member("Alex")

library.add_book(book1)
library.add_book(book2)
library.add_member(member1)
library.borrow_book(member1, book1)
library.return_book(member1, book1)