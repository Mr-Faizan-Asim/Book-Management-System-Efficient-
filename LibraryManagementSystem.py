import random

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
        self.available_copies = copies

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.transactions = []

    def add_book(self, title, author, copies):
        book = Book(title, author, copies)
        self.books.append(book)

    def add_user(self, name, id):
        user = User(name, id)
        self.users.append(user)

    def borrow_book(self, user_id, book_title):
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title and b.available_copies > 0), None)

        if user and book:
            book.available_copies -= 1
            transaction = {'user': user.name, 'book': book.title, 'action': 'borrow'}
            self.transactions.append(transaction)
            print(f"{user.name} borrowed {book.title}. Remaining copies: {book.available_copies}")
        else:
            print("Book not available or user not found.")

    def return_book(self, user_id, book_title):
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)

        if user and book:
            book.available_copies += 1
            transaction = {'user': user.name, 'book': book.title, 'action': 'return'}
            self.transactions.append(transaction)
            print(f"{user.name} returned {book.title}. Remaining copies: {book.available_copies}")
        else:
            print("Book not found or user not found.")

    def list_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author} - Available Copies: {book.available_copies}/{book.copies}")

    def list_users(self):
        for user in self.users:
            print(f"User ID: {user.id}, Name: {user.name}")

    def list_transactions(self):
        for transaction in self.transactions:
            print(f"User: {transaction['user']}, Book: {transaction['book']}, Action: {transaction['action']}")

    def recommend_book(self, user_id):
        user = next((u for u in self.users if u.id == user_id), None)
        if user:
            # Simple recommendation: Randomly choose a book from the library
            recommended_book = random.choice(self.books)
            print(f"Recommended book for {user.name}: {recommended_book.title} by {recommended_book.author}")
        else:
            print("User not found.")

    def find_most_popular_book(self):
        if self.transactions:
            book_counts = {}
            for transaction in self.transactions:
                book_title = transaction['book']
                book_counts[book_title] = book_counts.get(book_title, 0) + 1

            most_popular_book = max(book_counts, key=book_counts.get)
            print(f"Most popular book: {most_popular_book}")
        else:
            print("No transactions recorded.")

    # Add more functions...

# Example Usage
library = Library()

library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 5)
library.add_book("To Kill a Mockingbird", "Harper Lee", 3)
library.add_book("1984", "George Orwell", 4)

library.add_user("John Doe", 1)
library.add_user("Jane Doe", 2)

library.borrow_book(1, "The Great Gatsby")
library.borrow_book(2, "To Kill a Mockingbird")
library.borrow_book(1, "1984")

library.return_book(1, "The Great Gatsby")

library.list_books()
library.list_users()
library.list_transactions()

library.recommend_book(2)
library.find_most_popular_book()
